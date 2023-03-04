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
        banner.attack("Authorization")
        list_attacks = ["Tools", "Writeups", "Burp Extensions", "Go Back"]
        for i in range(len(list_attacks)):
            print(colors.options, f"{i}) {list_attacks[i]}".title(), colors.reset)
        option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        if option == "0":
            while True:
                print("\n[+] Tools")
                os.system("clear")
                banner.main()
                banner.attack("Tools")
                list_attacks = [
                    "Burp Suite",
                    "Wireshark",
                    "OWASP ZAP",
                    "Nessus",
                    "Hydra",
                    "BeEF",
                    "Sqlmap",
                    "Metasploit",
                    "Nmap",
                    "Penetration Testers Framework (PTF)",
                    "Go Back",
                ]
                for i in range(len(list_attacks)):
                    print(
                        colors.options, f"{i}) {list_attacks[i]}".title(), colors.reset
                    )
                option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                if option == "0":
                    os.system("clear")
                    WEB_Application_Analysis.burp_suite()
                elif option == "1":
                    os.system("clear")
                    github = "Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis, software and communications protocol development, and education. It can be used to examine data from a live network or from a previously saved capture file. Wireshark provides a graphical user interface (GUI) for capturing and analyzing network traffic."
                    template.template(
                        "wireshark",
                        "wireshark",
                        github.strip(),
                        {
                            "Wireshark Cheat-Sheet": "https://www.comparitech.com/net-admin/wireshark-cheat-sheet",
                            "What-is-Wireshark-and-How-to-Use-it": "https://www.comptia.org/content/articles/what-is-wireshark-and-how-to-use-it ",
                            "Video Resource Wireshark": "https://www.youtube.com/playlist?list=PLBf0hzazHTGPgyxeEj_9LBHiqjtNEjsgt",
                        },
                    )
                elif option == "2":
                    os.system("clear")
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
                elif option == "3":
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
                elif option == "4":
                    os.system("clear")
                    github_p1 = github_getting_text(
                        "https://www.kali.org/tools/hydra/", "p", 2
                    )
                    github_p2 = github_getting_text(
                        "https://www.kali.org/tools/hydra/", "p", 3
                    )
                    github_p3 = github_getting_text(
                        "https://www.kali.org/tools/hydra/", "p", 4
                    )
                    github = github_p1 + github_p2 + github_p3
                    template.template(
                        "hydra",
                        "hydra",
                        github.strip(),
                        {
                            "How to use the hydra for password cracking": "https://www.techtarget.com/searchsecurity/tutorial/How-to-use-the-Hydra-password-cracking-tool",
                            "Hydra Tool For Brute- force attack": "https://systemweakness.com/hydra-tool-for-brute-force-attack-72653db7abe9?gi=efe05fea34af",
                        },
                    )
                elif option == "5":
                    os.system("clear")
                    github_p1 = github_getting_text(
                        "https://github.com/beefproject/beef", 'p[dir="auto"]', 2
                    )
                    github_p2 = github_getting_text(
                        "https://github.com/beefproject/beef", 'p[dir="auto"]', 3
                    )
                    github = github_p1 + github_p2
                    template.template(
                        "beef-xss",
                        "beef-xss",
                        github.strip(),
                        {
                            "BEeF Hacking Framework Tutorial [5 Easy Steps]": "https://www.golinuxcloud.com/beef-hacking-framework-tutorial/",
                            "Browser Exploitation and Advanced Threat Actors: An Overview of BeEF": "https://medium.com/@andrearebora/browser-exploitation-and-advanced-threat-actors-an-overview-of-beef-bb907a5b73fa",
                            "Hooking victims to Browser Exploitation Framework (BeEF) using Reflected and Stored XSS.": "https://medium.com/@secureica/hooking-victims-to-browser-exploitation-framework-beef-using-reflected-and-stored-xss-859266c5a00a",
                            "Hijacking Browser with BeEF Framework": "https://medium.com/@krunalkumarpatel/hijacking-browser-with-beef-framework-bea784c03149",
                        },
                    )
                elif option == "6":
                    os.system("clear")
                    github = github_getting_text("https://sqlmap.org/", "p", 0)
                    template.template(
                        "sqlmap",
                        "sqlmap -h",
                        github.strip(),
                        {
                            "Usage Of Sqlmap": "https://github.com/sqlmapproject/sqlmap/wiki/Usage",
                            "How to use SQLMAP to test a website for SQL Injection vulnerability": "https://www.geeksforgeeks.org/use-sqlmap-test-website-sql-injection-vulnerability/",
                            "How to Use SQLMap to Find Database Vulnerabilities": "https://www.freecodecamp.org/news/how-to-protect-against-sql-injection-attacks/",
                            "SQLMap - Cheetsheat": "https://book.hacktricks.xyz/pentesting-web/sql-injection/sqlmap",
                        },
                    )
                elif option == "7":
                    os.system("clear")
                    github = "The Metasploit Framework is an open-source tool for developing and executing exploit code against a remote target machine. It can be used to test the security of a computer system by finding and exploiting vulnerabilities. The framework includes a large collection of exploit modules, as well as various tools for payload generation, post-exploitation, and more. It can be used by security professionals for penetration testing, as well as by attackers for malicious purposes."
                    template.template(
                        "metasploit-framework",
                        "msfconsole",
                        github.strip(),
                        {
                            "Msf-Community-Post-Exploitation": "https://www.offensive-security.com/metasploit-unleashed/msf-community-post-exploitation",
                            "Post Exploitation In Linux With Metasploit": "https://pentestlab.blog/2013/01/04/post-exploitation-in-linux-with-metasploit/",
                            "Privilege Escalation (Metasploit Unleashed)": "https://www.offensive-security.com/metasploit-unleashed/privilege-escalation/",
                            "Post Exploitation Metasploit Modules (Reference)": "https://www.infosecmatter.com/post-exploitation-metasploit-modules-reference",
                            "PSExec Pass the Hash (Horizontal Escalation)": "https://www.offensive-security.com/metasploit-unleashed/psexec-pass-hash/",
                            "ms10_002_aurora (Vertical Escalation)": "https://www.offensive-security.com/metasploit-unleashed/privilege-escalation/",
                            "ms10_002_aurora (Horizontal Escalation)": "https://www.offensive-security.com/metasploit-unleashed/pivoting/ ",
                            "jtr_crack_fast (Hash Cracking)": "https://www.offensive-security.com/metasploit-unleashed/john-ripper/",
                            "warftpd_165_user (Keylogging)": "https://www.offensive-security.com/metasploit-unleashed/keylogging/",
                            "3proxy (Backdoor)": "https://www.offensive-security.com/metasploit-unleashed/meterpreter-backdoor/",
                            "persistence.rb (Persistent Backdoor)": "https://www.offensive-security.com/metasploit-unleashed/meterpreter-service/",
                            "Enabling Remote Desktop": "https://www.offensive-security.com/metasploit-unleashed/enabling-remote-desktop/",
                            "Post Exploitation in Linux with Metasploit": "https://pentestlab.blog/2013/01/04/post-exploitation-in-linux-with-metasploit/",
                            "Post Exploitation Metasploit Modules Reference": "https://www.infosecmatter.com/post-exploitation-metasploit-modules-reference/",
                            "Hack Like Pro: Kill and Disable Antivirus Software Remote PC": "https://null-byte.wonderhowto.com/how-to/hack-like-pro-kill-and-disable-antivirus-software-remote-pc-0141906/",
                            "Armitage Post Exploitation": "https://www.offensive-security.com/metasploit-unleashed/armitage-post-exploitation/",
                            "Setup Armitage as a Command & Control Framework for Free": "https://infosecwriteups.com/setup-armitage-as-a-command-control-c2-framework-for-free-bae590064817",
                            "Event Log Management": "https://www.offensive-security.com/metasploit-unleashed/event-log-management",
                            "Interacting with the Registry": "https://www.offensive-security.com/metasploit-unleashed/interacting-registry",
                        },
                    )
                elif option == "8":
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
                elif option == "9":
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
                    "Securing Applications with Better User Authorization": "https://medium.com/capital-one-tech/securing-applications-with-better-user-authorization-625ec07a7001",
                    "Access Control": "https://portswigger.net/web-security/access-control",
                    "Web Security: Authentication & Authorization": "https://coderstower.com/2020/03/23/web-security-authentication-authorization/",
                    "Authentication & Authorization in Web Apps": "https://blog.jscrambler.com/authentication-authorization-in-web-apps",
                    "Session IDs - OWASP": "https://www.cgisecurity.com/lib/SessionIDs.pdf",
                    "JWT Authorization in Web Applications": "https://concisesoftware.com/blog/jwt-authorization-in-web-applications/",
                    "Insecure Authorization": "https://www.appsealing.com/insecure-authorization/",
                    "OAuth Vulnerabilities: Implementing Secure Authorization in Your Web Application": "https://medium.com/swlh/oauth-vulnerabilities-implementing-secure-authorization-in-your-web-application-3b9517b34798",
                    "OWASP Top 10 - Broken Access Control": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/",
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

        elif option == "2":
            print("\n[+] Burp Extensions")
            os.system("clear")
            banner.main()
            Cheat_sheet.cheat(
                {
                    "Portswigger - Auth Analyzer": "https://portswigger.net/bappstore/7db49799266c4f85866f54d9eab82c89",
                    "Github - Auth Analyzer": "https://github.com/simioni87/auth_analyzer",
                    "Portswigger - AutoRepeater": "https://portswigger.net/bappstore/f89f2837c22c4ab4b772f31522647ed8",
                    "Github - AutoRepeater": "https://github.com/nccgroup/AutoRepeater",
                    "Github - Burp-SessionAuthTool": "https://github.com/thomaspatzke/Burp-SessionAuthTool",
                    "Github - BurpAuthzPlugin": "https://github.com/wuntee/BurpAuthzPlugin",
                    "Github - Burp-uuid": "https://github.com/silentsignal/burp-uuid",
                    "Github - Autorize": "https://github.com/Quitten/Autorize",
                    "Github - AuthMatrix": "https://github.com/SecurityInnovation/AuthMatrix",
                    "Github - Burplay": "https://github.com/SpiderLabs/burplay",
                    "Github - Param-Miner": "https://github.com/PortSwigger/param-miner",
                    "Portswigger - SAML Raider": "https://portswigger.net/bappstore/c61cfa893bb14db4b01775554f7b802e",
                    "Portswigger - Authz": "https://portswigger.net/bappstore/4316cc18ac5f434884b2089831c7d19e",
                },
                "Authorization Burp Extensions",
            )

        else:
            return


def github_getting_text(link, selector, indexvalue):
    print("Please Wait....\r", end="")
    URL = link
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, "html5lib")
        paras = soup.select(selector)
        # check index value from test file
        return paras[indexvalue].text
    except:
        return f"{colors.red}Not Loaded Because No Internet Connection{colors.reset}"


if __name__ == "__main__":
    main()
