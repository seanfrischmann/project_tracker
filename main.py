# ===========================================================================
# +++main.py+++|
# _____________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

import sqlite3 as lite

con = lite.connect('project_tracker.db')
cur = con.cursor()

#def create_project(name):

program_msg = ('\nTime Tracker\n'
			'Author: Sean Frischmann\n'
			'Test Simulation \n')

menu_msg = ('Please enter one of the following command:\n'
			'	create	--> to create a new project\n')

print(program_msg)


while True:
	print(menu_msg)
	user_input = raw_input('>> ')
	str(user_input)
	if user_input == 'exit':
		con.close()
		break
	elif user_input == 'create':
		print 'Enter the name of the project you wish to create:\n'
		project_name = raw_input('>> ')
		print ('Creating project named: ' + project_name + '\n')

print 'Done!'
