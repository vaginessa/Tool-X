#Tool Name :- Tool-X v2.0 
# Author :- Rajkumar Dusad
# Date :- 1/11/2017
# Aex Software's :- Tool-X is a automatic tool installer. Specially made for termux and GNURoot Debian terminal.

import os
import sys
from time import sleep
from core.system import *
from logo import *
from cat1 import cat1
from cat2 import cat2
from cat3 import cat3
from cat4 import cat4
from cat5 import cat5
from cat6 import cat6
from cat7 import cat7
from cat8 import cat8
from cat9 import cat9
from cat10 import cat10
from cat11 import cat11
from cat12 import cat12

def cate():
	os.system("clear")
	cat_logo()
	Toolo = raw_input("\n\033[1;33m >>>  \033[1;m")
	if Toolo == "1":
		cat1()
		cate()
	elif Toolo == "2":
		cat2()
		cate()
	elif Toolo == "3":
		cat3()
		cate()
	elif Toolo == "4":
		cat4()
		cate()
	elif Toolo == "5":
		cat5()
		cate()
	elif Toolo == "6":
		cat6()
		cate()
	elif Toolo == "7":
		cat7()
		cate()
	elif Toolo == "8":
		cat8()
		cate()
	elif Toolo == "9":
		cat9()
		cate()
	elif Toolo == "10":
		cat10()
		cate()
	elif Toolo == "11":
		cat11()
		cate()
	elif Toolo == "12":
		cat12()
		cate()
	elif Toolo == "00":
		pass
	else:
		print ("\033[01;34m\007\n error : \033[01;37m\'"+Toolo+"\' \033[01;31minvalid option !!!")
		sleep(1)
		cate()