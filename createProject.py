# ===========================================================================
# +++createProject.py+++|
# ______________________|
#
# Sean Frischmann
# Time Tracker
# ===========================================================================

import sqlite3 as lite
import errors
import sys

# ***************************************************************************
# |List of Projects|
#
# -The purose of this method is to check if a table that lists all the 
# different user projects exists. If not then one is created.
#
# Variables Passed in:
#                     -Cursor to Database
# ***************************************************************************

def list_of_projects(cur):
	cur.execute("""CREATE TABLE list_of_projects(
				Project VARCHAR(15) NOT NULL PRIMARY KEY, 
				Description TEXT)""")

# ***************************************************************************
# |Create Project|
#
# -The purose of this method is to check if the given project name exists,
# if not then the project is created.
#
# Variables Passed in:
#                     -Cursor to Database
#                     -Project Name
#                     -Project Definition
# ***************************************************************************
def create_project(cur, name, definition):
	inputs = (name, definition)
	cur.execute(""" SELECT COUNT(*) FROM 
				 list_of_projects WHERE Project = ? """, (name, ))
	result = cur.fetchone()
	if result[0]:
		raise errors.myError(name+' already exists!\n')
	else:
		cur.execute("INSERT INTO list_of_projects VALUES(?, ?)", inputs)

# ***************************************************************************
# |Create Worksheet|
#
# -The purose of this method is to create a worksheet to store information
# relating to the associated project.
#
# Variables Passed in:
#                     -Cursor to Database
# ***************************************************************************
def create_worksheet(cur):
	cur.execute("""CREATE TABLE projects_worksheet(
				Project VARCHAR(15) NOT NULL PRIMARY KEY, 
				Project_Date DATE, Start_Time TIME, End_Time TIME, 
				Total_Time TIME, Comment TEXT)""")
