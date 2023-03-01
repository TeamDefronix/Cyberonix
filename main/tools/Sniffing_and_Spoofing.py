from main.tools import banner,run_on_browser,waiting,writeup,colors
import os
import subprocess
import threading
import time
import requests
from bs4 import BeautifulSoup

def check_installed(name,needargs=False):
    proc = subprocess.Popen([f"dpkg -s {name} 2>/dev/null"], stdout=subprocess.PIPE, shell=True)
    #there keyfor success output and noththere for error output
    (there, notthere) = proc.communicate()
    if "install ok installed" not in there.decode():
                print(f"{colors.red}[-] Not Installed")
                print(f"[+] It Is Not Installed In Your Kali{colors.reset}")
                download=input(f"{colors.blue}[+] Do You Want To Install It?(y/n):{colors.reset}")
                if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                    os.system(f"apt install {name} -y")
                    if needargs:
                        download=input(f"{colors.green}Do You Want To Run The Tool?(y/n):{colors.reset}")
                        if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                            #when tool is of cli no need of thread
                            thread_run(name,needargs)
                    else:
                        download=input(f"{colors.green}Do You Want To Run The Tool?(y/n):{colors.reset}")
                        if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                            #when tool is of gui it needs thread
                            
                            os.system(f"{name}")
    else:
                print(f"{colors.green}[+] Installed")
                print(f"[+] It Is Installed In Your Kali{colors.reset}")
                if needargs:
                        download=input(f"{colors.green}Do You Want To Run The Tool?(y/n):{colors.reset}")
                        if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                            #when tool is of cli no need of thread
                            thread_run(name,needargs)
                else:
                        download=input(f"{colors.green}Do You Want To Run The Tool?(y/n):{colors.reset}")
                        if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                            #when tool is of gui it needs thread
                            
                            os.system(f"{name} > /dev/null 2>&1")
def thread_run(command,needargs=False):
    if needargs=="no-help":
        #it will run only help because it is in cli
        os.system(f"{command}")
    elif needargs:
        os.system(f"{command} -h")
    else:
        #for gui all errors/output will go in null 
        os.system(f"{command} > /dev/null 2>&1")

def github_getting_text(link,selector,indexvalue):
    print("Please Wait....\r",end="")
    URL = link
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        paras = soup.select(selector)
        #check index value from test file
        return paras[indexvalue].text
    except:
        return "Not loaded because no internet connection"

def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Sniffing & Spoofing")
        list_attacks=[" Wireshark"," Bettercap"," Tcpdump"," Arpspoof"," Dsniff"," Scapy"," Netsniff-ng"," Macchanger"," Responder"," Airgeddon","Sharesniffer","Wifi-Pumpkin-3","go back"]
        for i in range(len(list_attacks)):
                print(colors.options,f"{i}) {list_attacks[i]}".title(),colors.reset)
        option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        if option=="0":
            print("\n[+] Wireshark")
            os.system("clear")
            Wireshark()
        elif option=="1":
            print("\n[+] Bettercap")
            os.system("clear")
            Bettercap()
        elif option=="2":
            print("\n[+] Tcpdump")
            os.system("clear")
            Tcpdump()
        elif option=="3":
            print("\n[+] Arpspoof")
            os.system("clear")
            Arpspoof()
        elif option=="4":
            print("\n[+] Dsniff")
            os.system("clear")
            Dsniff()
        elif option=="5":
            print("\n[+] Scapy")
            os.system("clear")
            Scapy()
        elif option=="6":
            print("\n[+] Netsniff-ng")
            os.system("clear")
            Netsniff()
        elif option=="7":
            print("\n[+] Macchanger")
            os.system("clear")
            Macchanger()
        elif option=="8":
            print("\n[+] Responder")
            os.system("clear")
            Responder()
        elif option=="9":
            print("\n[+] Airgeddon")
            os.system("clear")
            Airgeddon()
        elif option=="10":
            print("\n[+] Sharesniffer")
            os.system("clear")
            Sharesniffer()
        elif option=="11":
            print("\n[+] Wifi-Pumpkin-3")
            os.system("clear")
            WifiPumpkin()
        else:
            return
