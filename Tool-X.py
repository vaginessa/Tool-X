import os

def menu():

    print(""" 

__________________________________________
__________________________________________


      _____           _     __  __
     |_   _|__   ___ | |    \ \/ /
       | |/ _ \ / _ \| |_____\  /
       | | (_) | (_) | |_____/  \     
       |_|\___/ \___/|_|    /_/\_\ v1.0


__________________________________________

        Install Best Hacking Tool
__________________________________________


   1.  Install Nmap 
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
  27.  Install Pybelt
  28.  Install Hunner
  29.  Install Infoga
  30.  Install Hakku Framework
  31.  Install Hammer
  32.  Install Breacher
  33.  Install CredMap
  34.  Install Admin-Panel-Finder
  35.  Install Airgeddon
  36.  Install Commix
  37.  Install Webpwn3r
  38.  Install Recon-dog
  39.  Install CPScan
  40.  Install Tor
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

__________________________________________
99. Exit
==========================================

""")

loop = True

while loop:
    menu()
    what = input("=> ")
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap installed successfully :)")
        print("[+] Type 'nmap' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] hydra installed successfully :)")
        print("[+] Type 'hydra' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap installed successfully :)")
        print("[+] Go to sqlmap folder and type 'python2 sqlmap.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit installed successfully :)")
        print("[+] Type 'msfconsole' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ngrok installed successfully :)")
        print("[+] Go to ngrok folder and type './ngrok http 80' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Nethunter installed successfully :)")
        print("[+] Go to Nethunter-In-Termux folder and type './kalinethunter' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
        os.system("cd /data/data/com.termux/files/home/angryFuzzer && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] angryFuzzer installed successfully :)")
        print("[+] Go to angryFuzzer folder and type 'python2 angryFuzzer.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK installed successfully :)")
        print("[+] Go to RED_HAWK folder and type 'php rhawk.php' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] weeman installed successfully :)")
        print("[+] Go to weeman folder and type 'python2 weeman.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home/IPGeoLocation && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] IPGeoLocation installed successfully :)")
        print("[+] Go to IPGeoLocation folder and type 'python ipgeolocation.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "11":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
        print("====================================")
        print("[+] Cupp installed successfully :)")
        print("[+] Go to cupp folder and type 'python cupp3.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "12":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack installed successfully :)")
        print("[+] Go to instahack folder and type 'python hackinsta.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "13":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pip install mechanicalsoup")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
        print("====================================")
        print("[+] TwitterSniper installed successfully :)")
        print("[+] Go to TwitterSniper folder and type 'python TwitterSniper.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu installed successfully :)")
        print("[+] Go to termux-ubuntu folder and type './start.sh' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "15":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora installed successfully :)")
        print("[+] Type 'sh termux-fedora.sh f26_arm64' or 'sh termux-fedora.sh f26_arm' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
        print("====================================")
        print("[+] viSQL installed successfully :)")
        print("[+] Go to viSQL folder and type 'python2 viSQL.py --help' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "18":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "19":
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("cd /data/data/com.termux/files/home/routersploit && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home/routersploit && pip2 install -r requirements-dev.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requests")
            print("====================================")
            print("[+] routersploit installed successfully :)")
            print("[+] Go to routersploit folder and type 'python2 rsf.py' to start.")
            print("====================================")
            rmenu = input("[?] Back to Menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    elif what == "20":
        os.system("cd")
        os.system("pkg update -y")
        os.system("pkg install -y clang")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Clang installed successfully :)")
        print("[+] Now you can run c,c++ program.")
        print("[+] To write c program type 'nano new.c' and start your program and save it.")
        print("[+] To compile your program type 'clang new.c -o new'.")
        print("[+] To run your program type './new' .")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "21":
        os.system("cd")
        os.system("pkg update -y")
        os.system("pkg install -y python")
        os.system("pkg install -y python-pip")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Python installed successfully :)")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "22":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("pkg install -y python2-pip")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Python2 installed successfully :)")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "23":
        os.system("pkg update -y")
        os.system("pkg install -y python3")
        os.system("pkg install -y python3-pip")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Python3 installed successfully :)")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "24":
        os.system("pkg update -y")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] PHP installed successfully :)")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "25":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y python3-pip")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/derv82/wifite.git")
        os.system("cd /data/data/com.termux/files/home/wifite && chmod +x wifite.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Wifite installed successfully :)")
        print("[+] Go to wifite folder and type 'python2 wifite.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "26":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/jorik041/recon-ng.git")
        os.system("cd /data/data/com.termux/files/home/recon-ng && chmod +x recon-ng.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Recon-ng installed successfully :)")
        print("[+] Go to recon-ng folder and type 'python2 recon-ng.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "27":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Ekultek/Pybelt.git")
        os.system("cd /data/data/com.termux/files/home/Pybelt && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home/Pybelt && chmod +x pybelt.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Pybelt installed successfully :)")
        print("[+] Go to pybelt folder and type 'python2 pybelt.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "28":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/b3-v3r/Hunner.git")
        os.system("cd /data/data/com.termux/files/home/Hunner && chmod +x hunner.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Hunner installed successfully :)")
        print("[+] Go to Hunner folder and type 'python hunner.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "29":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("pkg install -y python2-pip")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/m4ll0k/Infoga.git")
        os.system("cd /data/data/com.termux/files/home/Infoga && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home/Infoga && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home/Infoga && termux-fix-shebang requirements.txt")
        os.system("cd /data/data/com.termux/files/home/Infoga && chmod 777 infoga.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Infoga installed successfully :)")
        print("[+] Go to Infoga folder and type 'python2 infoga.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "30":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/4shadoww/hakkuframework.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Hakku Framework installed successfully :)")
        print("[+] Go to hakkuframework folder and type 'python hakku' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "31":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/cyweb/hammer")
        os.system("cd /data/data/com.termux/files/home/hammer && chmod +x hammer.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Hammer installed successfully :)")
        print("[+] Go to hammer folder and type 'python hammer.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "32":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Breacher.git")
        os.system("cd /data/data/com.termux/files/home/Breacher && chmod +x breacher.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Breacher installed successfully :)")
        print("[+] Go to Breacher folder and type 'python2 breacher.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "33":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/lightos/credmap.git")
        os.system("cd /data/data/com.termux/files/home/credmap && chmod +x credmap.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] CredMap installed successfully :)")
        print("[+] Go to credmap folder and type 'python2 credmap.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "34":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/bdblackhat/admin-panel-finder.git")
        os.system("cd /data/data/com.termux/files/home/admin-panel-finder && chmod +x admin_panel_finder.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Admin Panel Finder installed successfully :)")
        print("[+] Go to admin_panel_finde folder and type 'python2 admin_panel_finder.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "35":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git")
        os.system("cd /data/data/com.termux/files/home/airgeddon && chmod +x airgeddon.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Airgeddon installed successfully :)")
        print("[+] To run Airgeddon install ubuntu.")
        print("[+] Then go to airgeddon folder and type './airgeddon.sh' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "36":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/commixproject/commix.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] commix installed successfully :)")
        print("[+] Go to commix folder and type 'python2 commix.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "37":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/zigoo0/webpwn3r.git")
        os.system("cd /data/data/com.termux/files/home/webpwn3r && chmod +x scan.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Webpwn3r installed successfully :)")
        print("[+] Go to webpwn3r folder and type 'python2 scan.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "38":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/ReconDog.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ReconDog installed successfully :)")
        print("[+] Go to ReconDog folder and type 'python2 dog.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "39":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/susmithHCK/cpscan.git")
        os.system("cd /data/data/com.termux/files/home/cpscan && chmod +x cpscan.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] cpscan installed successfully :)")
        print("[+] Go to cpscan folder and type 'python2 cpscan.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "40":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y tor")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] tor installed successfully :)")
        print("[+] To use tor type 'tor' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "41":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("pkg install -y tor")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/dotfighter/torshammer.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] torshammer installed successfully :)")
        print("[+] Go to torshammer folder and type 'python2 torshammer.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "42":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y tsu")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/SpencerDelta/Gloom-Framework.git")
        os.system("cd /data/data/com.termux/files/home/Gloom-Framework && chmod +x install.py")
        os.system("cd /data/data/com.termux/files/home/Gloom-Framework && chmod +x gloom.py")
        os.system("cd /data/data/com.termux/files/home/Gloom-Framework")
        os.system("cd /data/data/com.termux/files/home/Gloom-Framework && python2 install.py")
        os.system("cd /data/data/com.termux/files/home/Gloom-Framework && pip2 install bs4")
        os.system("cd /data/data/com.termux/files/home/Gloom-Framework && pip2 install beautifulsoup")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Gloom-Framework installed successfully :)")
        print("[+] Go to Gloom-Framework folder and type 'python2 gloom.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "43":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/verluchie/termux-lazysqlmap.git")
        os.system("cd /data/data/com.termux/files/home/termux-lazysqlmap")
        os.system("cd /data/data/com.termux/files/home/termux-lazysqlmap && chmod 777 install.sh")
        os.system("cd /data/data/com.termux/files/home/termux-lazysqlmap && ./install.sh")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Lazysqlmap installed successfully :)")
        print("[+] Go to termux-lazysqlmap folder and type 'lazysqlmap' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "44":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("pkg install -y tor")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/k4m4/onioff.git")
        os.system("cd /data/data/com.termux/files/home/onioff && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] onioff installed successfully :)")
        print("[+] Go to onioff folder and type 'python2 onioff.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "45":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y curl")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/googleinurl/SCANNER-INURLBR.git")
        os.system("cd /data/data/com.termux/files/home/SCANNER-INURLBR")
        os.system("cd /data/data/com.termux/files/home/SCANNER-INURLBR && chmod +x inurlbr.php")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SCANNER-INURLBR installed successfully :)")
        print("[+] Go to SCANNER-INURLBR folder and type 'php inurlbr.php' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "46":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y ruby")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ruby installed successfully :)")
        print("[+] Go to ruby folder and type 'ruby file name.rb' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "47":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/bytezcrew/wfdroid-termux.git")
        os.system("cd /data/data/com.termux/files/home/wfdroid-termux")
        os.system("cd /data/data/com.termux/files/home/wfdroid-termux && chmod 777 wfdinstall")
        os.system("cd /data/data/com.termux/files/home/wfdroid-termux && ./wfdinstall")
        os.system("cd /data/data/com.termux/files/home/wfdroid-termux && chmod +x master.1")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] wfdroid installed successfully :)")
        print("[+] Go to wfdroid-termux folder and type './master.1' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "48":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/r00tmars/XPL-SEARCH.git")
        os.system("cd /data/data/com.termux/files/home/XPL-SEARCH")
        os.system("cd /data/data/com.termux/files/home/XPL-SEARCH && chmod +x 'xpl search.php' ")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] XPL-SEARCH installed successfully :)")
        print("[+] Go to XPL-SEARCH folder and type php 'xpl search.php' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "49":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/st42/termux-sudo.git")
        os.system("cd /data/data/com.termux/files/home/termux-sudo")
        os.system("cat sudo > /data/data/com.termux/files/usr/bin/sudo")
        os.system("chmod 700 /data/data/com.termux/files/usr/bin/sudo")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Sudo installed successfully :)")
        print("[+] to run sudo type 'sudo' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "50":
        os.system("pkg install -y w3m")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] w3m installed successfully :)")
        print("[+] To run w3m type 'w3m www.google.com' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "99":
        print("""
__________________________________________


    Thanks For Using Tool-X.......(°_°) 


      _____           _     __  __
     |_   _|__   ___ | |    \ \/ /
       | |/ _ \ / _ \| |_____\  /
       | | (_) | (_) | |_____/  \     
       |_|\___/ \___/|_|    /_/\_\ v1.0


Created BY : User-X                  V_1.0
__________________________________________
""")
        break
