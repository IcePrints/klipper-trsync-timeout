#!/usr/bin/env python3
import os

FILE_PATH = '/home/biqu/klipper/klippy/mcu.py'
TIMEOUT_LINE = 'TRSYNC_TIMEOUT = 0.025'
CUSTOM_LINE = (
    'import configparser\n'
    'config = configparser.ConfigParser()\n'
    "config.read('/home/biqu/printer_data/config/trsync.cfg')\n"
    "try:\n"
    "    TRSYNC_TIMEOUT = float(config.get('mcu', 'trsync_timeout', fallback='0.025'))\n"
    "except Exception:\n"
    "    TRSYNC_TIMEOUT = 0.025\n"
)

def update_file():
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()

    if any('configparser' in line for line in lines):
        print("✅ Patch already applied.")
        return

    for i, line in enumerate(lines):
        if TIMEOUT_LINE in line:
            lines[i] = CUSTOM_LINE
            break
    else:
        print("⚠️ Could not find TRSYNC_TIMEOUT line.")
        return

    with open(FILE_PATH, 'w') as f:
        f.writelines(lines)

    print("✨ Patch applied successfully.")

if __name__ == '__main__':
    update_file()

