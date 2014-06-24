# ===========================================================================
# +++scripts.py+++|
# ________________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

# ***************************************************************************
# The following are a series of scripts used to print messages to the terminal
# ***************************************************************************

def program_message():
	print ('\nTime Tracker\n'
			'Author: Sean Frischmann\n'
			'Test Simulation \n')

def main_menu():
	print ('\nPlease enter one of the following commands:\n'
			'	create	--> to create a new project\n'
			'	select	--> to select an existing project\n')

def project_name_prompt():
	print ('\nEnter the name of the project you wish to create:\n')

def project_description_prompt():
	print ('\nEnter a brief description of the project')

def creating_project_prompt(project_name):
	print ('\nCreating project named: ' + project_name + '\n')

def project_list_prompt():
	print ('\nThe following are a list of existing projects:')

def select_project_prompt():
	print ('\nEnter the project you wish to select or enter Cancel to\n'
			'go back to the main menu:')

def select_menu():
	print ('\nWhat would you like to do?\n'
			'	View	--> view an existing entry\n'
			'	New		--> create a new entry\n'
			'	Cancel	--> exit to main menu\n')

def start_timer_prompt():
	print ('\nWhen you are ready to start the timer, please enter Start or'
			'\n Cancel to go back to the main menu:')

def stop_timer_prompt():
	print ('\nWhen you are ready to stop the timer, enter Stop or if you\n'
			'would like to take a break, enter break:')

def comment_prompt():
	print ('\nEnter any comments you like, if you don\'t to then just hit enter')
