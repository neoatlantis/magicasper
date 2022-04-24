#!/usr/bin/env python3

import os
import sys


class SystemShutdownActor:

    def __init__(self):
        pass

    def __send_sysrq(self, signal):
        if os.path.isfile("/proc/sysrq-trigger"):
            self.__write_file("/proc/sysrq-trigger", signal)
            return True
        return False

    def __call_command(self, *command):
        pass


    def _via_sysrq(self, emergency=False):
        
        pass

    def _via_cmd_shutdown(self, emergency=False):
        if emergency: return False
        self.__call_command("shutdown", "-h", "now")
        return True

    def __call__(self, emergency=False):
        self._via_cmd_shutdown(emergency=emergency)
