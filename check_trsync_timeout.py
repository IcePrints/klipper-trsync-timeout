#!/usr/bin/env python3
import configparser

CONFIG_PATH = '/home/biqu/printer_data/config/trsync.cfg'

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

try:
    timeout = float(config.get('mcu', 'trsync_timeout', fallback='0.025'))
    print(f"✅ TRSYNC_TIMEOUT is set to: {timeout:.3f} seconds")
except Exception as e:
    print(f"⚠️ Failed to read TRSYNC_TIMEOUT: {e}")