def Wireshark():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Wireshark")
        banner.description("Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis, software and communications protocol development, and education. It can be used to examine data from a live network or from a previously saved capture file. Wireshark provides a graphical user interface (GUI) for capturing and analyzing network traffic. It supports a wide range of protocols and can be run on various operating systems, including Windows, macOS, and Linux")
        ask=tool_writeups()
        if ask=="1":
            ask_install=input(f"{colors.blue}[+] Do you want to install Wireshark or not?(y/n):{colors.reset}")
            if ask_install=="y" or ask_install=="Y" or ask_install=="Yes" or ask_install=="yes":
                check_installed("wireshark")
            
        elif ask=="2":
            #first argument for dictionary(key=title,value=url) second argument for banner 
            writeup.writeup({"Wireshark Cheat-Sheet":"https://www.comparitech.com/net-admin/wireshark-cheat-sheet","What-is-Wireshark-and-How-to-Use-it":"https://www.comptia.org/content/articles/what-is-wireshark-and-how-to-use-it ","Video Resource Wireshark":"https://www.youtube.com/playlist?list=PLBf0hzazHTGPgyxeEj_9LBHiqjtNEjsgt"},"Wireshark writeup.writeup")
        else:
            return

def Bettercap():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Bettercap")
        github_text_0=github_getting_text("https://github.com/bettercap/bettercap",'p[dir="auto"]',3)
        banner.description(github_text_0)
        ask=tool_writeups()
        if ask=="1":
            ask_install=input(f"{colors.blue}[+] Do you want to install Bettercap or not?(y/n):{colors.reset}")
            if ask_install=="y" or ask_install=="Y" or ask_install=="Yes" or ask_install=="yes":
                check_installed("bettercap")
                waiting.waiting()
            
        elif ask=="2":
            writeup.writeup({"Man in the Middle": "https://www.cybervie.com/blog/easy-and-better-man-in-the-middle-using-bettercap/", "MITM Labs Write-up": "https://charlesreid1.com/wiki/MITM_Labs/Bettercap_Over_Wifi", "NTLM Capturing": "https://blog.xpnsec.com/bettercap-capturing-ntlm/", "DNS Spoofing": "https://psychovik.medium.com/dns-spoofing-using-bettercap-24a8435f7a03"},"Bettercap writeup.writeup")
        else:
            return

def Tcpdump():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Tcpdump")
        github_text_0=github_getting_text("https://opensource.com/article/18/10/introduction-tcpdump",'p',5)
        github_text_1=github_getting_text("https://opensource.com/article/18/10/introduction-tcpdump",'p',6)
        merged_text = github_text_0 + github_text_1
        banner.description(merged_text)
        
        ask=tool_writeups()
        if ask=="1":
            ask_install=input(f"{colors.blue}[+] Do you want to install Tcpdump or not?(y/n):{colors.reset}")
            if ask_install=="y" or ask_install=="Y" or ask_install=="Yes" or ask_install=="yes":
                check_installed("tcpdump")
                waiting.waiting()
            
        elif ask=="2":
            writeup.writeup({"TCPDump": "https://www.qnx.com/developers/docs/7.0.0/index.html#com.qnx.doc.neutrino.utilities/topic/t/tcpdump.html","Deep Packet Analysis": "https://thwack.solarwinds.com/resources/b/geek-speak/posts/deep-packet-analysis---practical-applications-with-tcpdump","TCPDump F5": "https://support.f5.com/csp/article/K2289","TCPDump FreeBSD": "https://www.freebsd.org/cgi/man.cgi?tcpdump(1)"},"Tcp-Dump writeup.writeup")
        else:
            return
