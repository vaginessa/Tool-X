# Tool Name :- Tool-X v2.0
# Author :- Rajkumar Dusad
# Date :- 1/10/2018
# Aex Software's :- Tool-X is a automatic tool installer. Specially made for termux and GNURoot Debian terminal.

import os
import sys
from core.system import *

def all_logo():
  if system=="termux":
    hader()
    print ('''
\033[1;33m  [ 1 ] \033[1;32mInstall all tools.\033[1;33m [ \033[1;91mTotal 240 tools\033[1;33m ]
\033[1;33m  [ 0 ] \033[1;32mFor Back.\033[00m''')
    footer()
  else:
    hader()
    print ('''
\033[1;33m   [ 1 ] \033[1;32mInstall all tools.\033[1;33m [ \033[1;91mTotal 240 tools\033[1;33m ]
\033[1;33m   [ 0 ] \033[1;32mFor Back.\033[00m''')
    footer()

def as_logo():
  if system=="termux":
    hader()
    print ('''
 \033[1;33m      [ + ] \033[1;32mAll Tools Installed Successfully.
 \033[1;33m      [ + ] \033[1;32mPress any key to continue.\033[00m''')
    footer()
  else:
    hader()
    print ('''
 \033[1;33m      [ + ] \033[1;32mAll Tools Installed Successfully.
 \033[1;33m      [ + ] \033[1;32mPress any key to continue.\033[00m''')
    footer()

def up_logo():
  if system=="termux":
    hader()
    print ('''
\033[1;33m  [ 1 ] \033[1;32mUpdate your Tool-X.
\033[1;33m  [ 0 ] \033[1;32mFor Back.\033[00m''')
    footer()
  else:
    hader()
    print ('''
\033[1;33m   [ 1 ] \033[1;32mUpdate your Tool-X.
\033[1;33m   [ 0 ] \033[1;32mFor Back.\033[00m''')
    footer()

def ups_logo():
  if system=="termux":
    hader()
    print ('''
\033[1;33m      [ + ] \033[1;32mTool-X Updated Successfully.
\033[1;33m      [ + ] \033[1;32mPress Enter to continue.\033[00m''')
    footer()
  else:
    hader()
    print ('''
\033[1;33m      [ + ] \033[1;32mTool-X Updated Successfully.
\033[1;33m      [ + ] \033[1;32mPress Enter to continue.\033[00m''')
    footer()


def unrr():
  if system=="termux":
    hader()
    print ('''
\033[1;31m  [ + ]  \033[1;31mWe can't Update Tool-X.\033[1;m
\033[1;31m  [ + ]  \033[1;31mAre you offline?\033[1;m
\033[1;31m  [ + ]  \033[1;31mIf you are online.\033[1;m
\033[1;31m  [ + ]  \033[1;31mThen the server is down.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[00m''')
    footer()
  else:
    hader()
    print ('''
\033[1;31m  [ + ]  \033[1;31mWe can't Update Tool-X.\033[1;m
\033[1;31m  [ + ]  \033[1;31mAre you offline?\033[1;m
\033[1;31m  [ + ]  \033[1;31mIf you are online.\033[1;m
\033[1;31m  [ + ]  \033[1;31mThen the server is down.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[00m''')
    footer()


def a_logo():
  if system=="termux":
    hader()
    print ('''
\033[1;33m       [+] Tool Name :- \033[1;32mTool-X
\033[1;33m       [+] Author :- \033[1;32mRajkumar Dusad
\033[1;33m       [+] Powered By :- \033[1;32mAex Software's.\033[1;m
\033[1;33m       [+] Latest Update :- \033[1;32m16/11/2018.\033[1;m

\033[1;33m [+] \033[1;32mTool-x is automatic tool installer.
\033[1;33m [+] \033[1;32mMade for termux and GNURool Debian Terminal.
\033[1;33m [+] \033[1;32mIn the tool-x almost 240 tools available.
\033[1;31m [+] Note :- Use this tool at your own risk.''')
    footer()
  else:
    hader()
    print ('''
\033[1;33m              [+] Tool Name :- \033[1;32mTool-X
\033[1;33m              [+] Author :- \033[1;32mRajkumar Dusad
\033[1;33m              [+] Powered By :- \033[1;32mAex Software's.\033[1;m
\033[1;33m              [+] Latest Update :- \033[1;32m16/11/2018.\033[1;m

\033[1;33m   [+] \033[1;32mTool-x is automatic tool installer.
\033[1;33m   [+] \033[1;32mMade for termux and GNURool Debian Terminal.
\033[1;33m   [+] \033[1;32mIn the tool-x almost 240 tools available.
\033[1;31m   [+] Note :- Use this tool at your own risk.''')
    footer()

