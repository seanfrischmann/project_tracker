# ===========================================================================
# +++selectProject.py+++|
# ______________________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

import sqlite3 as lite
import errors

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

# ***************************************************************************
# |Check Exisiting Projects|
#
# -The purose of this method is to check all existing projects in the
# database.
#
# Variables Passed in:
#                     -Cursor to Database
#                     -Selected Project
# ***************************************************************************
def check_existing_projects(cur, project_select):
	cur.execute(""" SELECT COUNT(*) FROM 
				list_of_projects WHERE Project = ? """, (project_select, ))
	result = cur.fetchone()
	if not result[0]:
		raise errors.myError(project_select+' does not exist!')
