import logging
import re
import sys
from io import TextIOWrapper
from typing import TextIO
from datetime import datetime

from .key_seqv import KeySeqv
from .regex_groups import Groups, KEY_SEQV_REGEX, LINE_REGEX
from .mappings import *


HEADER_CONTENT = \
"""/**
 * @brief Defines key sequence for Linux systems.
 *
 * This particular set of key sequence was generated by rd_parser module.
 *
 * This source code serves as submission to my bachelor thesis topic
 * "Implement Rubber Duckies on Available USB Devices and Make a Practical Test"
 * at FIT, BUT 2022/23.
 *
 * @author Hung Do
 * @date {}
 */
#include "key_seqv.h"

/// List of key sequences for (my) Linux system
struct key_seqv_t key_seqvs[] = {{
    INITIAL_DELAY,
""".format(datetime.strftime(datetime.today(), '%d/%m/%Y'))

FOOTER_CONTENT = \
"""};
"""

class KeySeqvParser:

    def __init__(self, in_file: TextIO|TextIOWrapper=sys.stdin,
                 out_file: TextIO|TextIOWrapper=sys.stdout):
        self._in_file = in_file
        self._out_file = out_file
        self._lof_keyseqvs: list[KeySeqv] = []
        self.__new_sequence_structure()
        self._compile_patterns()


    @property
    def lof_keyseqvs(self) -> tuple:
        """Returns set of key sequences."""
        return tuple(self._lof_keyseqvs)


    def _compile_patterns(self):
        self._line_regex = re.compile(LINE_REGEX)
        self._key_seqv_regex = re.compile(KEY_SEQV_REGEX)


    def clear_lof_keyseqvs(self):
        """Clear the set of key sequences."""
        self._lof_keyseqvs.clear()


    def set_out_file(self, new_out_file: TextIO|TextIOWrapper):
        if new_out_file:
            self._out_file = new_out_file


    def set_in_file(self, new_in_file: TextIO|TextIOWrapper):
        if new_in_file:
            self._in_file = new_in_file



    def __new_sequence_structure(self):
        """Create a new structure for the keys."""
        self.__ks_struct = {
            'delay': 0,
            'modifiers': [],
            'keys': []
        }


    def __push_pressed_and_released(self):
        """Simulate keys press and prepare new key sequence structure."""
        # keys pressed
        self._lof_keyseqvs.append(KeySeqv(**self.__ks_struct))
        self.__new_sequence_structure()
        # keys released
        self._lof_keyseqvs.append(KeySeqv(**self.__ks_struct))
        self.__new_sequence_structure()


    def __check_normal_keys(self, value: str):
        # check if symbol requires shift modifier
        if value in shift_mapping or value.isupper():
            key_macro_name = normal_mapping[shift_mapping[value]] \
                             if value in shift_mapping else \
                             normal_mapping[value.lower()]
            # first check if the key is already being pressed
            # if so we need to release it first (push current sequence)
            # and press it again
            if key_macro_name in self.__ks_struct['keys']:
                self.__push_pressed_and_released()

            # new sequence
            if not self.__ks_struct['keys']:
                self.__ks_struct['modifiers'].append(Modifier.LSHIFT)
            # shift is not toggled yet push the key sequence first
            elif Modifier.LSHIFT not in self.__ks_struct['modifiers'] and \
                 Modifier.RSHIFT not in self.__ks_struct['modifiers']:
                self.__push_pressed_and_released()
                self.__ks_struct['modifiers'].append(Modifier.LSHIFT)

            self.__ks_struct['keys'].append(key_macro_name)

        else:
            key_macro_name = normal_mapping[value]
            # first check if the key is already being pressed
            # if so we need to release it first (push current sequence)
            # and press it again
            if key_macro_name in self.__ks_struct['keys']:
                self.__push_pressed_and_released()

            # if shift is toggled push the key sequence first
            if Modifier.LSHIFT in self.__ks_struct['modifiers'] or \
               Modifier.RSHIFT in self.__ks_struct['modifiers']:
                self.__push_pressed_and_released()
            self.__ks_struct['keys'].append(normal_mapping[value])


    def __parse_normal_keys_in_special(self, keys: str) -> tuple[bool, list[Key]]:
        keys_pressed = []
        for i in keys:
            pass
        return True, keys_pressed


    def __check_special_keys(self, match: list, line_index: int):
        used_modifiers: list[Modifier] = []
        if match[Groups.SPECIAL_MODIFIERS.value]:
            # extracts modifiers
            seqv_modifiers = match[Groups.SPECIAL_MODIFIERS.value].split('-')[:-1]
            for m in seqv_modifiers:
                if not modifier_mapping.get(m.lower()):
                    logging.error(f'Unexpected modifier "{m}" in',
                                   '"{match[Groups.SPECIAL_ORIGINAL.value]}" on line {line_index+1}!')
                    # FIXME: exception
                    continue
                if modifier_mapping[m.lower()] in used_modifiers:
                    logging.warn(f'Duplicate use of modifier "{m}" in',
                                  '"{match[Groups.SPECIAL_ORIGINAL.value]}" on line {line_index+1}')
                    continue
                used_modifiers.append(modifier_mapping[m.lower()])

        special_value: str = match[Groups.SPECIAL_VALUE.value]
        # the escape sign on this position tells the parser that
        # the next set of characters defines a special keys name
        # (special_mapping or special_key_naming)
        if match[Groups.SPECIAL_ESCAPE_EN.value]:
            # special key (like escape or return)
            if special_value.lower() in special_mapping:
                self.__ks_struct['keys'].append(special_mapping[special_value.lower()])
                self.__ks_struct['modifiers'] = used_modifiers
                # FIXME: delay
                self.__push_pressed_and_released()
                return
            if special_value.lower() in special_key_naming:
                # add shift if not toggled yet
                # TODO: shift error
                key_modifier, key_value = special_key_naming[special_value.lower()]
                if key_modifier and key_modifier not in used_modifiers:
                    used_modifiers.append(key_modifier)

                self.__ks_struct['keys'].append(key_value)
                self.__ks_struct['modifiers'] = used_modifiers
                # FIXME: delay
                self.__push_pressed_and_released()
                return
            # TODO: error unknown special key name
            logging.error(f'Unknown special key value:',
                           '"{match[Groups.SPECIAL_ORIGINAL.value]}" on line {line_index+1}')

        # otherwise normal keys are expected
        # can't send more than 6 keys at once
        if len(special_value) > 6:
            logging.error(f'Special sequence value is too long (max 6 keys):',
                           '"{match[Groups.SPECIAL_ORIGINAL.value]}" on line {line_index+1}')
            return
        # shift should not be toggled yet
        if (Modifier.LSHIFT in used_modifiers or
            Modifier.RSHIFT in used_modifiers):
            logging.error('When pressing normal keys, special key sequence should',
                          'not contain shift modifier in the script.')
            logging.error(f'Remove "s-" from {match[Groups.SPECIAL_ORIGINAL.value]} on line {line_index+1}')
            return
        # TODO: test duplicity
        is_shift_toggled, keys_pressed = self.__parse_normal_keys_in_special(special_value)
        if is_shift_toggled:
            used_modifiers.append(Modifier.LSHIFT)
        self.__ks_struct['modifiers'] = used_modifiers
        self.__ks_struct['keys'] = keys_pressed
        # TODO: push but with delay


    def parse_line(self, line: str, line_index: int):

        self.__new_sequence_structure()
        matches = self._key_seqv_regex.findall(line)

        for match in matches:
            # TODO: hold delay
            # wait delay
            if match[Groups.DELAY_WAIT_ORIGINAL.value]:
                # finish previous sequence and add delay to the new one
                if self.__ks_struct['keys'] or self.__ks_struct['delay']:
                    # keys pressed
                    self._lof_keyseqvs.append(KeySeqv(**self.__ks_struct))
                    self.__new_sequence_structure()
                # keys release with delay
                self.__ks_struct['delay'] = int(match[Groups.DELAY_WAIT_VALUE.value])
                self._lof_keyseqvs.append(KeySeqv(**self.__ks_struct))
                self.__new_sequence_structure()

            # max 6 keys pressed are allowed to be sent at the same time
            if len(self.__ks_struct['keys']) > 5:
                self.__push_pressed_and_released()

            # load special
            if match[Groups.SPECIAL_ORIGINAL.value]:
                # push current sequence and create it for special sequence
                if self.__ks_struct['keys']:
                    self.__push_pressed_and_released()
                self.__check_special_keys(match, line_index)

            # ignoring comments
            if match[Groups.COMMENT.value]:
                pass

            # load normal keys
            elif match[Groups.NORMAL_KEYS.value]:
                value: str = match[Groups.NORMAL_KEYS.value]
                self.__check_normal_keys(value)

        # finish last item pending (if exists)
        if self.__ks_struct['keys']:
            self.__push_pressed_and_released()


    def parse_content(self):
        """Parse the input file."""

        for i, line in enumerate(self._in_file):
            # line check
            if not self._line_regex.match(line):
                logging.warn(f'Unexpected character in line {i+1}')
                continue

            # parsing
            self.parse_line(line, i)

        # set last item as last item
        if self._lof_keyseqvs:
            last_item = self._lof_keyseqvs[-1]
            last_item.last = True


    def generate_output_file(self):
        # generate header
        self._out_file.write(HEADER_CONTENT)
        # generate content
        for ks in self._lof_keyseqvs:
            self._out_file.write(str(ks))
        # generate footer
        self._out_file.write(FOOTER_CONTENT)
