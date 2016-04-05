"""
roms.py

SUMMARY
This handles ROM files.
"""

import os
import logging as logs
logs.basicConfig(level=logs.DEBUG)
logger = logs.getLogger(__name__)

def main():
    rom_dir = "ROMS/"
    try:
        if not os.path.exists(rom_dir):
            logs.info("ROM folder not found. Please create a ROMS directory in your root folder titled '{}'".format(rom_dir))
            exit()
        # Find all .gb ROMS and map to a list
        found_roms = filter(lambda f: f.lower().endswith(".gb"), os.listdir(rom_dir))
        if len(found_roms) == 0:
            logs.error("No .gb ROMS found in '{}'".format(rom_dir))
            exit()
        else:
            for i, f in enumerate(found_roms):
                logs.info("{}\t{}".format(i + 1, f))

        # User input to choose which ROM to play
        filename = raw_input("Write the name or number of the ROM file:\n")
        try:
            filename = rom_dir + found_roms[int(filename) - 1]
            logs.info("Now Playing: '{}'".format(filename))
        except IndexError as ex:
            logs.error("That is not a valid choice!")
            raise ex

    # Gotta catch em all!
    except KeyboardInterrupt:
        logs.info("Interrupted by keyboard!")
    except Exception as ex:
        logs.error(ex.message)
        logs.error("You should try blowing dust off your cartridge and re-insert into Gameboy...")
        raise ex

    # Done!
    exit()


if __name__ == "__main__":
    main()

