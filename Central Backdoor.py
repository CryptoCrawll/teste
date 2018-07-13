#!/usr/bin/python
# -*- coding:utf-8 -*-

############################################# LIBRARY ########################################

import os, time, sys, socket, pty, traceback

######################################### COLOR VARIABLES ####################################

yellow = "\033[1;33m"
normal = "\033[0;1m"
green = "\033[32;1m"
blue = "\033[34;1m"
red = "\033[31;1m"
white = "\033[0m"

######################################### LOGO CODESEC BR ####################################

codesec = """
\033[0m  ██████╗ ██████╗ ██████╗ ███████╗███████╗███████╗ ██████╗    \033[31;1m██████╗ ██████╗ 
\033[0m ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝    \033[31;1m██╔══██╗██╔══██╗
\033[0m ██║     ██║   ██║██║  ██║█████╗  ███████╗█████╗  ██║         \033[31;1m██████╔╝██████╔╝
\033[0m ██║     ██║   ██║██║  ██║██╔══╝  ╚════██║██╔══╝  ██║         \033[31;1m██╔══██╗██╔══██╗
\033[0m ╚██████╗╚██████╔╝██████╔╝███████╗███████║███████╗╚██████╗    \033[31;1m██████╔╝██║  ██║
\033[0m  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝    \033[31;1m╚═════╝ ╚═╝  ╚═╝
"""

######################################## SEPARATION LINE #####################################

line = """

\033[0;1m   **************************************************************************
"""

################################## FUNTION CLEAR, LOGO, LINE #################################

def cll():

	os.system("clear")
	print codesec + line

######################################## FUNTION EXIT ########################################

def exit_script():
	
	cll()
	print(red + "    [-] Exiting the software ...\n" + normal)
	time.sleep(2)
	os.system("clear")
	exit()

######################################## FUNTION MENU ########################################

def menu():

	cll()
	options = """
    [!] 1. Open new session
    [!] 2. List sessions 
    [!] 3. Connect to session
    [!] 4. Exit
	"""
	answer = True
	while answer:
	    print options
	    answer = raw_input(red + "    [+] Choice: " + white)
	    if answer == "1":
	    	new_session()
	    elif answer == "2":
	    	list_session()
	    elif answer=="3":
	    	connect_session()
	    elif answer=="4":
	    	exit_script()
	    else:
	    	print(red + "\n    [-] Not Valid Choice, Try again!" + normal)
	    	time.sleep(2)
	    	os.system("clear")
	    	cll()

##################################### FUNTION NEW SESSION ####################################

def new_session():

	print("\n    [!] Open new session\n")
	exit()

##################################### FUNTION LIST SESSION ###################################

def list_session():

	print("\n    [!] List sessions\n")
	exit()

################################### FUNTION CONNECT SESSION ##################################

def connect_session():	

	print("\n    [!] Trying Connect to session\n")

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		s.bind(("0.0.0.0", 789))
		s.listen(5)
		s.accept()

		pty.spawn('/bin/bash')
		#print("\n    [+] Session connected!\n")	

	except Exception as erro:
		print("\n    [-] Failed Connection!\n")

######################################## FUNTION MAIN ########################################

def main():

	cll()
	menu()

##################################### STARTING A SCRIPT ######################################

try:

	main()

except KeyboardInterrupt:

	exit_script()