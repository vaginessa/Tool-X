# Tool Name :- Tool-X v2.0
# Author :- Rajkumar Dusad
# Date :- 1/10/2018
# Aex Software's :- Tool-X is a automatic tool installer. Specially made for termux and GNURoot Debian terminal.

import os
import sys
from time import sleep

if os.path.exists("/usr/bin/yum"):
  if os.path.exists("/usr/lib/sudo"):
    system="fedora"
    home=os.getenv("HOME")+"/"
    bpath="/usr/bin/"
    pack="sudo yum"
  else:
    system="fedora"
    home=os.getenv("HOME")+"/"
    bpath="/usr/bin/"
    pack="yum"

elif os.path.exists("/usr/bin/apt"):
  if os.path.exists("/usr/lib/sudo"):
    system="ubuntu"
    home=os.getenv("HOME")+"/"
    bpath="/usr/bin/"
    pack="sudo apt-get"
  else:
    system="debian"
    home=os.getenv("HOME")+"/"
    bpath="/usr/bin/"
    pack="apt-get"

elif os.path.exists("/usr/bin/apt"):
  if os.path.exists("/usr/bin/sudo"):
    system="ubuntu"
    home=os.getenv("HOME")+"/"
    bpath="/usr/bin/"
    pack="sudo apt-get"
  else:
    system="debian"
    home=os.getenv("HOME")+"/"
    bpath="/usr/bin/"
    pack="apt-get"

elif os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
  system="termux"
  home=os.getenv("HOME")+"/"
  bpath="/data/data/com.termux/files/usr/bin/"
  pack="pkg"

elif os.path.exists("/usr/bin/brew"):
  system="mac"
  home=os.getenv("HOME")+"/"
  bpath="/usr/bin/"
  pack="brew"

elif os.path.exists("/bin/brew"):
  system="mac"
  home=os.getenv("HOME")+"/"
  bpath="/bin/"
  pack="brew"

def ex():
  ex=sys.exit()

def ux():
  ux=os.system("clear")