def cat_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] Information Gathering.
  [ 2 ] Vulnerability Scanner.
  [ 3 ] Stress Testing.
  [ 4 ] Password Attacks.
  [ 5 ] Web Hacking.
  [ 6 ] Exploitation Tools.
  [ 7 ] Sniffing & Spoofing.
  [ 8 ] Wireless Testing.
  [ 9 ] IP-Tracking tools.
  [ 10 ] Programming Languages.
  [ 11 ] DDOS Attacks.
  [ 12 ] Web Server's.\033[00m
""")
  b_logo()

def cat1_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] Nmap
  [ 2 ] Red Hawk
  [ 3 ] D-Tect
  [ 4 ] sqlmap
  [ 5 ] Infoga
  [ 6 ] ReconDog
  [ 7 ] sqlmate
  [ 8 ] Crips
  [ 9 ] EvilURL
  [ 10 ] OSIF
  [ 11 ] Devploit
  [ 12 ] Setoolkit
  [ 13 ] WPScan
  [ 14 ] CMSmap
  [ 15 ] XSStrike
  [ 16 ] Doork
""")
  b_logo()

def cat2_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] Nmap
  [ 2 ] Red Hawk
  [ 3 ] D-Tect
  [ 4 ] Damn Small SQLi Scanner
  [ 5 ] SQLiv
  [ 6 ] sqlmap
  [ 7 ] sqlscan
  [ 8 ] WPScan
  [ 9 ] sqlmate
  [ 10 ] Rang3r
  [ 11 ] Striker
  [ 12 ] Routersploit
  [ 13 ] Xshell
  [ 14 ] SH33LL
  [ 15 ] BlackBox
  [ 16 ] XAttacker\033[00m
""")
  b_logo()

def cat3_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] Torshammer
  [ 2 ] Slowloris
  [ 3 ] GoldenEye
  [ 4 ] Xerxes
  [ 5 ] Planetwork-DDOS
  [ 6 ] Hydra
  [ 7 ] santet-online\033[00m
""")
  b_logo()

def cat4_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] Hydra
  [ 2 ] Hash Buster
  [ 3 ] Cupp
  [ 4 ] InstaHack
  [ 5 ] Social-Engineering
  [ 6 ] Hashzer
  [ 7 ] Hasher
  [ 8 ] Hash-Generator
  [ 9 ] Hasherdotid\033[00m
""")
  b_logo()

def cat5_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] sqlmap
  [ 2 ] Webdav
  [ 3 ] sqlmate
  [ 4 ] Xshell
  [ 5 ] SH33LL
  [ 6 ] XAttacker
  [ 7 ] XSStrike
  [ 8 ] Breacher
  [ 9 ] Doork
  [ 10 ] Inurlbr
  [ 11 ] BruteX\033[00m
""")
  b_logo()

def cat6_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] Metasploit
  [ 2 ] commix
  [ 3 ] sqlmap
  [ 4 ] Brutal
  [ 5 ] A-Rat
  [ 6 ] Websploit
  [ 7 ] Routersploit
  [ 8 ] BlackBox
  [ 9 ] XAttacker
  [ 10 ] TXTool
  [ 11 ] ATSCAN
  [ 12 ] Shellnoob\033[00m
""")
  b_logo()


def cat7_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] KnockMail
  [ 2 ] Spammer-Grab
  [ 3 ] Spammer-Email
  [ 4 ] SocialFish
  [ 5 ] santet-online
  [ 6 ] SEToolkit
  [ 7 ] SSLtrip
  [ 8 ] pyPISHER\033[00m
""")
  b_logo()

def cat8_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] aircrack-ng
  [ 2 ] wifite
  [ 3 ] Fluxion
  [ 4 ] Wifresti
  [ 5 ] WiFi-Pumpkin
  [ 6 ] WifiBruteCrack
  [ 7 ] wirespy
  [ 8 ] wifi-hacker
  [ 9 ] airgeddon
  [ 10 ] reaver\033[00m
""")
  b_logo()

def cat9_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] IP-Tracer
  [ 2 ] IP GeoLocation
  [ 3 ] IP Locator
  [ 4 ] TrackOut
  [ 5 ] IP-FY\033[00m
""")
  b_logo()

def cat10_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] Python
  [ 2 ] C
  [ 3 ] C++
  [ 4 ] Perl
  [ 5 ] Ruby
  [ 6 ] Golang
  [ 7 ] PHP
  [ 8 ] node js
\033[00m""")
  b_logo()

def cat11_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] Xerxes
  [ 2 ] Hulk
  [ 3 ] Hammer
  [ 4 ] Slowloris
  [ 5 ] Torshamer\033[00m
""")
  b_logo()

def cat12_logo():
  hader()
  print ("""\033[01;32m
  [ 1 ] MyServer
  [ 2 ] Apache
  [ 3 ] Alien Host
  [ 4 ] Nginx\033[00m
""")
  b_logo()



