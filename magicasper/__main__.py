#!/usr/bin/env python3

import argparse
from .shutdown import SystemShutdownActor

argparser = argparse.ArgumentParser(
    prog="python3 -m magicasper",
    description="""
    MAGICASPER is a tool for controlling system power supply. It may run as a
    daemon or called via command line. In case of emergency, this tool may also
    shutdown the system aggressively using multiple methods (which may cause
    data corruption).
    """)
argparser.add_argument("action", choices=["shutdown"])
argparser.add_argument(
    "--emergency", "-e",
    help="Shutdown in emergency mode.",
    action="store_true")
args = argparser.parse_args()



if args.action == "shutdown":
    actor = SystemShutdownActor()
    actor(emergency=args.emergency)
