# Tool Name :- Tool-X v2.0
# Author :- Rajkumar Dusad
# Date :- 9/10/2018
# Aex Software's :- Tool-X is a automatic tool installer. Specially made for termux and GNURoot Debian terminal.

import os
import sys
from logo import *
from core.system import *
from time import sleep

def t_log():
  ux()
  tos_logo()
  print("")
  b_logo()
  print("")

def tos():
	t_log()
	Toolo = raw_input("\033[1;33m >>>  \033[1;m")
	if Toolo == "1":
		os.system("cd .tools && python2 .T1.aex")
		tos()
	elif Toolo == "2":
		os.system("cd .tools && python2 .T2.aex")
		tos()
	elif Toolo == "3":
		os.system("cd .tools && python2 .T3.aex")
		tos()
	elif Toolo == "4":
		os.system("cd .tools && python2 .T4.aex")
		tos()
	elif Toolo == "5":
		os.system("cd .tools && python2 .T5.aex")
		tos()
		
	elif Toolo == "00":
		pass
	else:
		print ("\033[01;34m\007\n error : \033[01;37m\'"+Toolo+"\' \033[01;31minvalid option !!!")
		sleep(1)
		tos()
