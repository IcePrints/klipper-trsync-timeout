# 🛠️ Klipper: Configurable TRSYNC_TIMEOUT with Automated Workflow

This repo makes Klipper’s `TRSYNC_TIMEOUT` value configurable through an external `.cfg` file—and ensures the patch re-applies automatically after every Klipper update. Ideal for advanced setups with multiple MCUs or sync-sensitive hardware.

## 🚀 What This Includes

- 🔧 Patch to `klippy/mcu.py` using Python's `configparser`
- 🗂 External config file: `trsync.cfg`, avoids breaking Klipper's native validation
- 🤖 Patch automation: a Python script + bash update flow
- ✅ Sanity check tool to confirm runtime values
- 🔁 Optional Moonraker/Mainsail integration via post-update hook

## 📦 Included Files

| File                      | Purpose                                         |
|---------------------------|-------------------------------------------------|
| `update_trsync_timeout.py`| Applies the patch to `mcu.py`                   |
| `check_trsync_timeout.py` | Prints the current timeout from your config     |
| `update-klipper.sh`       | Automates updates + patch reapplication         |
| `trsync_timeout.patch`    | Unified diff backup patch (optional)            |
| `trsync.cfg`              | External config file (not validated by Klipper) |

## 📜 License

MIT for code. Documentation may be covered by [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
