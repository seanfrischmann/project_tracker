# ===========================================================================
# +++errors.py+++|
# _______________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

import sys

class myError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
