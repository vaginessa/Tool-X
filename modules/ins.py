# Tool Name :- Tool-X v2.0
# Author :- Rajkumar Dusad
# Date :- 1/11/2017
# Aex Software's :- Tool-X is a automatic tool installer. Specially made for termux and GNURoot Debian terminal.

import os
import sys
from logo import *
from core.system import *
from time import sleep

def show():
  #search=raw_input(" Tool name :")

  for userinput in range(1,241):
    if os.path.exists(".tools/%d.aex"%userinput):
      opn=open(".tools/%d.aex"%userinput,"r")
      red=opn.read()
      opn.close()
      n=len(red)

      # ------------------------- Getting Tool name
      for i in range(0,n):
        if red[i]=="#" or red[i] != "{":
          if red[i]!="#" and red[i]!=" ":
            tmp=open("toolname.txt","a")
            tmp.write(red[i])
            tmp.close()
        else:
          break
      if os.path.exists("toolname.txt"):
        tn=open("toolname.txt","r")
        toolname=tn.read()
        tn.close()
        os.system("rm toolname.txt")

      if toolname=="Null":
        pass
      else:
        print ("  \033[01;32m[ \033[01;37m%d \033[01;32m] \033[01;33mInstall \033[01;32m%s"%(userinput,toolname))

def intool():
  ux()
  in_logo()
  print("\007")
  show()
  print("")
  b_logo()
  print("")

def inst1():
	os.system("cd .tools && python2 .inst1.aex")
	tmn()
def inst():
	os.system("cd .tools && python2 .inst.aex")
	tmn()

