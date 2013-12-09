project_tracker
===============
-----------------------------Description-----------------------------------

The purpose of this project is to create a multi-functional project tracker

===========================Timer Functions=================================

* Time is recorded in hours and minutes

* Create New Project:

		Initializes Project----->	Allows user to input a name and description
									of the project

		Creates File------------>	Uses the name the user inputted to create
									projectName.txt

		Sets Current Project---->	The intialized project is set to current
									working project

		Add as Existing Project->	Adds the initialized project to a list of
									existing projects

* Select Existing Project:

		Display projects-------->	Allows user to select an existing project

		Sets Current Project---->	The selected project is set to current
									working project

* Start Timer:

		Get Date and Time------->	Retrieves current date and time

		Existing Entry Check---->	If entry exists for current date for current
									project, timer is resumed

		Create New Timer-------->	If existing entry is false, a new timer is 
									created and started

* Start Break:

		Pause Project Timer----->	Project Timer is stopped

		Create New Timer-------->	Allows user to input a name for the break
									and creates a new timer

* End Break:

		Stop Project Timer------>	Stops current project timer, read 'Stop
									Project Timer' below

		Resume Project Timer---->	Resumes current project timer

		Record Break------------>	Records break to current project file

* Stop Project Timer:

		Stop Project Timer------>	Allows user to comment and stops current
									project timer

		Record Project Timer---->	Records Time to file of current project

* Finished Project:

		Remove Project---------->	Removes current project from existing
									projects

		Add Finished Project---->	Adds current project to finished project
									list and allows user to comment

* Review Existing and Finished Projects:

		Displays Overview------->	Displays projects broken up by whether
									they are finished or exisiting, and
									shows total time

		Select Project---------->	Allows user to select a finished or
									existing project and shows the time,
									length (1 week, month, etc.), and the
									comments associated with that project

		Edit Project------------>	Allows user to edit the selected project
									comments. If it is a finished project,
									allows user to change it to a existing
									project
