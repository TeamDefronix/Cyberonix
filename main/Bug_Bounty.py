import os
from main.tools import template,banner,colors,information_gathering,Vulnerability_Analysis,Password_Hacking,WEB_Application_Analysis,Exploitation_Tools,Configuration_Management,run_on_browser
import requests
from bs4 import BeautifulSoup

def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Bug Bounty")
        list_root_attacks = ["Bug Bounty Video Series","Reconnaissance", "Intel Discovery", "Enumeration","Vulnerability Analysis","Exploitation","Reporting", "go back"]
        for i in range(len(list_root_attacks)):
            print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
        try:
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            return
        if option == "1":
            run_on_browser.main("https://github.com/defronixpro/Defronix-Cybersecurity-Roadmap/blob/main/README.md#bug-bounty")
        elif option == "2":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Reconnaissance")
                banner.description("Bug Bounty phase in reconnaissance involves ethical hackers discovering vulnerabilities in systems for rewards, enhancing cybersecurity by identifying weaknesses before malicious actors exploit them")
                list_root_attacks = ["Search Engines", "Tools","Usefull Websites", "go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    print("\n[+] Search Engines")
                    os.system("clear")
                    template.template("Search Engines", "no-tools","Best Serach Engines",
                                       {
                                           "Google": "https://www.google.com/",
                                           "DuckDuckGO":"https://duckduckgo.com/",
                                           "Shodan":"https://www.shodan.io/",
                                           "Censys":"https://search.censys.io/",
                                           "Bing":"https://www.bing.com/",
                                           "Starpage":"https://www.startpage.com/",
                                           "Ecosia":"https://www.ecosia.org/",
                                           "Brave":"https://search.brave.com/",
                                           "Yandex":"https://yandex.com/",
                                           "Ahmia":"https://ahmia.fi/",
                                           "Yahoo":"https://www.yahoo.com/",
                                           
                                       })
                elif ask == "2":
                    while True:
                        os.system("clear")
                        banner.main()
                        banner.attack("Tools")
                        banner.description("Reconnaissance Tools.")
                        list_root_attacks = [" Nmap\t\t(Recommended)"," Recon-ng\t\t(Recommended)"," theHarvester"," Subfinder\t\t(Recommended)"," Sublist3r"," SpiderFoot"," Amass\t\t(Recommended)"," Legion"," Netdiscover\t(Recommended)","Unicornscan","Feroxbuster","go back"]
                        for i in range(len(list_root_attacks)):
                            print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                        try:
                            vuln = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                        except KeyboardInterrupt:
                            return
                        if vuln == "1":
                            print("\n[+] Nmap")
                            information_gathering.nmap() 
                        elif vuln == "2":
                            print("\n[+] Recon-ng")
                            information_gathering.recon_ng()
                        elif vuln == "3":
                            print("\n[+] TheHarvester")
                            information_gathering.theharvester()
                        elif vuln == "4":
                            print("\n[+] subfinder")
                            information_gathering.subfinder()
                        elif vuln == "5":
                            print("\n[+] sublist3r")
                            information_gathering.sublist3r()
                        elif vuln == "6":
                            print("\n[+] spiderfoot")
                            information_gathering.spiderfoot()
                        elif vuln == "7":
                            print("\n[+] amass")
                            information_gathering.amass()
                        elif vuln == "8":
                            print("\n[+] legion")
                            Vulnerability_Analysis.legion()
                        elif vuln == "9":
                            print("\n[+]Netdiscover")
                            information_gathering.netdiscover()
                        elif vuln == "10":
                            print("\n[+] Unicornscan")
                            unicorn()
                        elif vuln == "11":
                            print("\n[+] Feroxbuster")
                            Configuration_Management.feroxbuster()
                        else:
                            break
                        
                elif ask == "3":
                    print("\n[+] Useful Websites")
                    os.system("clear")
                    template.template("Useful Websites","no-tools",'This is website for Bug Bounty',{
                            " Social-Search Website":"https://www.social-searcher.com/",
                            " IP2info":"https://ipinfo.io/",
                            " Viewdns":"https://viewdns.info/", 
                            " Wayback Machine":"https://archive.org/web/",
                            " Dnsdumpster":"https://dnsdumpster.com/",
                            " MXToolbox":"https://mxtoolbox.com/",
                            " Lopseg":"https://www.lopseg.com.br/osint",
                            " Arin whois":"https://whois.arin.net/ui/",
                            " Dnschecker":"https://dnschecker.org/",
                            "BGP-Toolkit":"https://bgp.he.net/",
                            "Mattw.io":"https://mattw.io/",
                            "Searchftps":"https://www.searchftps.net/",
                            "Security Headers":"https://securityheaders.com/",
                            "Robtex":"https://www.robtex.com/",
                            "Builtwith":"https://builtwith.com/",
                            "Intodns":"https://www.intodns.com/",
                            "Serachdns":"https://searchdns.netcraft.com/",
                            "Hackertarget":"https://hackertarget.com/",
                            "Vulners":"https://vulners.com/",
                            "cvedetails":"https://www.cvedetails.com/",
                            "Zero Day initiative":"https://www.zerodayinitiative.com/",})
                else:
                     break

        elif option == "3":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Discovery tools")
                banner.description("Intel Discovery in the context of bug bounty refers to Intel's bug bounty program, which aims to identify and address security vulnerabilities in their products. Researchers and ethical hackers are invited to discover and report security flaws in Intel hardware, software, and firmware. In return, they may receive monetary rewards, recognition, and the opportunity to help improve the security of Intel products. The program emphasizes responsible disclosure, meaning vulnerabilities should be reported privately to Intel to allow them to fix the issues before public disclosure.")
                list_root_attacks = ["Burpsuite\t\t(Recommended)","Owasp Zap\t\t(Recommended)","Nessus\t\t(Recommended)","Metasploit framework(Recommended)", "Dirb ","Dirsearch ","Gobuster\t\t(Recommended) ","go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    print("\n[+] Burpsuite")
                    WEB_Application_Analysis.burp_suite()
                elif ask == "2":
                    print("\n[+] Owasp Zap")
                    WEB_Application_Analysis.owasp_zap()
                elif ask == "3":
                    print("\n[+] Nessus")
                    WEB_Application_Analysis.nessus()
                elif ask == "4":
                    print("\n[+] Metasploit-Framework")
                    Exploitation_Tools.metasploit()
                elif ask == "5":
                    print("\n[+] Dirb")
                    WEB_Application_Analysis.dirb()
                elif ask == "6":
                    print("\n[+] Dirsearch")
                    WEB_Application_Analysis.dirsearch()
                elif ask == "7":
                    print("\n[+] Gobuster")
                    Configuration_Management.gobuster()
                else:
                     break
                
        elif option == "4":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Enumeration")
                banner.description("Enumeration in bug bounty refers to the process of systematically gathering information about a target system to identify potential entry points for exploitation. This can include discovering subdomains, open ports, services running on those ports, directories, files, and user accounts. Enumeration is a crucial step in the reconnaissance phase of a bug bounty program, as it helps bug hunters map the attack surface and uncover vulnerabilities that can be exploited.")
                list_root_attacks = ["Nmap\t\t(Recommended)","Unicornscan","Masscan\t\t(Recommended)","Nikto ","DNSRecon\t\t(Recommended)","go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    print("\n[+] Nmap")
                    information_gathering.nmap()
                elif ask == "2":
                    print("\n[+] Unicornscan")
                    unicorn()
                elif ask == "3":
                    print("\n[+] Masscan")
                    masscan()
                elif ask == "4":
                    print("\n[+] Nikto")
                    Vulnerability_Analysis.nikto()
                elif ask == "5":
                    print("\n[+] Dnsrecon")
                    dnsrecon()
                else:
                     break

        elif option == "5":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Vulnerability Analysis")
                banner.description("Vulnerability Analysis in bug bounty refers to the process of identifying, evaluating, and prioritizing security weaknesses in a target system. This involves examining the system's components, configurations, and code to find potential vulnerabilities that could be exploited by attackers. Bug hunters use various tools and techniques during this phase to detect issues such as SQL injection, cross-site scripting (XSS), and insecure configurations. The goal of vulnerability analysis is to understand the nature and impact of the discovered weaknesses, allowing for effective reporting and remediation.")
                list_root_attacks = ["Wpscan","Burpsuite\t\t(Recommended)","OWASP ZAP\t\t(Recommended)","Nessus\t\t(Recommended)","Sqlmap\t\t(Recommended)","go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    print("\n[+] Wpscan")
                    Vulnerability_Analysis.wpscan()
                elif ask == "2":
                    print("\n[+] Burpsuite")
                    WEB_Application_Analysis.burp_suite()
                elif ask == "3":
                    print("\n[+] Owasp Zap")
                    WEB_Application_Analysis.owasp_zap()
                elif ask == "4":
                    print("\n[+] Nessus")
                    WEB_Application_Analysis.nessus()
                elif ask == "5":
                    print("\n[+] Sqlmap")
                    Exploitation_Tools.sqlmap()
                else:
                     break
                
        elif option == "6":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Exploitation")
                banner.description("Exploitation in bug bounty refers to the phase where a bug hunter attempts to leverage identified vulnerabilities to execute attacks on a target system. The objective is to demonstrate the practical impact of a vulnerability, such as gaining unauthorized access, escalating privileges, or exfiltrating sensitive data. This step often involves crafting and executing specific exploits to prove that the vulnerability can be used in a real-world scenario. Successful exploitation helps validate the severity of the vulnerability, guiding the target organization on necessary remediation actions.")
                list_root_attacks = ["Crackmapexec\t(Recommended)","Masscan","Beef\t\t(Recommended)","Social Engineering Toolkit","PowerSploit","Mimikatz\t\t(Recommended)","go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    print("\n[+] Crackmapexec")
                    Exploitation_Tools.crackmapexec()
                elif ask == "2":
                    print("\n[+] Masscan")
                    masscan()
                elif ask == "3":
                    print("\n[+] beef")
                    Exploitation_Tools.beef()
                elif ask == "4":
                    print("\n[+]Social Engineering Toolkit")
                    Password_Hacking.setoolkit()
                elif ask == "5":
                    print("\n[+]powersploit")
                    powersploit()               
                elif ask == "6":
                    print("\n[+]mimikatz")
                    mimikatz()                
                elif ask == "7":
                    print("\n[+]httpx-toolkit")
                    httpx_toolkit()         
                else:
                     break   

        elif option == "7":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Reporting Tools")
                banner.description("Reporting tools in bug bounty are specialized software or platforms that help bug hunters document and submit their findings to the target organization. These tools facilitate the structured reporting of vulnerabilities, including details such as the type of vulnerability, steps to reproduce it, potential impact, and suggested mitigations. ")
                list_root_attacks = ["Dradis","CherryTree\t\t(Recommended)","faradaystart","recordmydesktop ","pipal","maltego\t\t(Recommended)","go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    print("\n[+]Dradis")
                    dradis()               
                elif ask == "2":
                    print("\n[+]Cherrytree")
                    cherrytree()                
                elif ask == "3":
                    print("\n[+]faraday")
                    faraday()                    
                elif ask == "4":
                    print("\n[+]recordmydesktop")
                    recordmydesktop()                    
                elif ask == "5":
                    print("\n[+]pipal")
                    pipal ()               
                elif ask == "6":
                    print("\n[+] Maltego")
                    information_gathering.maltego()
                else:
                     break  
        else:
            return            

def recordmydesktop():
    os.system("clear")
    github ="recordmydesktop application produces an ogg-encapsulated theora-vorbis file. recordMyDesktop tries to be as unobstrusive as possible by proccessing only regions of the screen that have changed."
    template.template("recordmydesktop","recordmydesktop --help",github.strip(),{"How to record screencasts with recordMyDesktop":"https://opensource.com/business/15/11/how-record-screencasts","recordmydesktop Tool help file":"https://www.kali.org/tools/recordmydesktop/",})
                
def faraday():
    os.system("clear")
    github ="Faraday introduces a new concept (IPE) Integrated Penetration-Test Environment a multiuser Penetration test IDE. Designed for distribution, indexation and analysis of the generated data during the process of a security audit."  
    template.template("faraday","faraday --help",github.strip(),{"faraday Tool Documentation":"https://www.kali.org/tools/python-faraday/#tool-documentation","How to scan web sites with Faraday IDE on Kali Linux":"https://www.securityhardening.com/library/Article33.pdf",})
                
def cherrytree():
    os.system("clear")
    github ="CherryTree is a hierarchical note taking application, featuring rich text, syntax highlighting, images handling, hyperlinks, import/export with support for multiple formats, support for multiple languages, and more."
    template.template("cherrytree","cherrytree --help",github.strip(),{"How To Install cherrytree on Kali Linux":"https://installati.one/install-cherrytree-kalilinux/","Cherry tree General Commands Manual":"https://www.kali.org/tools/cherrytree/#tool-documentation",})
                
def dradis():
    os.system("clear")
    github ="Dradis is an open-source collaboration framework, tailored to InfoSec teams."
    template.template("dradis","dradis --help",github.strip(),{"dradis helpfile":"https://www.kali.org/tools/dradis/","Dradis: Reporting and Collaboration Tool":"https://www.hackingarticles.in/dradis-reporting-and-collaboration-tool/","dradis github":"https://github.com/dradis/dradis-ce",})
                
def pipal():
    os.system("clear")
    github ="On most internal pen-tests I do, I generally manage to get a password dump from the DC. To do some basic analysis on this I wrote Counter and since I originally released it I have made quite a few mods to it to generate extra stats that are useful when doing reports to management."
    template.template("pipal","pipal --help",github.strip(),{"pipal Help file":"https://www.kali.org/tools/pipal/#tool-documentation","Password Cracking Strategy: Using pipal to Determine Common Password Patterns":"https://www.hackers-arise.com/post/password-cracking-strategy-using-pipal-to-determine-password-patterns",})
                
def httpx_toolkit():
    os.system("clear")
    github ="httpx is a fast and multi-purpose HTTP toolkit allow to run multiple probers using retryablehttp library, it is designed to maintain the result reliability with increased threads."
    template.template("httpx-toolkit","httpx-toolkit --help",github.strip(),{"httpx-toolkit kali":"https://www.kali.org/tools/httpx-toolkit/","A Detailed Guide on httpx":"https://www.hackingarticles.in/a-detailed-guide-on-httpx/",})
                
def mimikatz():
    os.system("clear")
    github ="Mimikatz uses admin rights on Windows to display passwords of currently logged in users in plaintext."
    template.template("mimikatz","mimikatz --help",github.strip(),{"Mimikatz tutorial: How it hacks Windows passwords, credentials":"https://www.techtarget.com/searchsecurity/tutorial/Mimikatz-tutorial-How-it-hacks-Windows-passwords-credentials","What is Mimikatz? The Beginner's Guide":"https://www.varonis.com/blog/what-is-mimikatz","What Is Mimikatz? Everything You Need to Know":"https://www.cynet.com/network-attacks/mimikatz/",})
                
def powersploit():
    os.system("clear")
    github ="PowerSploit is a series of Microsoft PowerShell scripts that can be used in post-exploitation scenarios during authorized penetration tests."
    template.template("powersploit","powersploit --help",github.strip(),{"How to Use PowerSploit, Part 1 (Evading Antivirus Software)":"https://null-byte.wonderhowto.com/how-to/hack-like-pro-use-powersploit-part-1-evading-antivirus-software-0165535/",})
                
def dnsrecon():
    os.system("clear")
    github="DNSRecon is a Python port of a Ruby script that I wrote to learn the language and about DNS in early 2007.This time I wanted to learn about Python and extend the functionality of the original tool and in the process re-learn how DNS works and how could it be used in the process of a security assessment and network troubleshooting."
    template.template("dnsrecon","dnsrecon --help",github.strip(),{"dnsrecon Documentation":"https://www.kali.org/tools/dnsrecon/","DNSRecon: a powerful DNS reconnaissance tool":"https://securitytrails.com/blog/dnsrecon-tool","DNSRecon Cheat Sheet":"https://www.eccouncil.org/wp-content/uploads/2023/09/DNSRecon-Cheat-Sheet-3.pdf",})
                
                         
def unicorn():
    os.system("clear")
    github = "Unicornscan is a new information gathering and correlation engine built for and by members of the security research and testing communities. It was designed to provide an engine that is Scalable, Accurate, Flexible, and Efficient."
    template.template("unicornscan","unicornscan -h",github.strip(),{"Unicornscan Penetration Testing Tool in Kali Linux":"https://www.geeksforgeeks.org/unicornscan-penetration-testing-tool-in-kali-linux/","Reconnaissance with Unicornscan":"https://www.hackers-arise.com/post/2017/08/20/reconnaissance-with-unicornscan",})

def masscan():
    os.system("clear")
    github="MASSCAN is TCP port scanner which transmits SYN packets asynchronously and produces results similar to nmap, the most famous port scanner. Internally, it operates more like scanrand, unicornscan, and ZMap, using asynchronous transmission. It’s a flexible utility that allows arbitrary address and port ranges."
    template.template("masscan","masscan --help",github.strip(),{"masscan Documentation":"https://www.kali.org/tools/masscan/","Masscan -- 1000 Times Faster Than NMAP":"https://www.kalilinux.in/2020/09/masscan-1000-times-faster-than-nmap.html","Masscan Cheatsheet":"https://cheatsheet.haax.fr/network/port-scanning/masscan_cheatsheet/",})


if __name__ == "__main__":
    main()
