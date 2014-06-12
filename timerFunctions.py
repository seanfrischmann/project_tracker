# ===========================================================================
# +++timerFunctions.py+++|
# _______________________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

import time
import scripts

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
    def get_hours(self,x):
        hours = int(x/60)/60
        return hours
    def get_minutes(self,x):
        minutes = int(x/60)%60
        return minutes
    def get_seconds(self,x):
        seconds = int(x%60)
        return seconds
