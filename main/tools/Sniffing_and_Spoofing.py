from main.tools import banner, colors, template,Vulnerability_Analysis
import os
import requests
from bs4 import BeautifulSoup

# main function


def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Sniffing & Spoofing")
        list_attacks = [" Wireshark\t\t(Recommended)", " Bettercap\t\t(Recommended)", " Tcpdump", " Dsniff", " Scapy", " Netsniff-ng", " Macchanger",
                        " Responder", " Airgeddon",  "Wifi-Pumpkin-3\t(Recommended)", "mitmproxy\t\t(Recommended) ", "zaproxy ", "Go Back"]
        for i in range(len(list_attacks)):
            print(colors.options, f"{i+1}) {list_attacks[i]}".title(), colors.reset)
        try:
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            return
        if option == "1":
            print("\n[+] Wireshark")
            Vulnerability_Analysis.wireshark()
        elif option == "2":
            print("\n[+] Bettercap")
            bettercap()
        elif option == "3":
            print("\n[+] Tcpdump")
            tcpdump()    
        elif option == "4":
            print("\n[+] Dsniff")
            dsniff()        
        elif option == "5":
            print("\n[+] Scapy")
            scapy()
        elif option == "6":
            print("\n[+] Netsniff-ng")
            netsniff_ng()    
        elif option == "7":
            print("\n[+] Macchanger")
            macchanger()        
        elif option == "8":
            print("\n[+] Responder")
            responder()    
        elif option == "9":
            print("\n[+] Airgeddon")
            airgeddon()               
        elif option == "10":
            print("\n[+] Wifi-Pumpkin-3")
            wifipumpkin3()        
        elif option == "11":
            print("\n[+] mitmproxy")
            mitmproxy()        
        elif option == "12":
            print("\n[+] zaproxy")
            zaproxy()        
        else:
            return


def github_getting_text(link, selector, indexvalue):
    print("Please Wait....\r", end="")
    URL = link
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')
        paras = soup.select(selector)
        # check index value from test file
        return paras[indexvalue].text
    except:
        return f"{colors.red}Not Loaded Because No Internet Connection{colors.reset}"

def tcpdump():
    os.system("clear")
    github = github_getting_text(
                "https://opensource.com/article/18/10/introduction-tcpdump", 'p', 5)
    template.template("tcpdump", "tcpdump -h", github.strip()+'\r\n - '.join(github.strip().split('\n')), {"TCPDump": "https://www.qnx.com/developers/docs/7.0.0/index.html#com.qnx.doc.neutrino.utilities/topic/t/tcpdump.html", "Deep Packet Analysis":
                              "https://thwack.solarwinds.com/resources/b/geek-speak/posts/deep-packet-analysis---practical-applications-with-tcpdump", "TCPDump F5": "https://support.f5.com/csp/article/K2289", "TCPDump FreeBSD": "https://www.freebsd.org/cgi/man.cgi?tcpdump"})
       
       
def dsniff():
    os.system("clear")
    github = "dsniff is a collection of tools for network auditing and penetration testing. dsniff, filesnarf, mailsnarf, msgsnarf, urlsnarf, and webspy passively monitor a network for interesting data (passwords, e-mail, files, etc.). arpspoof, dnsspoof, and macof facilitate the interception of network traffic normally unavailable to an attacker (e.g, due to layer-2 switching). sshmitm and webmitm implement active monkey-in-the-middle attacks against redirected SSH and HTTPS sessions by exploiting weak bindings in ad-hoc PKI."
    template.template("dsniff", "dsniff -h", github.strip(), {"Dsniff Repo": "https://github.com/tecknicaltom/dsniff",
                              "Manpages Dsniff": "https://www.unix.com/man-page/debian/8/dsniff/", "Introduction": "http://www.ouah.org/dsniffintr.htm"})
        
def scapy():
    os.system("clear")
    github = "Scapy is a Python program that enables the user to send, sniff and dissect and forge network packets. This capability allows construction of tools that can probe, scan or attack networks."
    template.template("scapy", "chmod +x run_scapy && ./run_scapy", github.strip(), {"what is Scapy": "https://www.freecodecamp.org/news/how-to-use-scapy-python-networking/", "Scapy Introduction": "https://scapy.readthedocs.io/en/latest/introduction.html", "Scapy Usage": "https://python.astrotech.io/network/transport/scapy.html", "Scapy Tutorial": "https://youtu.be/LvaII2PEwcQ",
                              "https://datascientest.com/en/scapy-everything-you-need-to-know-about-the-python-based-network-packaging-tool": "https://datascientest.com/en/scapy-everything-you-need-to-know-about-the-python-based-network-packaging-tool"}, method="github", github_install="git clone https://github.com/secdev/scapy.git", github_check="scapy")
        
def netsniff_ng():
    os.system("clear")
    github_text_0 = github_getting_text(
                "http://netsniff-ng.org/", 'p', 0)
    github_text_1 = github_getting_text(
                "http://netsniff-ng.org/", 'p', 1)
    github_text_2 = github_getting_text(
                "http://netsniff-ng.org/", 'p', 2)
    github = github_text_0.strip().replace("\n", "").replace("\t", "") + github_text_1.strip().replace("\n", "").replace("\t", "") + github_text_2.strip().replace("\n", "").replace("\t", "")
    template.template("netsniff-ng", "netsniff-ng -h", github.strip(), {"Netsniff-ng Website": "http://netsniff-ng.org/", "Sniffing Network Traffic": "https://medium.com/purple-team/sniffing-network-traffic-with-netsniff-ng-55b8f5d436c2",
                              "Manual": "https://linux.die.net/man/8/netsniff-ng", "Video Resources": "https://www.irongeek.com/i.php?page=videos/hack3rcon4/09-netsniff-ng-jon-schipp"})
        