def Arpspoof():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Arpspoof")
        banner.description("\narpspoof is a utility for network auditing and penetration testing. It is part of the dsniff suite of tools, which is used to perform various types of network attacks and security auditing. It can be used to intercept and modify traffic on a local area network. It works by sending out specially crafted ARP (Address Resolution Protocol) packets, which can be used to redirect traffic from one host to another. This is known as ARP spoofing or ARP cache poisoning.")
        
        ask=tool_writeups()
        if ask=="1":
            ask_install=input(f"{colors.blue}[+] Do you want to install Arpspoof or not?(y/n):{colors.reset}")
            if ask_install=="y" or ask_install=="Y" or ask_install=="Yes" or ask_install=="yes":
                proc = subprocess.Popen([f"dpkg -s dsniff 2>/dev/null"], stdout=subprocess.PIPE, shell=True)
                #there keyfor success output and noththere for error output
                (there, notthere) = proc.communicate()
                if "install ok installed" not in there.decode():
                    print(f"{colors.green}[-] Not Installed")
                    print("[+] It Is Not Installed In Your Kali{colors.reset}")
                    download=input(f"{colors.blue}[+] Do You Want To Install It?(y/n):{colors.reset}")
                    if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                        os.system(f"apt install dsniff -y")
                        download=input(f"{colors.green}Do You Want To Run The Tool?(y/n):{colors.reset}")
                        if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                            #when tool is of cli no need of thread
                            
                            os.system("arpspoof")
                            waiting.waiting()
                        else:
                            pass
                else:
                    print(f"{colors.green}[+] Installed")
                    print(f"[+] It Is Installed In Your Kali{colors.reset}")
                    download=input(f"{colors.green}Do You Want To Run The Tool?(y/n):{colors.reset} ")
                    if download=="y" or download=="Y" or download=="Yes" or download=="yes":
                        #when tool is of cli no need of thread
                        
                        os.system("arpspoof")
                        waiting.waiting()
                    else:
                        pass
            
        elif ask=="2":
            writeup.writeup({"Arp_Spoofing_Using_Man_In_The_Middle_Attack":"https://linuxhint.com/arp_spoofing_using_man_in_the_middle_attack/","ArpSpoof Video Resource":"https://www.youtube.com/watch?v=8SIP36Fym7U"},"ArpSpoof writeup.writeup")
        else:
            return
def Dsniff():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Dsniff")
        banner.description("\ndsniff is a collection of tools for network auditing and penetration testing. dsniff, filesnarf, mailsnarf, msgsnarf, urlsnarf, and webspy passively monitor a network for interesting data (passwords, e-mail, files, etc.). arpspoof, dnsspoof, and macof facilitate the interception of network traffic normally unavailable to an attacker (e.g, due to layer-2 switching). sshmitm and webmitm implement active monkey-in-the-middle attacks against redirected SSH and HTTPS sessions by exploiting weak bindings in ad-hoc PKI.\n")
        ask=tool_writeups()
        if ask=="1":
                check_installed("dsniff")
                waiting.waiting()
        elif ask=="2":
            writeup.writeup({"Dsniff Repo": "https://github.com/tecknicaltom/dsniff","Manpages Dsniff": "https://kaisenlinux.org/manpages/dsniff.html","Introduction": "http://www.ouah.org/dsniffintr.htm"},"Dsniff writeup.writeup")
        else:
            return

