# ===========================================================================
# +++main.py+++|
# _____________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

import sqlite3 as lite
import createProject
import selectProject
import sys
import scripts
import timerFunctions

con = lite.connect('project_tracker.db')
cur = con.cursor()

scripts.program_message()

while True:
	scripts.main_menu()
	user_input = raw_input('>> ')
	str(user_input)
	if user_input == 'exit':
		con.commit()
		con.close()
		print '\nBon Voyage!\n'
		sys.exit(0)
	elif user_input == 'create':
		scripts.project_name_prompt()
		project_name = raw_input('>> ')
		scripts.project_description_prompt()
		project_description = raw_input('>> ')
		scripts.creating_project_prompt(project_name)
		createProject.list_of_projects(cur, project_name, project_description)
	elif user_input == 'select project':
		scripts.project_list_prompt()
		selectProject.display_existing_projects(cur)
		scripts.select_project_prompt()
		project_select = raw_input('>> ')
		if project_select != 'Cancel':
			check = selectProject.check_existing_projects(cur, project_select)
			if check is True:
				while True:
					scripts.select_menu()
					entry_choice = raw_input('>> ')
					if entry_choice == 'View Entry':
						create = False
						is_entry = selectProject.check_worksheet(cur, create)
						if is_entry is True:
							print 'entry exists'
							break
						else:
							print 'There is no entry'
							break
					elif entry_choice == 'New Entry':
						create = True
						selectProject.check_worksheet(cur, create)
						timerFunctions.timer_function()
						print 'making new entry'
						break
					elif entry_choice == 'Cancel':
						break
					else:
						scripts.select_menu_error()
			else:
				scripts.does_not_exist_error()
	else:
		scripts.wrong_command_error()
