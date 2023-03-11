# C project: Bachelor Thesis
BUILD_DIR=./build
OS_NAME="Linux"

##############################################

.PHONY: build rubber_ducky doc run_tests pack clean

all: build

build: $(BUILD_DIR)/Makefile
	make -C$(BUILD_DIR) -j8

rubber_ducky: $(BUILD_DIR)/Makefile
	make -C$(BUILD_DIR) -j8 rubber_ducky

doc: Doxygen
	doxygen

pack: src/* README.md Makefile CMakeLists.txt Doxygen
	rm -f *.zip
	zip -r $(TARGET_NAME) $^

run_tests:
	cd scripts/tests/ && pytest

clean:
	rm -rf doc *.zip $(BUILD_DIR)

##############################################

$(BUILD_DIR)/Makefile: CMakeLists.txt ./rubber_ducky/*
	cmake -H. -B$(BUILD_DIR) -DCMAKE_BUILD_TYPE=Debug -DCMAKE_EXPORT_COMPILE_COMMANDS=YES -DPICO_SDK_PATH=pico-sdk/ -DOS_NAME=$(OS_NAME)
	cp $(BUILD_DIR)/compile_commands.json .

