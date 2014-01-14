# ===========================================================================
# +++createProject.py+++|
# ______________________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

import sqlite3 as lite

# ***************************************************************************
# |List of Projects|
#
# -The purose of this method is to check if a table that lists all the 
# different user projects exists. If not then one is created. In both
# circumstances, the project name and description is inserted into the table.
#
# Variables Passed in:
#                     -Cursor to Database
#                     -Project Name
#                     -Project Definition
# ***************************************************************************

def list_of_projects(cur, name, definition):
	inputs = (name, definition)
	try:
		cur.execute(""" SELECT COUNT(*) FROM 
					sqlite_master WHERE name = 'list_of_projects' """)
		result = cur.fetchone()
		if result[0]:
			cur.execute(""" SELECT COUNT(*) FROM 
						 list_of_projects WHERE Project = ? """, (name, ))
			result = cur.fetchone()
			if result[0]:
				print ('Project exists already!\n'+
						'Please either create a new project or '+
						'open the existing project.\n')
			else:
				print 'Creating project!\n'
				cur.execute("INSERT INTO list_of_projects VALUES(?, ?)", inputs)
		else:
			cur.execute("""CREATE TABLE list_of_projects(
						Project VARCHAR(15) NOT NULL PRIMARY KEY, 
						Description TEXT)""")
			cur.execute("INSERT INTO list_of_projects VALUES(?, ?)", inputs)
	except:
		print 'There was an error processing your command\n'
