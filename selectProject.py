# ===========================================================================
# +++selectProject.py+++|
# ______________________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

import sqlite3 as lite

# ***************************************************************************
# |Display Exisiting Projects|
#
# -The purose of this method is to dispay all existing projects in the
# database.
#
# Variables Passed in:
#                     -Cursor to Database
# ***************************************************************************
def display_existing_projects(cur):
	cur.execute("SELECT Project FROM list_of_projects")
	for row in cur:
		print "--> ", row[0]

# ***************************************************************************
# |Check Exisiting Projects|
#
# -The purose of this method is to check all existing projects in the
# database.
#
# Variables Passed in:
#                     -Cursor to Database
#                     -Selected Project
# Returns:
#                     -Boolean
# ***************************************************************************
def check_existing_projects(cur, project_select):
	cur.execute(""" SELECT COUNT(*) FROM 
				list_of_projects WHERE Project = ? """, (project_select, ))
	result = cur.fetchone()
	if result[0]:
		return True
	else:
		return False

# ***************************************************************************
# |Check Worksheet|
#
# -The purose of this method is to check if there is a worksheet for projects
# in the database. If there is not, and the user is trying to create a new
# entry then one is created.
#
# Variables Passed in:
#                     -Cursor to Database
#                     -Boolean
# Returns:
#                     -Boolean
# ***************************************************************************
def check_worksheet(cur, create):
	cur.execute(""" SELECT COUNT(*) FROM 
				sqlite_master WHERE name = ? """, ('projects_worksheet', ))
	result = cur.fetchone()
	if result[0]:
		if create is False:
			return True
	else:
		if create is True:
			cur.execute("""CREATE TABLE projects_worksheet(
						Project VARCHAR(15) NOT NULL PRIMARY KEY, 
						Project_Date DATE, Start_Time TIME, End_Time TIME, 
						Total_Time TIME, Comment TEXT)""")
			return False
