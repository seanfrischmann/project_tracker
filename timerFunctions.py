# ===========================================================================
# +++timerFunctions.py+++|
# ________________________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

import time
import scripts

def timer_function():
	scripts.start_timer_prompt()
	start_command = raw_input('>> ')
	if start_command == 'start' or start_command == 'Start':
		ret_dict = {'start_time':time.time()}
	elif start_command == 'cancel' or start_command == 'Cancel':
		return
	while True:
		scripts.stop_timer_prompt()
		end_command = raw_input('>> ')
		if end_command == 'stop' or end_command == 'Stop':
			end_dict = {'end_time':time.time()}
			ret_dict.update(end_dict)
			scripts.comment_prompt()
			end_comment = raw_input('>> ')
			final_dict = {'end_comment':raw_input('>> '),
					'total_time':end_dict.get('end_time')-ret_dict.get('start_time')}
			ret_dict.update(end_dict)
			ret_dict.update(final_dict)

			print ret_dict
			break

class timer_object():
	def start_end_timer():
		timer = int(time.time())
		return timer
	def convert_hours(time):
		hours = int(time/60)/60
		return hours
	def convert_minutes(time):
		minutes = int(time/60)%60
		return minutes
	def convert_seconds(time):
		seconds = int(time%60)
		return seconds
