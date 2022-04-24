#!/usr/bin/env python3

import os
import subprocess
import sys


def nofail(func):
    def decorated_func(*args, **kvargs):
        try:
            func(*args, **kvargs)
            return True
        except Exception as e:
            print(e)
            return False
    return decorated_func



class SystemShutdownActor:

    def __init__(self):
        pass

    def __call_command(self, *command, **kvargs):
        return subprocess.call(command, **kvargs)


    @nofail
    def _via_sysrq(self, emergency=False):
        # Enable SysRq poweroff
        open("/proc/sys/kernel/sysrq", "w").write("128")
        # Trigger SysRQ
        if emergency:
            command_series = ""
        else:
            command_series = "s"
        command_series += "o"
        for s in command_series:
            open("/proc/sysrq-trigger", "w").write(s)

    @nofail
    def _via_cmd_shutdown(self, emergency=False):
        self.__call_command("shutdown", "-h", "now")

    @nofail
    def _via_cmd_systemctl(self, emergency=False):
        self.__call_command("systemctl", "poweroff")

    @nofail
    def _via_cmd_poweroff(self, emergency=False):
        self.__call_command("poweroff")

    def __call__(self, emergency=False):
        if emergency:
            # priority
            self._via_sysrq(True)
        #self._via_cmd_shutdown(emergency=emergency)
        #self._via_cmd_systemctl(emergency=emergency)
        #self._via_cmd_poweroff(emergency=emergency)

        self._via_sysrq(False) # Try shutdown via SysRQ anyway
