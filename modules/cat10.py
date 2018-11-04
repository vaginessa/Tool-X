#Tool Name :- Tool-X v2.0 
# Author :- Rajkumar Dusad
# Date :- 1/11/2017
# Aex Software's :- Tool-X is a automatic tool installer. Specially made for termux and GNURoot Debian terminal.

import os
import sys
from time import sleep
from core.system import *
from logo import *

def inst():
	os.system("cd .tools && python2 .inst.aex")

def inst1():
	os.system("cd .tools && python2 .inst1.aex")

def cat10():
	os.system("clear")
	cat10_logo()

	Toolo = raw_input("\n\033[1;33m >>>  \033[1;m")
	if Toolo == "1":
		usr=open(".tools/uip.aex","w")
		usr.write("37")
		usr.close()
		inst1()
	elif Toolo == "2":
		usr=open(".tools/uip.aex","w")
		usr.write("11")
		usr.close()
		inst1()
	elif Toolo == "3":
		usr=open(".tools/uip.aex","w")
		usr.write("11")
		usr.close()
		inst1()
	elif Toolo == "4":
		usr=open(".tools/uip.aex","w")
		usr.write("24")
		usr.close()
		inst1()
	elif Toolo == "5":
		usr=open(".tools/uip.aex","w")
		usr.write("45")
		usr.close()
		inst1()
	elif Toolo == "6":
		usr=open(".tools/uip.aex","w")
		usr.write("161")
		usr.close()
		inst1()
	elif Toolo == "7":
		usr=open(".tools/uip.aex","w")
		usr.write("15")
		usr.close()
		inst1()
	elif Toolo == "8":
		usr=open(".tools/uip.aex","w")
		usr.write("217")
		usr.close()
		inst1()
	elif Toolo == "00":
		pass
	else:
		print ("\033[01;34m\007\n error : \033[01;37m\'"+Toolo+"\' \033[01;31minvalid option !!!")
		sleep(1)
		cat10()
