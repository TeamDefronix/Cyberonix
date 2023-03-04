from main.tools import banner,colors,template
import os
import requests
from bs4 import BeautifulSoup

#main function
def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Sniffing & Spoofing")
        list_attacks=[" Wireshark"," Bettercap"," Tcpdump"," Arpspoof"," Dsniff"," Scapy"," Netsniff-ng"," Macchanger"," Responder"," Airgeddon","Sharesniffer","Wifi-Pumpkin-3","Go Back"]
        for i in range(len(list_attacks)):
                print(colors.options,f"{i}) {list_attacks[i]}".title(),colors.reset)
        option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        if option=="0":
            print("\n[+] Wireshark")
            os.system("clear")
            # name,command,discription,writeup,link=True,method="kali",github_install="",github_check=True
            github = "Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis, software and communications protocol development, and education. It can be used to examine data from a live network or from a previously saved capture file. Wireshark provides a graphical user interface (GUI) for capturing and analyzing network traffic."
            template.template("wireshark","wireshark",github.strip(),{"Wireshark Cheat-Sheet":"https://www.comparitech.com/net-admin/wireshark-cheat-sheet","What-is-Wireshark-and-How-to-Use-it":"https://www.comptia.org/content/articles/what-is-wireshark-and-how-to-use-it ","Video Resource Wireshark":"https://www.youtube.com/playlist?list=PLBf0hzazHTGPgyxeEj_9LBHiqjtNEjsgt"})        
        elif option=="1":
            print("\n[+] Bettercap")
            os.system("clear")
            github=github_getting_text("https://github.com/bettercap/bettercap",'p[dir="auto"]',3)
            template.template("bettercap","bettercap",github.strip(),{"Man in the Middle": "https://www.cybervie.com/blog/easy-and-better-man-in-the-middle-using-bettercap/", "MITM Labs Write-up": "https://charlesreid1.com/wiki/MITM_Labs/Bettercap_Over_Wifi", "NTLM Capturing": "https://blog.xpnsec.com/bettercap-capturing-ntlm/", "DNS Spoofing": "https://psychovik.medium.com/dns-spoofing-using-bettercap-24a8435f7a03"})
        elif option=="2":
            print("\n[+] Tcpdump")
            os.system("clear")
            github = github_getting_text("https://opensource.com/article/18/10/introduction-tcpdump",'p',5)
            template.template("tcpdump","tcpdump -h",github.strip()+'\r\n - '.join(github.strip().split('\n')),{"TCPDump": "https://www.qnx.com/developers/docs/7.0.0/index.html#com.qnx.doc.neutrino.utilities/topic/t/tcpdump.html","Deep Packet Analysis": "https://thwack.solarwinds.com/resources/b/geek-speak/posts/deep-packet-analysis---practical-applications-with-tcpdump","TCPDump F5": "https://support.f5.com/csp/article/K2289","TCPDump FreeBSD": "https://www.freebsd.org/cgi/man.cgi?tcpdump(1)"})
        elif option=="3":
            print("\n[+] Arpspoof")
            os.system("clear")
            github = "arpspoof is a utility for network auditing and penetration testing. It is part of the dsniff suite of tools, which is used to perform various types of network attacks and security auditing. It can be used to intercept and modify traffic on a local area network. It works by sending out specially crafted ARP (Address Resolution Protocol) packets, which can be used to redirect traffic from one host to another. This is known as ARP spoofing or ARP cache poisoning."
            template.template("dsniff","arpspoof",github.strip(),{"Arp_Spoofing_Using_Man_In_The_Middle_Attack":"https://linuxhint.com/arp_spoofing_using_man_in_the_middle_attack/","ArpSpoof Video Resource":"https://www.youtube.com/watch?v=8SIP36Fym7U"})
        elif option=="4":
            print("\n[+] Dsniff")
            os.system("clear")
            github = "dsniff is a collection of tools for network auditing and penetration testing. dsniff, filesnarf, mailsnarf, msgsnarf, urlsnarf, and webspy passively monitor a network for interesting data (passwords, e-mail, files, etc.). arpspoof, dnsspoof, and macof facilitate the interception of network traffic normally unavailable to an attacker (e.g, due to layer-2 switching). sshmitm and webmitm implement active monkey-in-the-middle attacks against redirected SSH and HTTPS sessions by exploiting weak bindings in ad-hoc PKI."
            template.template("dsniff","dsniff -h",github.strip(),{"Dsniff Repo": "https://github.com/tecknicaltom/dsniff","Manpages Dsniff": "https://kaisenlinux.org/manpages/dsniff.html","Introduction": "http://www.ouah.org/dsniffintr.htm"})
        elif option=="5":
            print("\n[+] Scapy")
            os.system("clear")
            github=github_getting_text("https://scapy.net/",'p',0)
            template.template("scapy","chmod +x run_scapy && ./run_scapy",github.strip(),{"what is Scapy": "https://santandergto.com/en/guide-using-scapy-with-python/#whatisScapy","Scapy Introduction": "https://scapy.readthedocs.io/en/latest/introduction.html","Scapy Usage": "https://python.astrotech.io/network/transport/scapy.html","Scapy Tutorial": "https://youtu.be/LvaII2PEwcQ"},method="github",github_install="git clone https://github.com/secdev/scapy.git",github_check="scapy")
        elif option=="6":
            print("\n[+] Netsniff-ng")
            os.system("clear")
            github_text_0=github_getting_text("http://netsniff-ng.org/",'p',0)
            github_text_1=github_getting_text("http://netsniff-ng.org/",'p',1)
            github_text_2=github_getting_text("http://netsniff-ng.org/",'p',2)
            github = github_text_0 + github_text_1 + github_text_2
            template.template("netsniff-ng","netsniff-ng -h",github.strip(),{"Netsniff-ng Website": "http://netsniff-ng.org/", "Sniffing Network Traffic": "https://medium.com/purple-team/sniffing-network-traffic-with-netsniff-ng-55b8f5d436c2", "Manual": "https://linux.die.net/man/8/netsniff-ng", "Video Resources": "https://www.irongeek.com/i.php?page=videos/hack3rcon4/09-netsniff-ng-jon-schipp"})
        elif option=="7":
            print("\n[+] Macchanger")
            os.system("clear")
            github=github_getting_text("https://www.kali.org/tools/macchanger/",'p',0)
            template.template("macchanger","macchanger --help",github.strip(),{"How to Change Mac Address": "https://linuxconfig.org/how-to-change-mac-address-using-macchanger-on-kali-linux/", "Macchanger on Kali Linux": "https://kennyvn.com/change-mac-address-macchanger-kali-linux/", "Permanently Change Mac Address": "https://www.linuxuprising.com/2018/05/how-to-permanently-change-mac-address.html"})
        elif option=="8":
            print("\n[+] Responder")
            os.system("clear")
            github_text_0=github_getting_text("https://www.kali.org/tools/responder/",'p',1)
            github_text_1=github_getting_text("https://www.kali.org/tools/responder/",'p',2)
            github = github_text_0 + github_text_1
            template.template("responder","responder -h",github,{"Responder-Guide": "https://www.ivoidwarranties.tech/posts/pentesting-tuts/responder/guide/","How-To-Use-Responder-to-Capture-NETNTLM-and-Grab-a-Shell": "https://www.a2secure.com/blog-en/how-to-use-responder-to-capture-netntlm-and-grab-a-shell/","infinitelogins.com-Responder": "https://infinitelogins.com/tag/responder/","Capture-Window-10-NTLM-Hashes-Responder": "https://secnhack.in/capture-window-10-ntlm-hashes-responder"})
        elif option=="9":
            print("\n[+] Airgeddon")
            os.system("clear")
            github = "Airgeddon is a wireless security auditing tool that is used to assess the security of wireless networks. It can be used to perform various types of attacks, such as cracking WPA/WPA2 passwords, capturing WPA/WPA2 handshakes, and identifying vulnerable wireless access points. The tool is open-source and runs on Linux systems. Airgeddon is not intended for illegal use, and should only be used on networks that you have permission to test."
            template.template("airgeddon","airgeddon",github.strip(),{"How to Use Airgeddon in Kali Linux":"https://www.systranbox.com/how-to-use-airgeddon-in-kali-linux/", "Airgeddon Wifi Crack in Kali Linux":"https://www.kalilinux.in/2021/03/airgeddon-wifi-crack-kalilinux.html", "Airgeddon Multi-Use Bash Script to Audit Wireless Networks":"https://xploitlab.com/airgeddon-multi-use-bash-script-to-audit-wireless-networks/", "Airgeddon Tool Installation and Fix All Errors":"https://www.hacknos.com/airgeddon-tool-installation-and-fix-all-errors/"})
        elif option=="10":
            print("\n[+] Sharesniffer")
            os.system("clear")
            github=github_getting_text("https://github.com/shirosaidev/sharesniffer",'p[dir="auto"]',2)
            template.template("sharesniffer","pip install python-nmap netifaces >/dev/null 2>&1 && chmod +x sharesniffer.py && ./sharesniffer.py -h",github.strip(),{"Sharesniffer Github-Repo":"github.com/shirosaidev/sharesniffer","Sharesniffer Presentation":"slideplayer.com/slide/6055181/"},method="github",github_install="git clone https://github.com/shirosaidev/sharesniffer",github_check="sharesniffer")    
        elif option=="11":
            print("\n[+] Wifi-Pumpkin-3")
            os.system("clear")
            github=github_getting_text("https://github.com/P0cL4bs/wifipumpkin3",'p[dir="auto"]',4)
            template.template("wifipumpkin3","wifipumpkin3",github.strip(),{"Wireless Penetration Testing": "https://www.hackingarticles.in/wireless-penetration-testing-wifipumpkin3/", "WiFiPumpkin3 : Powerful Framework For Rogue Access Point Attack": "https://kalilinuxtutorials.com/wifipumpkin3/"})    
        else:
            return
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
        return f"{colors.red}Not Loaded Because No Internet Connection{colors.reset}"

if __name__=='__main__':
    main()