def Scapy():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Scapy")
        github_text_0=github_getting_text("https://scapy.net/",'p',0)
        banner.description(github_text_0)
        ask=tool_writeups()
        if ask=="1":
                if not os.path.isdir("scapy"):
                    ask_install=input(f"{colors.blue}[+] Do you want to Download & Execute Scapy or not?(y/n):{colors.reset}")
                    if ask_install=="y" or ask_install=="Y" or ask_install=="Yes" or ask_install=="yes":
                        print(f"{colors.blue}Downloading ...  Please Wait !!{colors.reset}")
                        os.system("git clone https://github.com/secdev/scapy.git")
                        os.system("cd scapy && chmod u+x * && ./run_scapy")
                        waiting.waiting()
                else:
                    print(f"{colors.green}[+] Installed")
                    print(f"[+] it is Already Installed{colors.reset}")
                    download = input(f"{colors.green}Do You Want To Run The Tool?(y/n):{colors.reset} ")
                    if download == "y" or download == "Y" or download == "Yes" or download == "yes":
                        
                        os.system("cd scapy && chmod u+x * && ./run_scapy")
                        waiting.waiting()
                    else:
                        pass
            
        elif ask=="2":
            writeup.writeup({"what is Scapy": "https://santandergto.com/en/guide-using-scapy-with-python/#whatisScapy","Scapy Introduction": "https://scapy.readthedocs.io/en/latest/introduction.html","Scapy Usage": "https://python.astrotech.io/network/transport/scapy.html","Scapy Tutorial": "https://youtu.be/LvaII2PEwcQ"},"Scapy writeup.writeup")
        else:
            return

def Netsniff():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Netsniff-ng")
        github_text_0=github_getting_text("http://netsniff-ng.org/",'p',0)
        github_text_1=github_getting_text("http://netsniff-ng.org/",'p',1)
        github_text_2=github_getting_text("http://netsniff-ng.org/",'p',2)
        merged_text = github_text_0 + github_text_1 + github_text_2
        banner.description(merged_text)
        ask=tool_writeups()
        if ask=="1":
                check_installed("netsniff-ng")
                waiting.waiting()
        elif ask=="2":
            writeup.writeup({"Netsniff-ng Website": "http://netsniff-ng.org/", "Sniffing Network Traffic": "https://medium.com/purple-team/sniffing-network-traffic-with-netsniff-ng-55b8f5d436c2", "Manual": "https://linux.die.net/man/8/netsniff-ng", "Video Resources": "https://www.irongeek.com/i.php?page=videos/hack3rcon4/09-netsniff-ng-jon-schipp"},"Netsniff-ng writeup.writeup")
        else:
            return

def Macchanger():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Mac-changer")
        github_text_0=github_getting_text("https://www.kali.org/tools/macchanger/",'p',0)
        banner.description(github_text_0)
        ask=tool_writeups()
        if ask=="1":
                check_installed("macchanger")
                waiting.waiting()
            
        elif ask=="2":
            #first argument for dictionary(key=title,value=url) second argument for banner 
            writeup.writeup({"How to Change Mac Address": "https://linuxconfig.org/how-to-change-mac-address-using-macchanger-on-kali-linux/", "Macchanger on Kali Linux": "https://kennyvn.com/change-mac-address-macchanger-kali-linux/", "Permanently Change Mac Address": "https://www.linuxuprising.com/2018/05/how-to-permanently-change-mac-address.html"},"Mac-changer writeup.writeup")
        else:
            return

def Responder():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Responder")
        github_text_0=github_getting_text("https://www.kali.org/tools/responder/",'p',1)
        github_text_1=github_getting_text("https://www.kali.org/tools/responder/",'p',2)
        merged_text = github_text_0 + github_text_1
        banner.description(merged_text)
        ask=tool_writeups()
        if ask=="1":
                check_installed("responder")
                waiting.waiting()
        elif ask=="2":
            #first argument for dictionary(key=title,value=url) second argument for banner 
            writeup.writeup({"Responder-Guide": "https://www.ivoidwarranties.tech/posts/pentesting-tuts/responder/guide/","How-To-Use-Responder-to-Capture-NETNTLM-and-Grab-a-Shell": "https://www.a2secure.com/blog-en/how-to-use-responder-to-capture-netntlm-and-grab-a-shell/","infinitelogins.com-Responder": "https://infinitelogins.com/tag/responder/","Capture-Window-10-NTLM-Hashes-Responder": "https://secnhack.in/capture-window-10-ntlm-hashes-responder"},"Responder writeup.writeup")
        else:
            return

