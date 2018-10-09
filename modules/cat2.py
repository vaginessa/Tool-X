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

def cat2():
	os.system("clear")
	cat2_logo()

	Toolo = raw_input("\n\033[1;33m >>>  \033[1;m")
	if Toolo == "1":
		usr=open(".tools/uip.aex","w")
		usr.write("33")
		usr.close()
		inst1()
	elif Toolo == "2":
		usr=open(".tools/uip.aex","w")
		usr.write("43")
		usr.close()
		inst()
	elif Toolo == "3":
		usr=open(".tools/uip.aex","w")
		usr.write("68")
		usr.close()
		inst()
	elif Toolo == "4":
		usr=open(".tools/uip.aex","w")
		usr.write("131")
		usr.close()
		inst()
	elif Toolo == "5":
		usr=open(".tools/uip.aex","w")
		usr.write("107")
		usr.close()
		inst()
	elif Toolo == "6":
		usr=open(".tools/uip.aex","w")
		usr.write("48")
		usr.close()
		inst()
	elif Toolo == "7":
		usr=open(".tools/uip.aex","w")
		usr.write("137")
		usr.close()
		inst()
	elif Toolo == "8":
		usr=open(".tools/uip.aex","w")
		usr.write("117")
		usr.close()
		inst()
	elif Toolo == "9":
		usr=open(".tools/uip.aex","w")
		usr.write("138")
		usr.close()
		inst()
	elif Toolo == "10":
		usr=open(".tools/uip.aex","w")
		usr.write("139")
		usr.close()
		inst()
	elif Toolo == "11":
		usr=open(".tools/uip.aex","w")
		usr.write("140")
		usr.close()
		inst()
	elif Toolo == "12":
		usr=open(".tools/uip.aex","w")
		usr.write("44")
		usr.close()
		inst()
	elif Toolo == "13":
		usr=open(".tools/uip.aex","w")
		usr.write("141")
		usr.close()
		inst()
	elif Toolo == "14":
		usr=open(".tools/uip.aex","w")
		usr.write("142")
		usr.close()
		inst()
	elif Toolo == "15":
		usr=open(".tools/uip.aex","w")
		usr.write("143")
		usr.close()
		inst()
	elif Toolo == "16":
		usr=open(".tools/uip.aex","w")
		usr.write("95")
		usr.close()
		inst()
	elif Toolo == "00":
		pass
	else:
		print ("\033[01;34m\007\n error : \033[01;37m\'"+Toolo+"\' \033[01;31minvalid option !!!")
		sleep(1)
		cat2()
