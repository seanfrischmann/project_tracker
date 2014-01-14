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
