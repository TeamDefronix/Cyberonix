from main.tools import banner, colors, template,WEB_Application_Analysis,information_gathering
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
            print(colors.options, f"{i+1}) {list_attacks[i]}".title(), colors.reset)
        try:
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            return
        if option == "1":
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
                        colors.options, f"{i+1}) {list_attacks[i]}".title(), colors.reset
                    )
                try:
                    option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if option == "1":
                    os.system("clear")
                    WEB_Application_Analysis.owasp_zap()
                elif option == "2":
                    os.system("clear")
                    WEB_Application_Analysis.burp_suite()
                elif option == "3":
                    os.system("clear")
                    WEB_Application_Analysis.nikto()
                elif option == "4":
                    os.system("clear")
                    information_gathering.nmap()
                elif option == "5":
                    os.system("clear")
                    WEB_Application_Analysis.wapiti()
                elif option == "6":
                    os.system("clear")
                    WEB_Application_Analysis.nessus()
                elif option == "7":
                    os.system("clear")
                    WEB_Application_Analysis.nuclei()
                elif option == "8":
                    os.system("clear")
                    fiddler()                
                elif option == "9":
                    os.system("clear")
                    ptf()                
                else:
                    break

        elif option == "2":
            print("\n[+] Write-UPS")
            os.system("clear")
            template.template("Writeup","no-tools","Writeups",
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
                    "Session Hijacking: Danger on the Network - OWASP": "https://owasp.org/www-pdf-archive//Sessi%C3%B3n_Hijacking_Peligro_en_la_Red.pdf",
                    "Mastering Session Management - Siva Ram - PDF": "https://owasp.org/www-pdf-archive//Siva_Ram-Mastering_Session_Managment.pdf",
                    "Application Session Management Best Practices": "https://auth0.com/blog/application-session-management-best-practices/",
                },
                "Session Management Write-UPS",
            )

        elif option == "3":
            print("\n[+] Burp Extensions")
            os.system("clear")
            template.template("Burp Extensions","no-tools","Writeups",
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

def fiddler():
    github = github_getting_text(
                        "https://learn.microsoft.com/en-us/windows/win32/win7appqual/fiddler-web-debugger-tool/",
                        "p",
                        2,
                    )
    template.template(
                        "Fiddler",
                        "mono Fiddler.exe",
                        github.strip(),{
                            "Fiddler on Kali Linux":"https://techstarspace.engineer/2019/04/19/fiddler-on-kali-linux/",
                            "Fiddler In Action - Part 1":"https://www.mehdi-khalili.com/fiddler-in-action/part-1",
                            "Welcome to Fiddler Everywhere!":"https://docs.telerik.com/fiddler-everywhere/introduction",
                            
                        },
                       
                        method="github",
                        github_install="apt-get install mono-complete -y && wget http://telerik-fiddler.s3.amazonaws.com/fiddler/fiddler-linux.zip && unzip fiddler-linux.zip -d fiddler && rm -rf fiddler-linux.zip && cd fiddler",
                        github_check="fiddler",
                    )

def ptf():
    github = "The PenTesters Framework (PTF) is a Python script designed for Debian/Ubuntu/ArchLinux based distributions to create a similar and familiar distribution for Penetration Testing. PTF attempts to install all of your penetration testing tools (latest and greatest), compile them, build them, and make it so that you can install/update your distribution on any machine. Everything is organized in a fashion that is cohesive to the Penetration Testing Execution Standard (PTES) and eliminates a lot of things that are hardly used"
    template.template(
                        "PTF",
                        "./ptf",
                        github.strip(),
                       {
                           "The Penetration Testers Framework (PTF) - Is a Way for Modular Support for Up-to-date Tools ":"https://www.kitploit.com/2015/05/the-penetration-testers-framework-ptf.html?m=1",
                           "What is a Penetration Testing Framework?":"https://www.mitnicksecurity.com/blog/what-is-a-penetration-testing-framework",
                       },
                        method="github",
                        github_install="git clone https://github.com/trustedsec/ptf.git && cd ptf && pip install -r requirements.txt && chmod +x ptf ",
                        github_check="ptf",
                    )

if __name__ == "__main__":
    main()
