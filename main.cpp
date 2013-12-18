// ===========================================================================
// +++main.cpp+++|
// ______________|
//
// Sean Frischmann
// Time Tracker
// ===========================================================================

#include <iostream>
#include <map>
#include <stdlib.h>
#include <sstream>
#include <cstdlib>
#include <algorithm>
#include <stdexcept>


typedef void (*cmd_t)();
/**
 * ---------------------------------------------------------------------------
 * prototypes
 * ---------------------------------------------------------------------------
**/

void new_project();		//creates new project
/**
 * ---------------------------------------------------------------------------
 * Main Body
 * ---------------------------------------------------------------------------
**/
int main(){
	std::string line;
	std::map<std::string, cmd_t> cmd_map;
	cmd_map["create"] = &new_project;

	std::string usage_msg = "Time Tracker \n"
		               "Author: Sean Frischmann \n"
					   "Test Simulation \n";
	std::string menu = "Please enter one of the following commands: \n"
		          "create	--> for new project";

	std::cout <<  usage_msg << std::endl;
	std::cout << menu << std::endl;

	std::string cmd;
	while(std::cin){
		std::getline(std::cin, cmd);
		//std::istringstream iss(cmd);
		//iss >> cmd;
		if(cmd == "exit" || cmd == "quit" || cmd == "bye"){
			exit(0);
		}
		if(cmd == ""){
			std::cout << menu << std::endl;
			continue;
		}
		if(cmd_map.find(cmd) != cmd_map.end()){
			try{
				cmd_map[cmd]();
			}catch(std::runtime_error &e){
				std::cerr << "There was an error processing your command"
					<< std::endl;
			}
		}else{
			std::cerr<< menu << std::endl;
		}
	}
	return 0;
}

/**
 * ---------------------------------------------------------------------------
 * Create New Project
 * ---------------------------------------------------------------------------
**/
void new_project(){
	std::cout << "Please enter the name of a project" << std::endl;
}