def in_logo():
  if system=="termux":
    print ("""\033[01;33m ===============================================
\033[01;32m|______________ Select your tool _______________|
 \033[01;33m===============================================\033[00m""")
  else:
    print ("""\033[01;33m =========================================================
\033[01;32m|____________________ Install Any Tool ___________________|
 \033[01;33m=========================================================\033[00m""")

def b_logo():
  if system=="termux":
    print ("""\033[01;36m ===============================================
\033[01;33m|  00) Back                                     |
 \033[01;36m===============================================\033[00m""")
  else:
    print ("""\033[01;36m =========================================================
\033[01;33m|   00) Back                                              |
 \033[01;36m=========================================================\033[00m""")

def upp_logo():
  if system=="termux":
    print ("""\033[01;33m ===============================================
\033[01;32m|_______________ Updating Tool-X _______________|
 \033[01;33m===============================================\033[00m""")
  else:
    print ("""\033[01;33m =========================================================
\033[01;32m|____________________ Updating Tool-X ____________________|
 \033[01;33m=========================================================\033[00m""")

def ins_logo():
  if system=="termux":
    print ("""\033[01;33m ===============================================
\033[01;32m|_________________ Installing __________________|
 \033[01;33m===============================================\033[00m""")
  else:
    print ("""\033[01;33m =========================================================
\033[01;32m|_______________________ Installing ______________________|
 \033[01;33m=========================================================\033[00m""")

def hader():
  if system=="termux":
    print ('''\007


\033[1;33m
          _____           _    __  __
         |_   _|__   ___ | |   \ \/ /
           | |/ _ \ / _ \| |____\  /
           | | (_) | (_) | |____/  \     
           |_|\___/ \___/|_|   /_/\_\ \033[1;91mv2.0


\033[1;36m ===============================================\033[1;m
\033[1;33m|           Install Best Hacking Tool           |
\033[1;36m ===============================================\033[00m''')
  else:
    print ('''\007


\033[1;33m
               _____           _    __  __
              |_   _|__   ___ | |   \ \/ /
                | |/ _ \ / _ \| |____\  /
                | | (_) | (_) | |____/  \     
                |_|\___/ \___/|_|   /_/\_\ \033[1;31mv2.0
\033[1;m

\033[1;36m =========================================================\033[1;m
\033[1;33m|\033[1;m               \033[1;33m Install Best Hacking Tool.\033[1;m               \033[1;33m|\033[1;m
\033[1;36m =========================================================\033[00m''')


def footer():
  if system=="termux":
    print ('''\033[1;36m_________________________________________________
=================================================\033[00m''')
  else:
    print ('''\033[1;36m___________________________________________________________
===========================================================\033[00m''')

def menu():
  if system=="termux":
    hader()
    print ('''
\033[1;33m  [ 0 ] \033[1;32mInstall all tools.\033[1;33m [ \033[1;91mTotal 240 tools\033[1;33m ]
\033[1;33m  [ 1 ] \033[1;32mShow all tools.\033[1;33m [ \033[1;91mAlmost 240 tools\033[1;33m ]
\033[1;33m  [ 2 ] \033[1;32mTools Category.
\033[1;33m  [ 3 ] \033[1;32mTermux OS.
\033[1;33m  [ 4 ] \033[1;32mUpdate Tool-X.
\033[1;33m  [ 5 ] \033[1;32mAbout Us.
\033[1;33m  [ x ] \033[1;32mFor Exit.''')
    footer()
  else:
    hader()
    print ('''
\033[1;33m   [ 0 ] \033[1;32mInstall all tools.\033[1;33m [ \033[1;91mTotal 240 tools\033[1;33m ]
\033[1;33m   [ 1 ] \033[1;32mShow all tools.\033[1;33m [ \033[1;91mAlmost 240 tools\033[1;33m ]
\033[1;33m   [ 2 ] \033[1;32mTools Category.
\033[1;33m   [ 3 ] \033[1;32mUpdate Tool-X.
\033[1;33m   [ 4 ] \033[1;32mAbout Us.
\033[1;33m   [ x ] \033[1;32mFor Exit.''')
    footer()

def tos_logo():
  hader()
  print ('''\033[01;32m
  [ 1 ] Install Arch Linux
  [ 2 ] Install Alpine Linux
  [ 3 ] Install Kali-Nethunter(Kali Linux)
  [ 4 ] Install Fedora
  [ 5 ] Install Ubuntu\033[00m''')

def elogo():
  if system=="termux":
    hader()
    print ('''
\033[1;33m         [ + ] \033[1;32mThanks for using Tool-X 
\033[1;33m         [ + ] \033[1;32mGood By..... :)\033[00m
''')
    footer()
  else:
    hader()
    print ('''
\033[1;33m         [ + ] \033[1;32mThanks for using Tool-X 
\033[1;33m         [ + ] \033[1;32mGood By..... :)\033[00m
''')
    footer()

def exit():
  ux()
  elogo()
  sleep(0.5)
  ex()
