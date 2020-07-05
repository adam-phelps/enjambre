# Contains all the api manager api calls.
# Adam Phelps 7/04/2020

import time
from enjcli import EnjCLI

class EnjManager():
    def __init__(self, console="no"):
        ''' You must install enj manager with CLI, web console optional.'''
        self.creation_date = {
            "epoch": time.time(),
            "friendly": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        }
        if console == "yes":
            launch_console()

    def launch_cli(self):
        myEnjCLI = EnjCLI()
        return myEnjCLI.create_parser()

    def launch_console(self):
        pass

    def __str__(self):
        ''' Return EnjManager friendly info.'''
        return f"EnjManager created at {self.creation_date['friendly']}"

