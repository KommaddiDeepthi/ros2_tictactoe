#!/usr/bin/env python3

def try_import(mod_name):
    try:
        mod = __import__(mod_name)
        print(f"\n✅ Imported {mod_name}")
        for fn in ["movej", "movel", "wait", "set_robot_mode"]:
            print(f"  {fn}: {hasattr(mod, fn)}")
    except Exception as e:
        print(f"\n❌ Could not import {mod_name}: {e}")

def main():
    try_import("DR_init")
    try_import("DR_common2")
    try_import("DSR_ROBOT2")

if __name__ == "__main__":
    main()
