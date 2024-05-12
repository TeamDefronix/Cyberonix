from main.tools import banner, colors, template,Session_Management,information_gathering,WEB_Application_Analysis,Vulnerability_Analysis,Exploitation_Tools,Password_Hacking
import os
import requests
from bs4 import BeautifulSoup


# main function
def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Authorization")
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
                    " Burp Suite",
                    " Wireshark",
                    " OWASP ZAP",
                    " Nessus",
                    " Hydra",
                    " BeEF",
                    " Sqlmap",
                    " Metasploit",
                    " Nmap",
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
                    WEB_Application_Analysis.burp_suite()
                elif option == "2":
                    os.system("clear")
                    Vulnerability_Analysis.wireshark()
                elif option == "3":
                    os.system("clear")
                    WEB_Application_Analysis.owasp_zap()
                elif option == "4":
                    os.system("clear")
                    WEB_Application_Analysis.nessus()
                elif option == "5":
                    os.system("clear")
                    Password_Hacking.hydra()
                elif option == "6":
                    os.system("clear")
                    Exploitation_Tools.beef()
                elif option == "7":
                    os.system("clear")
                    Exploitation_Tools.sqlmap()
                elif option == "8":
                    os.system("clear")
                    Exploitation_Tools.metasploit()
                elif option == "9":
                    os.system("clear")
                    information_gathering.nmap()
                elif option == "10":
                    os.system("clear")
                    Session_Management.ptf()
                else:
                    break
        elif option == "2":
            print("\n[+] Write-UPS")
            os.system("clear")
            template.template("Writeup","no-tools","Writeups",
                {
                    " Securing Applications with Better User Authorization": "https://medium.com/capital-one-tech/securing-applications-with-better-user-authorization-625ec07a7001",
                    " Access Control": "https://portswigger.net/web-security/access-control",
                    " Web Security: Authentication & Authorization": "https://coderstower.com/2020/03/23/web-security-authentication-authorization/",
                    " Authentication & Authorization in Web Apps": "https://blog.jscrambler.com/authentication-authorization-in-web-apps",
                    " Session IDs - OWASP": "https://www.cgisecurity.com/lib/SessionIDs.pdf",
                    " JWT Authorization in Web Applications": "https://concisesoftware.com/blog/jwt-authorization-in-web-applications/",
                    " Insecure Authorization": "https://www.appsealing.com/insecure-authorization/",
                    " OAuth Vulnerabilities: Implementing Secure Authorization in Your Web Application": "https://medium.com/swlh/oauth-vulnerabilities-implementing-secure-authorization-in-your-web-application-3b9517b34798",
                    " OWASP Top 10 - Broken Access Control": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/",
                    "Broken Authorization Vulnerability": "https://knowledge-base.secureflag.com/vulnerabilities/broken_authorization/broken_authorization_vulnerability.html",
                    "OWASP Web Security Testing Guide - Authorization Testing": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/README",
                    "Web Authentication & Authorization": "https://www.slideshare.net/alex_pasaila/web-authentication-authorization-10930449",
                    "Web Security - Authorization": "https://www3.rocketsoftware.com/rocketd3/support/documentation/Uniface/10/uniface/webApps/webSecurity/webSecurity_Authorization.htm",
                    "Authorization Best Practices": "https://goteleport.com/blog/authorization-best-practices/",
                    "Secure Your Web Application with Spring Security - Identify How to Secure Access to an App Using Authentication and Authorization": "https://openclassrooms.com/en/courses/5683681-secure-your-web-application-with-spring-security/6695816-identify-how-to-secure-access-to-an-app-using-authentication-and-authorization",
                    "Preventing Broken Access Control": "https://crashtest-security.com/broken-access-control-prevention/",
                    "Preventing Broken Access Control - The No. 1 Vulnerability in the OWASP Top 10 2021": "https://www.synack.com/blog/preventing-broken-access-control-the-no-1-vulnerability-in-the-owasp-top-10-2021/",
                    "A Step-by-Step Guide to Broken Access Control Attacks": "https://www.polar.security/post/a-step-by-step-guide-to-broken-access-control-attacks",
                    "Broken-Access-Control - packetlabs": "https://www.packetlabs.net/posts/broken-access-control",
                    "Broken-Access-Control - qawerk": "https://qawerk.com/blog/broken-access-control/",
                    "Testing for Broken Authentication in Web Apps": "https://www.section.io/engineering-education/testing-for-broken-authentication-in-web-apps/",
                    "Broken-Access-Control (javascript) - Snyk": "https://learn.snyk.io/lessons/broken-access-control/javascript/",
                    "JSON Web Tokens Decoder - JWT.IO": "https://jwt.io/",
                    "Authorization Code Grant - Zine": "https://pbs.twimg.com/media/Et2T02KVcAEONV0?format=jpg&name=large",
                    "OWASP API1: 2019 – Broken Object Level Authorization": "https://securityboulevard.com/2023/02/owasp-api1-2019-broken-object-level-authorization/",
                    "BOLA: 3-Digit Bounty from Topcoder": "https://infosecwriteups.com/what-is-bola-3-digit-bounty-from-topcoder-a25e7fae0d64",
                    "Broken Function Level Authorization (API Security) 0x2": "https://infosecwriteups.com/broken-function-level-authorization-api-security-0x2-23a6d7c1aa46",
                    "A Deep Dive on the Most Critical API Vulnerability: BOLA": "https://inonst.medium.com/a-deep-dive-on-the-most-critical-api-vulnerability-bola-1342224ec3f2",
                    "Broken Object Level Authorization (BOLA) - NordiAPIs": "https://nordicapis.com/what-is-broken-object-level-authorization-and-how-to-fix-it/",
                    "Broken Function Level Authorization Leads to Disclosing PII Information of All Company Users": "https://webresearcher007.medium.com/broken-function-level-authorization-leads-to-disclosing-pii-information-of-all-company-users-35aee60b287b",
                },
                "Authorization Write-UPS",
            )

        elif option == "3":
            print("\n[+] Burp Extensions")
            os.system("clear")
            banner.main()
            template.template("Burp Extensions","no-tools","Writeups",
                {
                    " Portswigger - Auth Analyzer": "https://portswigger.net/bappstore/7db49799266c4f85866f54d9eab82c89",
                    " Github - Auth Analyzer": "https://github.com/simioni87/auth_analyzer",
                    " Portswigger - AutoRepeater": "https://portswigger.net/bappstore/f89f2837c22c4ab4b772f31522647ed8",
                    " Github - AutoRepeater": "https://github.com/nccgroup/AutoRepeater",
                    " Github - Burp-SessionAuthTool": "https://github.com/thomaspatzke/Burp-SessionAuthTool",
                    " Github - BurpAuthzPlugin": "https://github.com/wuntee/BurpAuthzPlugin",
                    " Github - Burp-uuid": "https://github.com/silentsignal/burp-uuid",
                    " Github - Autorize": "https://github.com/Quitten/Autorize",
                    " Github - AuthMatrix": "https://github.com/SecurityInnovation/AuthMatrix",
                    "Github - Burplay": "https://github.com/SpiderLabs/burplay",
                    "Github - Param-Miner": "https://github.com/PortSwigger/param-miner",
                    "Portswigger - SAML Raider": "https://portswigger.net/bappstore/c61cfa893bb14db4b01775554f7b802e",
                    "Portswigger - Authz": "https://portswigger.net/bappstore/4316cc18ac5f434884b2089831c7d19e",
                },
                "Authorization Burp Extensions",
            )

        else:
            return


if __name__ == "__main__":
    main()