def macchanger():
    os.system("clear")
    github_fetch = github_getting_text(
                "https://www.kali.org/tools/macchanger/", 'p', 0)
    github = github_fetch.strip().replace("\n", "").replace("\t", "")
    template.template("macchanger", "macchanger --help", github.strip(), {"How to Change Mac Address": "https://linuxconfig.org/how-to-change-mac-address-using-macchanger-on-kali-linux/",
                              "Macchanger on Kali Linux": "https://kennyvn.com/change-mac-address-macchanger-kali-linux/", "Permanently Change Mac Address": "https://www.linuxuprising.com/2018/05/how-to-permanently-change-mac-address.html"})
        
def responder():
    os.system("clear")
    github_text_0 = github_getting_text(
                "https://www.kali.org/tools/responder/", 'p', 1)
    github_text_1 = github_getting_text(
                "https://www.kali.org/tools/responder/", 'p', 2)
    github = github_text_0.strip().replace("\n", "").replace("\t", "") + github_text_1.strip().replace("\n", "").replace("\t", "")
    template.template("responder", "responder -h", github, {"Responder-Guide": "https://www.ivoidwarranties.tech/posts/pentesting-tuts/responder/guide/", "How-To-Use-Responder-to-Capture-NETNTLM-and-Grab-a-Shell":
                              "https://www.a2secure.com/blog-en/how-to-use-responder-to-capture-netntlm-and-grab-a-shell/", "infinitelogins.com-Responder": "https://infinitelogins.com/tag/responder/", "Capture-Window-10-NTLM-Hashes-Responder": "https://secnhack.in/capture-window-10-ntlm-hashes-responder"})
        
def airgeddon():
    os.system("clear")
    github = "Airgeddon is a wireless security auditing tool that is used to assess the security of wireless networks. It can be used to perform various types of attacks, such as cracking WPA/WPA2 passwords, capturing WPA/WPA2 handshakes, and identifying vulnerable wireless access points. The tool is open-source and runs on Linux systems. Airgeddon is not intended for illegal use, and should only be used on networks that you have permission to test."
    template.template("airgeddon", "airgeddon", github.strip(), {"How to Use Airgeddon in Kali Linux": "https://www.systranbox.com/how-to-use-airgeddon-in-kali-linux/", "Airgeddon Wifi Crack in Kali Linux": "https://www.kalilinux.in/2021/03/airgeddon-wifi-crack-kalilinux.html",
                              "Airgeddon Multi-Use Bash Script to Audit Wireless Networks": "https://xploitlab.com/airgeddon-multi-use-bash-script-to-audit-wireless-networks/", "Airgeddon Tool Installation and Fix All Errors": "https://www.hacknos.com/airgeddon-tool-installation-and-fix-all-errors/"})
        
def wifipumpkin3():
    os.system("clear")
    github = github_getting_text(
                "https://wifipumpkin3.github.io/", 'p', 1)
    template.template("wifipumpkin3", "wifipumpkin3", github.strip(), {
                              "Wireless Penetration Testing": "https://www.hackingarticles.in/wireless-penetration-testing-wifipumpkin3/", "WiFiPumpkin3 : Powerful Framework For Rogue Access Point Attack": "https://kalilinuxtutorials.com/wifipumpkin3/"})
        
def mitmproxy():
    os.system("clear")
    github = "mitmproxy is an interactive, SSL/TLS-capable intercepting proxy with a console interface for HTTP/1, HTTP/2, and WebSockets.mitmdump is the command-line version of mitmproxy. Think tcpdump for HTTP.mitmweb is a web-based interface for mitmproxy."
    template.template("mitmproxy", "mitmproxy", github.strip(), {
                              "An Introduction to mitmproxy": "https://medium.com/ciandt-techblog/an-introduction-to-mitmproxy-f3654e6bd53b", "mitmproxy docs": "https://docs.mitmproxy.org/stable/", })
        
def zaproxy():
    os.system("clear")
    github = github_getting_text(
                "https://github.com/zaproxy/zaproxy", 'p[dir=auto]', 2)
    template.template("zaproxy", "zaproxy", github.strip(), {
                              "Overview ZAP": "https://www.zaproxy.org/getting-started/", })
        
def bettercap():
    os.system("clear")
    github = github_getting_text(
                "https://www.bettercap.org/intro/", 'p', 0)
    template.template("bettercap", "bettercap", github.strip(), {"Man in the Middle": "https://www.cybervie.com/blog/easy-and-better-man-in-the-middle-using-bettercap/", "MITM Labs Write-up":
                              "https://charlesreid1.com/wiki/MITM_Labs/Bettercap_Over_Wifi", "NTLM Capturing": "https://blog.xpnsec.com/bettercap-capturing-ntlm/", "DNS Spoofing": "https://psychovik.medium.com/dns-spoofing-using-bettercap-24a8435f7a03"})
        

if __name__ == '__main__':
    main()
