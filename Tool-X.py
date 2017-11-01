#Tool Name :- Tool-X v1.0 
# Date :- 1/11/2017
# Developed by :- Rajkumar Dusad

import os
import sys, traceback

def main():
	try:
		
		def inicio1():
			while True:
				os.system("clear")
				print ('''

\033[1;36m_________________________________________________
=================================================
_________________________________________________
\033[1;m
\033[1;33m
          _____           _     __  __
         |_   _|__   ___ | |    \ \/ /
           | |/ _ \ / _ \| |_____\  /
           | | (_) | (_) | |_____/  \     
           |_|\___/ \___/|_|    /_/\_\ \033[1;m\033[1;91mv1.0\033[1;m

\033[1;36m
_________________________________________________\033[1;m

            \033[1;33mInstall Best Hacking Tool \033[1;m
\033[1;36m_________________________________________________\033[1;m

\033[1;36m
  [ 0 ] Install all tools\033[1;33m [\033[1;m \033[1;91mTotal 50 tools\033[1;m \033[1;33m ]\033[1;m \033[1;36m
  [ 1 ] Sow all tools\033[1;33m [\033[1;m \033[1;91mAlmost 50 tools\033[1;m \033[1;33m ]\033[1;m \033[1;36m
  [ 2 ] About us\033[1;m
\033[1;32m  [ control+c ] Exit \033[1;m

\033[1;36m_________________________________________________
=================================================\033[1;m
			''')

				opcion0 = raw_input('''\033[1;36m
 ##> \033[1;m''')
			
				while opcion0 == "1":
					print ('''

\033[1;36m
_________________________________________________
=================================================\033[1;m

                \033[1;32mSelect your tool \033[1;m
\033[1;36m_________________________________________________
=================================================\033[1;m


\033[1;33m

   1.  Install Tor
   2.  Install Hydra
   3.  Install SQLMap
   4.  Install Metasploit
   5.  Install ngrok
   6.  Install Kali Nethunter
   7.  Install angryFuzzer
   8.  Install Red_Hawk
   9.  Install Weeman
  10.  Install IPGeoLocation
  11.  Install Cupp
  12.  Instagram Bruteforcer (instahack)
  13.  Twitter Bruteforcer   (TwitterSniper)
  14.  Install Ubuntu
  15.  Install Fedora
  16.  Install viSQL
  17.  Install Hash-Buster
  18.  Install D-TECT
  19.  Install Routersploit
  20.  Install Clang
  21.  Install Python
  22.  Install Python2
  23.  Install Python3
  24.  Install PHP
  25.  Install Wifite
  26.  Install Recon-ng
  27.  Install Admin-Panel-Finder
  28.  Install Hunner
  29.  Install Infoga
  30.  Install Hakku Framework
  31.  Install Hammer
  32.  Install Breacher
  33.  Install CredMap
  34.  Install Nmap
  35.  Install Airgeddon
  36.  Install Commix
  37.  Install Webpwn3r
  38.  Install Recon-dog
  39.  Install CPScan
  40.  Install Pybelt
  41.  Install Torshammer
  42.  Install Gloom
  43.  Install Lazysqlmap
  44.  Install OniOff
  45.  Install SCANNER-INURLBR
  46.  Install Ruby
  47.  Install Wfdroid
  48.  Install XPL-SEARCH
  49.  Install Sudo
  50.  Install w3m
\033[1;m

\033[1;36m     
_________________________________________________
=================================================
\033[1;32m  00) Back\033[1;m
\033[1;36m_________________________________________________
=================================================\033[1;m

					''')
					repo = raw_input("\033[1;33m =>  \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-get update")
						cmd2 = os.system("pkg install nano")
						print ("\033[1;32m Nano installed succesfully !!!\033[1;m")
					elif repo == "2":
						cmd3 = os.system("apt-get update -m")
					elif repo == "00":
						inicio1()
					elif repo == "00":
						inicio1()

					else:
						print ("\033[1;31mSorry, Invalid command !!!\033[1;m")
			
				while opcion0 == "0":
					print ('''
\033[1;33m
_________________________________________________
=================================================

     [ + ] This can take long time....
     [ + ] So please put down your phone...

_________________________________________________
=================================================\033[1;m
					''')
					repo = raw_input("\033[1;36mDo you want to install all Tools ? [y/n] => \033[1;m")
					if repo == "n":
						inicio1()
					elif repo == "n":
						inicio1()
					elif repo == "y":
						cmd1 = os.system("chmod +x all.sh")
						cmd1 = os.system("./all.sh")
						print ("\033[1;31m\nAll Tools installed !!!\n\033[1;m")

					else:
						print ("\033[1;31mSorry, invalid command !!!\033[1;m")
			
				while opcion0 == "2":
					os.system("clear")
					print ('''

\033[1;36m_________________________________________________
=================================================
\033[1;m
\033[1;33m
         _____           _     __  __
        |_   _|__   ___ | |    \ \/ /
          | |/ _ \ / _ \| |_____\  /
          | | (_) | (_) | |_____/  \     
          |_|\___/ \___/|_|    /_/\_\ \033[1;m\033[1;91mv1.0\033[1;m

 \033[1;32m
       [ + ] Tool Name :- Tool-X
       [ + ] Developer Name :- Rajkumar Dusad
       [ + ] Developing Date :- 1/11/2017\033[1;m
\033[1;36m     
_________________________________________________
  00 ) back
=================================================\033[1;m
					''')
					repo = raw_input("\033[1;36m => \033[1;m")
					if repo == "00":
						inicio1()
					elif repo == "00":
						inicio1()

					else:
						print ("\033[1;31mSorry, invalid command !!!\033[1;m")


				def inicio():





						inicio()
		inicio1()
	except KeyboardInterrupt:
		print ('''

\033[1;32m Thanks for using Tool-X ...... \033[1;m

''')
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