def Airgeddon():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Airgeddon")
        banner.description("Airgeddon is a wireless security auditing tool that is used to assess the security of wireless networks. It can be used to perform various types of attacks, such as cracking WPA/WPA2 passwords, capturing WPA/WPA2 handshakes, and identifying vulnerable wireless access points. The tool is open-source and runs on Linux systems. Airgeddon is not intended for illegal use, and should only be used on networks that you have permission to test.")
        ask=tool_writeups()
        if ask=="1":
            ask_install=input(f"{colors.blue}[+] Do you want to install Airgeddon or not?(y/n):{colors.reset} ")
            if ask_install=="y" or ask_install=="Y" or ask_install=="Yes" or ask_install=="yes":
                check_installed("airgeddon")
                waiting.waiting()
            
        elif ask=="2":
            #first argument for dictionary(key=title,value=url) second argument for banner 
            writeup.writeup({"How to Use Airgeddon in Kali Linux":"https://www.systranbox.com/how-to-use-airgeddon-in-kali-linux/", "Airgeddon Wifi Crack in Kali Linux":"https://www.kalilinux.in/2021/03/airgeddon-wifi-crack-kalilinux.html", "Airgeddon Multi-Use Bash Script to Audit Wireless Networks":"https://xploitlab.com/airgeddon-multi-use-bash-script-to-audit-wireless-networks/", "Airgeddon Tool Installation and Fix All Errors":"https://www.hacknos.com/airgeddon-tool-installation-and-fix-all-errors/"},"Airgeddon writeup.writeup")
        else:
            return
        
def Sharesniffer():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Sharesniffer")
        github_text_0=github_getting_text("https://github.com/shirosaidev/sharesniffer",'p[dir="auto"]',2)
        banner.description(github_text_0)
        ask=tool_writeups()
        if ask=="1":
                if os.path.isfile("sharesniffer.py"):
                    print(f"{colors.green}[+] Downloaded")
                    print(f"[+] it is Already Installed{colors.reset}")
                    os.system("chmod +x sharesniffer.py && ./sharesniffer.py")
                else:
                    ask_install=input(f"{colors.blue}[+] Do you want to Download & Execute Sharesniffer or not?(y/n):{colors.reset} ")
                    if ask_install=="y" or ask_install=="Y" or ask_install=="Yes" or ask_install=="yes":
                        os.system("curl -s https://raw.githubusercontent.com/shirosaidev/sharesniffer/master/sharesniffer.py -o sharesniffer.py && chmod +x sharesniffer.py && ./sharesniffer.py")
                waiting.waiting()
            
            
        elif ask=="2":
            writeup.writeup({"Sharesniffer Github-Repo":"github.com/shirosaidev/sharesniffer","Sharesniffer Presentation":"slideplayer.com/slide/6055181/"},"Sharesniffer writeup.writeup")
        else:
            return

def WifiPumpkin():
    while True:
        os.system("clear")
        banner.main()
        github_text_0=github_getting_text("https://github.com/P0cL4bs/wifipumpkin3",'p[dir="auto"]',4)
        banner.description(github_text_0)
        ask=tool_writeups()
        if ask=="1":
                check_installed("wifipumpkin3")
                waiting.waiting()
            
        elif ask=="2":
            #first argument for dictionary(key=title,value=url) second argument for banner 
            writeup.writeup({"Wireless Penetration Testing": "https://www.hackingarticles.in/wireless-penetration-testing-wifipumpkin3/", "WiFiPumpkin3 : Powerful Framework For Rogue Access Point Attack": "https://kalilinuxtutorials.com/wifipumpkin3/"},"Wifi-Pumpkin-3 writeup.writeup")
        else:
            return

        
def tool_writeups():
    print(f"{colors.options}1) TOOL(About,Installation)")
    print(f"2) Write Ups")
    print(f"3) Go Back..")
    ask=input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
    return ask

if __name__ == "__main__": 
    main()
