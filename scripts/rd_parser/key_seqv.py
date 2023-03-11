import enum

class Modifier(enum.Enum):
    LCTRL = 'KEYBOARD_MODIFIER_LEFTCTRL'
    LSHIFT = 'KEYBOARD_MODIFIER_LEFTSHIFT'
    LALT = 'KEYBOARD_MODIFIER_LEFTALT'
    LMETA = 'KEYBOARD_MODIFIER_LEFTGUI'
    RCTRL = 'KEYBOARD_MODIFIER_RIGHTCTRL'
    RSHIFT = 'KEYBOARD_MODIFIER_RIGHTSHIFT'
    RALT = 'KEYBOARD_MODIFIER_RIGHTALT'
    RMETA = 'KEYBOARD_MODIFIER_RIGHTGUI'

class Key(enum.Enum):
    KEY_A = 'HID_KEY_A'
    KEY_B = 'HID_KEY_B'
    KEY_C = 'HID_KEY_C'
    KEY_D = 'HID_KEY_D'
    KEY_E = 'HID_KEY_E'
    KEY_F = 'HID_KEY_F'
    KEY_G = 'HID_KEY_G'
    KEY_H = 'HID_KEY_H'
    KEY_I = 'HID_KEY_I'
    KEY_J = 'HID_KEY_J'
    KEY_K = 'HID_KEY_K'
    KEY_L = 'HID_KEY_L'
    KEY_M = 'HID_KEY_M'
    KEY_N = 'HID_KEY_N'
    KEY_O = 'HID_KEY_O'
    KEY_P = 'HID_KEY_P'
    KEY_Q = 'HID_KEY_Q'
    KEY_R = 'HID_KEY_R'
    KEY_S = 'HID_KEY_S'
    KEY_T = 'HID_KEY_T'
    KEY_U = 'HID_KEY_U'
    KEY_V = 'HID_KEY_V'
    KEY_W = 'HID_KEY_W'
    KEY_X = 'HID_KEY_X'
    KEY_Y = 'HID_KEY_Y'
    KEY_Z = 'HID_KEY_Z'
    KEY_1 = 'HID_KEY_1'
    KEY_2 = 'HID_KEY_2'
    KEY_3 = 'HID_KEY_3'
    KEY_4 = 'HID_KEY_4'
    KEY_5 = 'HID_KEY_5'
    KEY_6 = 'HID_KEY_6'
    KEY_7 = 'HID_KEY_7'
    KEY_8 = 'HID_KEY_8'
    KEY_9 = 'HID_KEY_9'
    KEY_0 = 'HID_KEY_0'
    KEY_ENTER = 'HID_KEY_ENTER'
    KEY_ESCAPE = 'HID_KEY_ESCAPE'
    KEY_BACKSPACE = 'HID_KEY_BACKSPACE'
    KEY_TAB = 'HID_KEY_TAB'
    KEY_SPACE = 'HID_KEY_SPACE'
    KEY_MINUS = 'HID_KEY_MINUS'
    KEY_EQUAL = 'HID_KEY_EQUAL'
    KEY_BRACKET_LEFT = 'HID_KEY_BRACKET_LEFT'
    KEY_BRACKET_RIGHT = 'HID_KEY_BRACKET_RIGHT'
    KEY_BACKSLASH = 'HID_KEY_BACKSLASH'
    KEY_EUROPE_1 = 'HID_KEY_EUROPE_1'
    KEY_SEMICOLON = 'HID_KEY_SEMICOLON'
    KEY_APOSTROPHE = 'HID_KEY_APOSTROPHE'
    KEY_GRAVE = 'HID_KEY_GRAVE'
    KEY_COMMA = 'HID_KEY_COMMA'
    KEY_PERIOD = 'HID_KEY_PERIOD'
    KEY_SLASH = 'HID_KEY_SLASH'
    KEY_CAPS_LOCK = 'HID_KEY_CAPS_LOCK'
    KEY_F1 = 'HID_KEY_F1'
    KEY_F2 = 'HID_KEY_F2'
    KEY_F3 = 'HID_KEY_F3'
    KEY_F4 = 'HID_KEY_F4'
    KEY_F5 = 'HID_KEY_F5'
    KEY_F6 = 'HID_KEY_F6'
    KEY_F7 = 'HID_KEY_F7'
    KEY_F8 = 'HID_KEY_F8'
    KEY_F9 = 'HID_KEY_F9'
    KEY_F10 = 'HID_KEY_F10'
    KEY_F11 = 'HID_KEY_F11'
    KEY_F12 = 'HID_KEY_F12'
    KEY_PRINT_SCREEN = 'HID_KEY_PRINT_SCREEN'
    KEY_SCROLL_LOCK = 'HID_KEY_SCROLL_LOCK'
    KEY_PAUSE = 'HID_KEY_PAUSE'
    KEY_INSERT = 'HID_KEY_INSERT'
    KEY_HOME = 'HID_KEY_HOME'
    KEY_PAGE_UP = 'HID_KEY_PAGE_UP'
    KEY_DELETE = 'HID_KEY_DELETE'
    KEY_END = 'HID_KEY_END'
    KEY_PAGE_DOWN = 'HID_KEY_PAGE_DOWN'
    KEY_ARROW_RIGHT = 'HID_KEY_ARROW_RIGHT'
    KEY_ARROW_LEFT = 'HID_KEY_ARROW_LEFT'
    KEY_ARROW_DOWN = 'HID_KEY_ARROW_DOWN'
    KEY_ARROW_UP = 'HID_KEY_ARROW_UP'
    KEY_NUM_LOCK = 'HID_KEY_NUM_LOCK'
    KEY_KEYPAD_DIVIDE = 'HID_KEY_KEYPAD_DIVIDE'
    KEY_KEYPAD_MULTIPLY = 'HID_KEY_KEYPAD_MULTIPLY'
    KEY_KEYPAD_SUBTRACT = 'HID_KEY_KEYPAD_SUBTRACT'
    KEY_KEYPAD_ADD = 'HID_KEY_KEYPAD_ADD'
    KEY_KEYPAD_ENTER = 'HID_KEY_KEYPAD_ENTER'
    KEY_KEYPAD_1 = 'HID_KEY_KEYPAD_1'
    KEY_KEYPAD_2 = 'HID_KEY_KEYPAD_2'
    KEY_KEYPAD_3 = 'HID_KEY_KEYPAD_3'
    KEY_KEYPAD_4 = 'HID_KEY_KEYPAD_4'
    KEY_KEYPAD_5 = 'HID_KEY_KEYPAD_5'
    KEY_KEYPAD_6 = 'HID_KEY_KEYPAD_6'
    KEY_KEYPAD_7 = 'HID_KEY_KEYPAD_7'
    KEY_KEYPAD_8 = 'HID_KEY_KEYPAD_8'
    KEY_KEYPAD_9 = 'HID_KEY_KEYPAD_9'
    KEY_KEYPAD_0 = 'HID_KEY_KEYPAD_0'
    KEY_KEYPAD_DECIMAL = 'HID_KEY_KEYPAD_DECIMAL'
    KEY_EUROPE_2 = 'HID_KEY_EUROPE_2'
    KEY_APPLICATION = 'HID_KEY_APPLICATION'
    KEY_POWER = 'HID_KEY_POWER'
    KEY_KEYPAD_EQUAL = 'HID_KEY_KEYPAD_EQUAL'
    KEY_F13 = 'HID_KEY_F13'
    KEY_F14 = 'HID_KEY_F14'
    KEY_F15 = 'HID_KEY_F15'
    KEY_F16 = 'HID_KEY_F16'
    KEY_F17 = 'HID_KEY_F17'
    KEY_F18 = 'HID_KEY_F18'
    KEY_F19 = 'HID_KEY_F19'
    KEY_F20 = 'HID_KEY_F20'
    KEY_F21 = 'HID_KEY_F21'
    KEY_F22 = 'HID_KEY_F22'
    KEY_F23 = 'HID_KEY_F23'
    KEY_F24 = 'HID_KEY_F24'
    KEY_EXECUTE = 'HID_KEY_EXECUTE'
    KEY_HELP = 'HID_KEY_HELP'
    KEY_MENU = 'HID_KEY_MENU'
    KEY_SELECT = 'HID_KEY_SELECT'
    KEY_STOP = 'HID_KEY_STOP'
    KEY_AGAIN = 'HID_KEY_AGAIN'
    KEY_UNDO = 'HID_KEY_UNDO'
    KEY_CUT = 'HID_KEY_CUT'
    KEY_COPY = 'HID_KEY_COPY'
    KEY_PASTE = 'HID_KEY_PASTE'
    KEY_FIND = 'HID_KEY_FIND'
    KEY_MUTE = 'HID_KEY_MUTE'
    KEY_VOLUME_UP = 'HID_KEY_VOLUME_UP'
    KEY_VOLUME_DOWN = 'HID_KEY_VOLUME_DOWN'
    KEY_LOCKING_CAPS_LOCK = 'HID_KEY_LOCKING_CAPS_LOCK'
    KEY_LOCKING_NUM_LOCK = 'HID_KEY_LOCKING_NUM_LOCK'
    KEY_LOCKING_SCROLL_LOCK = 'HID_KEY_LOCKING_SCROLL_LOCK'
    KEY_KEYPAD_COMMA = 'HID_KEY_KEYPAD_COMMA'
    KEY_KEYPAD_EQUAL_SIGN = 'HID_KEY_KEYPAD_EQUAL_SIGN'
    KEY_KANJI1 = 'HID_KEY_KANJI1'
    KEY_KANJI2 = 'HID_KEY_KANJI2'
    KEY_KANJI3 = 'HID_KEY_KANJI3'
    KEY_KANJI4 = 'HID_KEY_KANJI4'
    KEY_KANJI5 = 'HID_KEY_KANJI5'
    KEY_KANJI6 = 'HID_KEY_KANJI6'
    KEY_KANJI7 = 'HID_KEY_KANJI7'
    KEY_KANJI8 = 'HID_KEY_KANJI8'
    KEY_KANJI9 = 'HID_KEY_KANJI9'
    KEY_LANG1 = 'HID_KEY_LANG1'
    KEY_LANG2 = 'HID_KEY_LANG2'
    KEY_LANG3 = 'HID_KEY_LANG3'
    KEY_LANG4 = 'HID_KEY_LANG4'
    KEY_LANG5 = 'HID_KEY_LANG5'
    KEY_LANG6 = 'HID_KEY_LANG6'
    KEY_LANG7 = 'HID_KEY_LANG7'
    KEY_LANG8 = 'HID_KEY_LANG8'
    KEY_LANG9 = 'HID_KEY_LANG9'
    KEY_ALTERNATE_ERASE = 'HID_KEY_ALTERNATE_ERASE'
    KEY_SYSREQ_ATTENTION = 'HID_KEY_SYSREQ_ATTENTION'
    KEY_CANCEL = 'HID_KEY_CANCEL'
    KEY_CLEAR = 'HID_KEY_CLEAR'
    KEY_PRIOR = 'HID_KEY_PRIOR'
    KEY_RETURN = 'HID_KEY_RETURN'
    KEY_SEPARATOR = 'HID_KEY_SEPARATOR'
    KEY_OUT = 'HID_KEY_OUT'
    KEY_OPER = 'HID_KEY_OPER'
    KEY_CLEAR_AGAIN = 'HID_KEY_CLEAR_AGAIN'
    KEY_CRSEL_PROPS = 'HID_KEY_CRSEL_PROPS'
    KEY_EXSEL = 'HID_KEY_EXSEL'
    KEY_SHIFT_LEFT = 'HID_KEY_SHIFT_LEFT'
    KEY_ALT_LEFT = 'HID_KEY_ALT_LEFT'
    KEY_GUI_LEFT = 'HID_KEY_GUI_LEFT'
    KEY_CONTROL_RIGHT = 'HID_KEY_CONTROL_RIGHT'
    KEY_SHIFT_RIGHT = 'HID_KEY_SHIFT_RIGHT'
    KEY_ALT_RIGHT = 'HID_KEY_ALT_RIGHT'
    KEY_GUI_RIGHT = 'HID_KEY_GUI_RIGHT'


class KeySeqv:

    def __init__(self, keys: list[Key], delay: int=0,
                 modifiers: list[Modifier]=[], last: bool=False):
        self.__delay = delay
        self.__modifiers = modifiers
        self.__keys = keys
        self.__last = last


    @property
    def delay(self) -> int:
        return self.__delay


    @property
    def modifiers(self) -> tuple[Modifier]:
        return tuple(self.__modifiers)


    @property
    def keys(self) -> tuple[Key]:
        return tuple(self.__keys)


    @property
    def last(self) -> bool:
        return self.__last


    @last.setter
    def last(self, value: bool):
        self.__last = value


    def __str__(self) -> str:
        out = '    {'
        out += f'{self.__delay}, {{'
        if self.__modifiers:
            out += '|'.join([m.value for m in self.__modifiers])
        else:
            out += '0'
        out += ', 0, {'
        if self.__keys:
            out += ', '.join([k.value for k in self.__keys])
        else:
            out += '0,'
        out += '}}, '
        out += f'{"true" if self.__last else "false"}}},\n'
        return out


    def __repr__(self) -> str:
        return str(self)
