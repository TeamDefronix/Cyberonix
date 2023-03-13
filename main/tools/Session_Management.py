from main.tools import banner, colors, template,WEB_Application_Analysis
from main import Cheat_sheet
import os
import requests
from bs4 import BeautifulSoup


# main function
def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Session Management")
        list_attacks = ["Tools", "Writeups", "Burp Extensions", "Go Back"]
        for i in range(len(list_attacks)):
            print(colors.options, f"{i}) {list_attacks[i]}".title(), colors.reset)
        try:
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            template.exit_program()
        if option == "0":
            while True:
                print("\n[+] Tools")
                os.system("clear")
                banner.main()
                banner.attack("Tools")
                list_attacks = [
                    "OWASP ZAP",
                    "BurpSuite",
                    "Nikto",
                    "Nmap",
                    "Wapiti",
                    "Nessus",
                    "Nuclei",
                    "Fiddler",
                    "Penetration Testers Framework (PTF)",
                    "Go Back",
                ]
                for i in range(len(list_attacks)):
                    print(
                        colors.options, f"{i}) {list_attacks[i]}".title(), colors.reset
                    )
                try:
                    option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    template.exit_program()
                if option == "0":
                    os.system("clear")
                    # name,command,discription,writeup,link=True,method="kali",github_install="",github_check=True
                    github = "The OWASP Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications.\nIt is designed to be used by people with a wide range of security experience and as such is ideal for developers and functional testers who are new to penetration testing as well as being a useful addition to an experienced pen testers toolbox."
                    template.template(
                        "zaproxy",
                        "zaproxy > /dev/null 2>&1",
                        github.strip(),
                        {
                            "How to setup OWASP ZAP to scan your web application for security vulnerabilities": "https://www.linkedin.com/pulse/how-setup-owasp-zap-scan-your-web-application-security-botla/",
                            "Authenticated Scan using OWASP-ZAP": "https://medium.com/@secureica/authenticated-scan-using-owasp-zap-f0a71dafe41",
                            "OWASP ZAP: 6 Key Capabilities and a Quick Tutorial": "https://www.hackerone.com/knowledge-center/owasp-zap-6-key-capabilities-and-quick-tutorial",
                            "Initial Setup": "https://infosecgirls.gitbook.io/infosecgirls-training/v/appsec/initial-setup-with-owasp-zap/untitled",
                            "Setup OWASP ZAP": "https://infosecgirls.gitbook.io/infosecgirls-training/v/appsec/initial-setup-with-owasp-zap/setup-owasp-zap",
                        },
                    )
                elif option == "1":
                    os.system("clear")
                    WEB_Application_Analysis.burp_suite()
                elif option == "2":
                    os.system("clear")
                    github = github_getting_text(
                        "https://github.com/sullo/nikto/wiki/Overview-&-Description",
                        "p",
                        0,
                    )
                    template.template(
                        "nikto",
                        "nikto",
                        github.strip(),
                        {
                            "What is nikto and its usages": "https://www.geeksforgeeks.org/what-is-nikto-and-its-usages/",
                            "Nikto website vulnerability scanner": "https://securitytrails.com/blog/nikto-website-vulnerability-scanner",
                            "Nikto webserver scanner": "https://geekflare.com/nikto-webserver-scanner/",
                            "What is Nikto Tool in Kali and how to use it?": "https://www.cyber-today.com/what-is-nikto-tool-in-kali-and-how-to-use-it/",
                            "Basic Testing": "https://github.com/sullo/nikto/wiki/Basic-Testing",
                        },
                    )
                elif option == "3":
                    os.system("clear")
                    github = "Nmap (Network Mapper) is a network scanner created by Gordon Lyon (also known by his pseudonym Fyodor Vaskovich). Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses."
                    template.template(
                        "nmap",
                        "nmap",
                        github.strip(),
                        {
                            "Nmap Cheat-Sheet": "https://www.stationx.net/nmap-cheat-sheet/",
                            "Official website": "https://nmap.org/ ",
                            "Other resources": "https://linux.die.net/man/1/nmap",
                        },
                    )
                elif option == "4":
                    os.system("clear")
                    github = github_getting_text(
                        "https://github.com/wapiti-scanner/wapiti", 'p[dir="auto"]', 6
                    )
                    template.template(
                        "wapiti",
                        "wapiti -h | head -30",
                        github.strip(),
                        {
                            "wapiti free web application vulnerability scanner": "https://pentestit.medium.com/wapiti-free-web-application-vulnerability-scanner-ce7712adf644",
                            "Official docs": "https://github.com/wapiti-scanner/wapiti",
                            "wapiti tutorial": "https://www.kalilinux.in/2021/01/wapiti-tutorial.html",
                            "complete guide to using wapiti web vulnerability scanner to keep your web applications websites secure": "https://linuxsecurity.com/features/complete-guide-to-using-wapiti-web-vulnerability-scanner-to-keep-your-web-applications-websites-secure",
                        },
                    )
                elif option == "5":
                    os.system("clear")
                    github = github_getting_text(
                        "https://www.techtarget.com/searchnetworking/definition/Nessus",
                        'section[id="content-body"]',
                        0,
                    )
                    template.template(
                        "nessus",
                        "nessus",
                        github.strip(),
                        {
                            "How To: Run Your First Vulnerability Scan with Nessus": "https://www.tenable.com/blog/how-to-run-your-first-vulnerability-scan-with-nessus",
                            "A brief introduction to the Nessus vulnerability scanner": "https://resources.infosecinstitute.com/topic/a-brief-introduction-to-the-nessus-vulnerability-scanner/",
                            "Beginner’s Guide to Nessus": "https://www.hackingarticles.in/beginners-guide-to-nessus/",
                            "Nessus Ubuntu Installation and Tutorial": "https://linuxhint.com/nessus-ubuntu-installation-tutorial/",
                        },
                        link="https://www.tenable.com/downloads/api/v2/pages/nessus/files/Nessus-10.4.2-debian9_amd64.deb",
                        method="deb",
                    )
                elif option == "6":
                    os.system("clear")
                    github = github_getting_text(
                        "https://github.com/projectdiscovery/nuclei", 'p[dir="auto"]', 3
                    )
                    template.template(
                        "nuclei",
                        "nuclei --help",
                        github.strip(),
                        {
                            "Nuclei - Automated Vulnerability Scanning Tool": "https://allabouttesting.org/nuclei-automated-vulnerability-scanning-tool/",
                            "Nuclei – Fast and Customizable Vulnerability Scanner": "https://www.geeksforgeeks.org/nuclei-fast-and-customizable-vulnerability-scanner/",
                            "Gauing+Nuclei for Instant Bounties": "https://infosecwriteups.com/gauing-nuclei-for-instant-bounties-7a8a07979fff ",
                            "DevSecOps 101 Part 3: Scanning Live Web Applications with Nuclei": "https://escape.tech/blog/devsecops-part-iii-scanning-live-web-applications",
                        },
                    )
                elif option == "7":
                    os.system("clear")
                    github = github_getting_text(
                        "https://learn.microsoft.com/en-us/windows/win32/win7appqual/fiddler-web-debugger-tool/",
                        "p",
                        2,
                    )
                    template.template(
                        "Fiddler",
                        "mono Fiddler.exe",
                        github.strip(),
                        "no-writeups",
                        method="github",
                        github_install="apt-get install mono-complete -y && wget http://telerik-fiddler.s3.amazonaws.com/fiddler/fiddler-linux.zip && unzip fiddler-linux.zip -d fiddler",
                        github_check="fiddler",
                    )
                elif option == "8":
                    os.system("clear")
                    github = "The PenTesters Framework (PTF) is a Python script designed for Debian/Ubuntu/ArchLinux based distributions to create a similar and familiar distribution for Penetration Testing. PTF attempts to install all of your penetration testing tools (latest and greatest), compile them, build them, and make it so that you can install/update your distribution on any machine. Everything is organized in a fashion that is cohesive to the Penetration Testing Execution Standard (PTES) and eliminates a lot of things that are hardly used"
                    template.template(
                        "Penetration Testers Framework (PTF)",
                        "chmod +x ptf && ./ptf",
                        github.strip(),
                        "no-writeups",
                        method="github",
                        github_install="git clone https://github.com/trustedsec/ptf.git",
                        github_check="ptf",
                    )
                else:
                    break

        elif option == "1":
            os.system("clear")
            banner.main()
            Cheat_sheet.cheat(
                {
                    "Session Management - Authgear": "https://www.authgear.com/post/session-management",
                    "OWASP Session Management Cheat Sheet": "https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html",
                    "Session Management Overview - Secure Coding": "https://www.securecoding.com/blog/session-management-an-overview/",
                    "Session Management Best Practices - Packetlabs": "https://www.packetlabs.net/posts/session-management/",
                    "HTTP Sessions - MDN Web Docs": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Session",
                    "Attacking Session Management with Burp Suite": "https://portswigger.net/support/using-burp-to-attack-session-management",
                    "Session Management Lecture Notes - Stanford": "https://crypto.stanford.edu/cs155old/cs155-spring16/lectures/10-SessionMgmt.pdf",
                    "Broken Authentication and Session Management - Crashtest Security": "https://crashtest-security.com/broken-authentication-and-session-management/",
                    "Preventing Security Voids in Web Applications - SANS Institute": "https://sansorg.egnyte.com/dl/CmpHWTzrja",
                    "PHP Session Security Management - PHP.net": "https://www.php.net/manual/en/features.session.security.management.php",
                    "Session Management in ColdFusion - CFDocs": "https://cfdocs.org/security-session-management",
                    "Comprehensive Guide on Broken Authentication and Session Management - Hacking Articles": "https://hackingarticles.in/comprehensive-guide-on-broken-authentication-session-management/",
                    "What is Session Management? - Clerk.dev": "https://clerk.dev/blog/what-is-session-management",
                    "All You Need to Know About User Session Security - SuperTokens": "https://supertokens.com/blog/all-you-need-to-know-about-user-session-security",
                    "How to Secure Authentication, Session Management, and Access Control Systems of Your Web Applications - Vaadata": "https://www.vaadata.com/blog/how-to-secure-authentication-session-management-and-access-control-systems-of-your-web-applications/",
                    "Understanding Session Management - Coveros": "https://www.coveros.com/understanding-session-management-one-of-owasp-top-10-part-1/",
                    "Broken Authentication and Session Management Tips - Hacklido": "https://hacklido.com/blog/207-broken-authentication-and-session-management-tips",
                    "Web Security Session Management Slide": "https://slideplayer.com/slide/5689194/#.XFSQwUKWre4.twitter",
                    "Attacking Session Management - OWASP": "https://owasp.org/www-pdf-archive//Attacking_Session_Management_-_Alexandre_Villas.pdf",
                    "Improving the Security of Session Management in Web Applications - OWASP": "https://owasp.org/www-pdf-archive//Improving_the_Security_of_Session_Management_in_Web_Applications_-_Philippe_De_Ryck.pdf",
                    "Session Management - OWASP 2011": "https://owasp.org/www-pdf-archive//OWASP_2011_-_Slawomir_Rozbicki_-_Session_Managemnt.pdf",
                    "Session Fixation - OWASP AppSec Research 2010": "https://owasp.org/www-pdf-archive//OWASP_AppSec_Research_2010_Session_Fixation_by_Schrank_Braun_Johns_and_Poehls.pdf",
                    "SAP Session (Fixation) Attacks and Protections - OWASP": "https://owasp.org/www-pdf-archive//SAP-Session_(Fixation)_Attacks_and_Protections-OWASP-RaulSiles_Taddong.pdf",
                    "Session Hijacking: Danger on the Network - OWASP": "https://owasp.org/www-pdf-archive//Sessi%C3%B3n_Hijacking_Peligro_en_la_Red.pdf",
                    "Mastering Session Management - Siva Ram - PDF": "https://owasp.org/www-pdf-archive//Siva_Ram-Mastering_Session_Managment.pdf",
                    "Application Session Management Best Practices": "https://auth0.com/blog/application-session-management-best-practices/",
                },
                "Session Management Write-UPS",
            )

        elif option == "2":
            print("\n[+] Burp Extensions")
            os.system("clear")
            banner.main()
            Cheat_sheet.cheat(
                {
                    "PortSwigger - Session Timeout Test": "https://portswigger.net/bappstore/c4bfd29882974712a1d69c6d8f05874e",
                    "PortSwigger - CSRF Scanner": "https://portswigger.net/bappstore/60f172f27a9b49a1b538ed414f9f27c3",
                    "PortSwigger - Token Extractor": "https://portswigger.net/bappstore/f24211fa6fcd4bbea6b21f99c5cad27a",
                    "PortSwigger - Headers Analyzer": "https://portswigger.net/bappstore/8b4fe2571ec54983b6d6c21fbfe17cb2",
                    "PortSwigger - J2EE Scan": "https://portswigger.net/bappstore/7ec6d429fed04cdcb6243d8ba7358880",
                    "PortSwigger - CO2": "https://portswigger.net/bappstore/c5071c7a7e004f72ae485e8a72911afc",
                    "PortSwigger - WS Security": "https://portswigger.net/bappstore/i5431k07za13636g0o9a1733ke7h10g3",
                    "PortSwigger - JWT Editor": "https://portswigger.net/bappstore/26aaa5ded2f74beea19e2ed8345a93dd",
                    "Github - WS-Attacker": "https://github.com/RUB-NDS/WS-Attacker",
                    "Github - logger++": "https://github.com/PortSwigger/logger-plus-plus",
                },
                "Session Management Burp Extensions",
            )

        else:
            return


def github_getting_text(link, selector, indexvalue):
    print("Please Wait....\r", end="")
    URL = link
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, "html.parser")
        paras = soup.select(selector)
        # check index value from test file
        return paras[indexvalue].text
    except:
        return f"{colors.red}Not Loaded Because No Internet Connection{colors.reset}"


if __name__ == "__main__":
    main()