def tmn():
	os.system("clear")
	intool()
	Toolo = raw_input("\033[1;33m >>>  \033[1;m")
	usr=open(".tools/uip.aex","w")
	usr.write(Toolo)
	usr.close()
	if Toolo == "1":
		inst()
	elif Toolo == "2":
		inst()
	elif Toolo == "3":
		inst1()
	elif Toolo == "4":
		inst()
	elif Toolo == "5":
		inst()
	elif Toolo == "6":
		inst()
	elif Toolo == "7":
		inst()
	elif Toolo == "8":
		inst()
	elif Toolo == "9":
		inst()
	elif Toolo == "10":
		inst()
	elif Toolo == "11":
		inst1()
	elif Toolo == "12":
		inst()
	elif Toolo == "13":
		inst()
	elif Toolo == "14":
		inst1()
	elif Toolo == "15":
		inst1()
	elif Toolo == "16":
		inst1()
	elif Toolo == "17":
		inst()
	elif Toolo == "18":
		inst()
	elif Toolo == "19":
		inst()
	elif Toolo == "20":
		inst1()
	elif Toolo == "21":
		inst()
	elif Toolo == "22":
		inst()
	elif Toolo == "23":
		inst()
	elif Toolo == "24":
		inst1()
	elif Toolo == "25":
		inst()
	elif Toolo == "26":
		inst()
	elif Toolo == "27":
		inst()
	elif Toolo == "28":
		inst()
	elif Toolo == "29":
		inst()
	elif Toolo == "30":
		inst1()
	elif Toolo == "31":
		inst()
	elif Toolo == "32":
		inst()
	elif Toolo == "33":
		inst1()
	elif Toolo == "34":
		inst()
	elif Toolo == "35":
		inst()
	elif Toolo == "36":
		inst()
	elif Toolo == "37":
		inst1()
	elif Toolo == "38":
		inst1()
	elif Toolo == "39":
		inst()
	elif Toolo == "40":
		inst()
	elif Toolo == "41":
		inst()
	elif Toolo == "42":
		inst()
	elif Toolo == "43":
		inst()
	elif Toolo == "44":
		inst()
	elif Toolo == "45":
		inst1()
	elif Toolo == "46":
		inst()
	elif Toolo == "47":
		inst()
	elif Toolo == "48":
		inst()
	elif Toolo == "49":
		inst()
	elif Toolo == "50":
		inst()
	elif Toolo == "51":
		inst()
	elif Toolo == "52":
		inst1()
	elif Toolo == "53":
		inst1()
	elif Toolo == "54":
		inst()
	elif Toolo == "55":
		inst()
	elif Toolo == "56":
		inst()
	elif Toolo == "57":
		inst()
	elif Toolo == "58":
		inst()
	elif Toolo == "59":
		inst()
	elif Toolo == "60":
		inst()
	elif Toolo == "61":
		inst()
	elif Toolo == "62":
		inst()
	elif Toolo == "63":
		inst1()
	elif Toolo == "64":
		inst()
	elif Toolo == "65":
		inst()
	elif Toolo == "66":
		inst()
	elif Toolo == "67":
		inst()
	elif Toolo == "68":
		inst()
	elif Toolo == "69":
		inst()
	elif Toolo == "70":
		inst()
	elif Toolo == "71":
		inst()
	elif Toolo == "72":
		inst()
	elif Toolo == "73":
		inst()
	elif Toolo == "74":
		inst1()
	elif Toolo == "75":
		inst1()
	elif Toolo == "76":
		inst()
	elif Toolo == "77":
		inst()
	elif Toolo == "78":
		inst()
	elif Toolo == "79":
		inst()
	elif Toolo == "80":
		inst()
	elif Toolo == "81":
		inst()
	elif Toolo == "82":
		inst()
	elif Toolo == "83":
		inst()
	elif Toolo == "84":
		inst()
	elif Toolo == "85":
		inst()
	elif Toolo == "86":
		inst()
	elif Toolo == "87":
		inst()
	elif Toolo == "88":
		inst()
	elif Toolo == "89":
		inst()
	elif Toolo == "90":
		inst()
	elif Toolo == "91":
		inst()
	elif Toolo == "92":
		inst()
	elif Toolo == "93":
		inst()
	elif Toolo == "94":
		inst()
	elif Toolo == "95":
		inst()
	elif Toolo == "96":
		inst()
	elif Toolo == "97":
		inst()
	elif Toolo == "98":
		inst()
	elif Toolo == "99":
		inst()
	elif Toolo == "100":
		inst()
	elif Toolo == "101":
		inst()
	elif Toolo == "102":
		inst()
	elif Toolo == "103":
		inst()
	elif Toolo == "104":
		inst()
	elif Toolo == "105":
		inst()
	elif Toolo == "106":
		inst()
	elif Toolo == "107":
		inst()
	elif Toolo == "108":
		inst()
	elif Toolo == "109":
		inst()
	elif Toolo == "110":
		inst()
	elif Toolo == "111":
		inst()
	elif Toolo == "112":
		inst()
	elif Toolo == "113":
		inst()
	elif Toolo == "114":
		inst()
	elif Toolo == "115":
		inst()
	elif Toolo == "116":
		inst()
	elif Toolo == "117":
		inst()
	elif Toolo == "118":
		inst()
	elif Toolo == "119":
		inst()
	elif Toolo == "120":
		inst()
	elif Toolo == "121":
		inst()
	elif Toolo == "122":
		inst()
	elif Toolo == "123":
		inst()
	elif Toolo == "124":
		inst()
	elif Toolo == "125":
		inst()
	elif Toolo == "126":
		inst()
	elif Toolo == "127":
		inst()
	elif Toolo == "128":
		inst()
	elif Toolo == "129":
		inst()
	elif Toolo == "130":
		inst()
	elif Toolo == "131":
		inst()
	elif Toolo == "132":
		inst()
	elif Toolo == "133":
		inst()
	elif Toolo == "134":
		inst()
	elif Toolo == "135":
		inst()
	elif Toolo == "136":
		inst()
	elif Toolo == "137":
		inst()
	elif Toolo == "138":
		inst()
	elif Toolo == "139":
		inst()
	elif Toolo == "140":
		inst()
	elif Toolo == "141":
		inst()
	elif Toolo == "142":
		inst()
	elif Toolo == "143":
		inst()
	elif Toolo == "144":
		inst()
	elif Toolo == "145":
		inst()
	elif Toolo == "146":
		inst()
	elif Toolo == "147":
		inst()
	elif Toolo == "148":
		inst()
	elif Toolo == "149":
		inst()
	elif Toolo == "150":
		inst()
	elif Toolo == "151":
		inst()
	elif Toolo == "152":
		inst()
	elif Toolo == "153":
		inst()
	elif Toolo == "154":
		inst()
	elif Toolo == "155":
		inst()
	elif Toolo == "156":
		inst()
	elif Toolo == "157":
		inst()
	elif Toolo == "158":
		inst()
	elif Toolo == "159":
		inst()
	elif Toolo == "160":
		inst()
	elif Toolo == "161":
		inst1()
	elif Toolo == "162":
		inst1()
	elif Toolo == "163":
		inst1()
	elif Toolo == "164":
		inst()
	elif Toolo == "165":
		inst()
	elif Toolo == "166":
		inst()
	elif Toolo == "167":
		inst()
	elif Toolo == "168":
		inst()
	elif Toolo == "169":
		inst()
	elif Toolo == "170":
		inst()
	elif Toolo == "171":
		inst()
	elif Toolo == "172":
		inst()
	elif Toolo == "173":
		inst()
	elif Toolo == "174":
		inst()
	elif Toolo == "175":
		inst()
	elif Toolo == "176":
		inst()
	elif Toolo == "177":
		inst()
	elif Toolo == "178":
		inst()
	elif Toolo == "179":
		inst()
	elif Toolo == "180":
		inst()
	elif Toolo == "181":
		inst()
	elif Toolo == "182":
		inst()
	elif Toolo == "183":
		inst()
	elif Toolo == "184":
		inst()
	elif Toolo == "185":
		inst()
	elif Toolo == "186":
		inst()
	elif Toolo == "187":
		inst()
	elif Toolo == "188":
		inst()
	elif Toolo == "189":
		inst()
	elif Toolo == "190":
		inst()
	elif Toolo == "191":
		inst()
	elif Toolo == "192":
		inst()
	elif Toolo == "193":
		inst()
	elif Toolo == "194":
		inst()
	elif Toolo == "195":
		inst()
	elif Toolo == "196":
		inst()
	elif Toolo == "197":
		inst()
	elif Toolo == "198":
		inst()
	elif Toolo == "199":
		inst()
	elif Toolo == "200":
		inst()
	elif Toolo == "201":
		inst()
	elif Toolo == "202":
		inst()
	elif Toolo == "203":
		inst()
	elif Toolo == "204":
		inst()
	elif Toolo == "205":
		inst()
	elif Toolo == "206":
		inst()
	elif Toolo == "207":
		inst()
	elif Toolo == "208":
		inst()
	elif Toolo == "209":
		inst()
	elif Toolo == "210":
		inst()
	elif Toolo == "211":
		inst()
	elif Toolo == "212":
		inst()
	elif Toolo == "213":
		inst()
	elif Toolo == "214":
		inst()
	elif Toolo == "215":
		inst()
	elif Toolo == "216":
		inst1()
	elif Toolo == "217":
		inst1()
	elif Toolo == "218":
		inst()
	elif Toolo == "219":
		inst()
	elif Toolo == "220":
		inst()
	elif Toolo == "221":
		inst()
	elif Toolo == "222":
		inst()
	elif Toolo == "223":
		inst()
	elif Toolo == "224":
		inst()
	elif Toolo == "225":
		inst()
	elif Toolo == "226":
		inst()
	elif Toolo == "227":
		inst()
	elif Toolo == "228":
		inst()
	elif Toolo == "229":
		inst()
	elif Toolo == "230":
		inst()
	elif Toolo == "231":
		inst()
	elif Toolo == "232":
		inst()
	elif Toolo == "233":
		inst()
	elif Toolo == "234":
		inst()
	elif Toolo == "235":
		inst()
	elif Toolo == "236":
		inst()
	elif Toolo == "237":
		inst()
	elif Toolo == "238":
		inst()
	elif Toolo == "239":
		inst()
	elif Toolo == "240":
		inst()
	elif Toolo == "00" or Toolo=="back":
		pass
	else:
		print ("\033[01;34m\007\n error : \033[01;37m\'"+Toolo+"\' \033[01;31minvalid option !!!")
		sleep(1)
		tmn()
      
