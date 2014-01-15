# ===========================================================================
# +++main.py+++|
# _____________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

import sqlite3 as lite
import posixpath as pos
import sys
import createProject
import selectProject
import sys
import scripts
import timerFunctions
import errors

create_database = pos.isfile('project_tracker.db')

con = lite.connect('project_tracker.db')
cur = con.cursor()

if not create_database:
	createProject.list_of_projects(cur)
	createProject.create_worksheet(cur)
	print 'creating database'

scripts.program_message()

while True:
	try:
		scripts.main_menu()
		user_input = raw_input('>> ')
		str(user_input)
		if (user_input == 'exit' or user_input == 'Exit' or user_input == 'quit' 
				or user_input == 'Quit'):
			con.commit()
			con.close()
			print '\nBon Voyage!\n'
			sys.exit(0)
		elif user_input == 'create' or user_input == 'Create':
			scripts.project_name_prompt()
			project_name = raw_input('>> ')
			scripts.project_description_prompt()
			project_description = raw_input('>> ')
			scripts.creating_project_prompt(project_name)
			createProject.create_project(cur, project_name, project_description)
		elif user_input == 'select' or user_input == 'Select':
			while True:
				scripts.project_list_prompt()
				selectProject.display_existing_projects(cur)
				for row in cur:
					print "--> ", row[0]
				scripts.select_project_prompt()
				project_select = raw_input('>> ')
				if project_select == 'Cancel' or project_select == 'cancel':
					break
				else:
					selectProject.check_existing_projects(cur, project_select)
					scripts.select_menu()
					entry_choice = raw_input('>> ')
					if entry_choice == 'View' or entry_choice == 'view':
						print 'Viewing entry'
					elif entry_choice == 'New' or entry_choice == 'new':
						timerFunctions.timer_function()
						print 'making new entry'
					elif entry_choice == 'Cancel' or entry_choice == 'cancel':
						break
					else:
						raise errors.myError('invalid entry\n')
		else:
			raise errors.myError('invalid entry\n')
	except errors.myError as err:
		print ('Error: '+err.value)
