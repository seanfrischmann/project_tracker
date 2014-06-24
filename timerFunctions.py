# ===========================================================================
# +++timerFunctions.py+++|
# _______________________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

import time
import scripts
from datetime import datetime 

# ***************************************************************************
# |Timer Object|
#
# The timer object is used to keep track of a project time, including break
# times.
#
# ***************************************************************************
class Timer_object():
    def __init__(self):
        self.start = 0
        self.stop = 0
        self.time = 0
        self.break_start = 0
        self.break_stop = 0
        self.break_time = 0
    def start_break(self):
        self.time += (time.time() - self.start)
        self.break_start = time.time()
    def stop_break(self):
        self.break_stop = time.time()
        self.break_time = self.break_stop - self.break_start
        self.start = time.time()
    def start_time(self):
        self.start = int(time.time())
    def stop_time(self):
        self.stop = int(time.time())
        self.time += (self.stop - self.start)
    def get_current(self):
        current = datetime.strftime(datetime.now(), '%I:%M:%S %p')
        return current
    def get_elapsed(self,x):
        elapsed = int(time.time()) - x
        return elapsed
    def get_time(self,x):
        hours = int(int(x/60)/60)
        minutes = int(int(x/60)%60)
        seconds = int(x%60)
        if hours < 10:
            hours = '0' + str(hours)
        if minutes < 10:
            minutes = '0' + str(minutes)
        if seconds < 10:
            seconds = '0' + str(seconds)
        time = str(hours) + ':' + str(minutes) + ':' + str(seconds)
        return time
