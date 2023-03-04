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
        banner.attack("Risky Functionality Card Payment")
        list_attacks = ["Tools", "Writeups", "Go Back"]
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
                    "Sqlmap",
                    "Fiddler",
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
                elif option == "5":
                    os.system("clear")
                    github = github_getting_text(
                        "https://learn.microsoft.com/en-us/windows/win32/win7appqual/fiddler-web-debugger-tool/",
                        "p",
                        2,
                    )
                    template.template(
                        "Fiddler",
                        "chmod u+x fiddler-everywhere-4.1.2.AppImage && su -c ./fiddler-everywhere-4.1.2.AppImage $SUDO_USER > /dev/null 2>&1",
                        github.strip(),
                        "no-writeups",
                        method="github",
                        github_install="wget -q --show-progress https://downloads.getfiddler.com/linux/fiddler-everywhere-4.1.2.AppImage && mkdir Fiddler_Everywhere && mv fiddler-everywhere-4.1.2.AppImage Fiddler_Everywhere",
                        github_check="Fiddler_Everywhere",
                    )
                elif option == "6":
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
                elif option == "7":
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
                    "Exploiting Payment Gateways": "https://vasuyadav0786.medium.com/exploiting-payment-gateways-97ce7af5a9cf",
                    "Let's Break Into Payment Gateways": "https://infosecwriteups.com/lets-break-into-payment-gateways-fc52523eeaca",
                    "Common Vulnerabilities in Payment Functionality": "https://dl.packetstormsecurity.net/papers/general/common-vulnerabilities.pdf",
                    "Bug Bounty Response Manipulation Leading to Payment Bypass": "https://infosecwriteups.com/bug-bounty-response-manipulation-leading-to-payment-bypass-cb5fde360b1a",
                    "Web Application Security Testing - Testing Payment Functionality": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/10-Test-Payment-Functionality",
                    "Application Security Testing Techniques - Testing Payment Functionality": "https://www.softwaretestinghelp.com/how-to-test-application-security-web-and-desktop-application-security-testing-techniques/",
                    "Parameter Tampering Vulnerability Using 3 Different Approaches": "https://www.cobalt.io/blog/parameter-tampering-vulnerability-using-3-different-approaches",
                    "Webinar: Understanding Payment Gateway Related Vulnerabilities": "https://www.youtube.com/watch?v=oin2fplOazU",
                    "Payment Gateway Security Measures Overview": "https://yashsali7.medium.com/an-overview-of-security-measures-used-in-payment-gateways-86375eb12364",
                    "Payment Bypass Vulnerability on BigBasket": "https://medium.com/@ranjeetjagtap25/payment-bypass-vulnerability-on-bigbasket-2aab137e9631",
                    "Security Features of Payment Gateway": "https://www.ukessays.com/essays/information-technology/security-features-of-payment-gateway-information-technology-essay.php",
                    "Vulnerabilities in Electronic Payment Systems (EPS)": "https://www.linkedin.com/pulse/vulnerabilities-eps-electronic-payment-systems-from-david-joao-",
                    "Security Threats to E-Commerce": "https://www.javatpoint.com/security-threat-to-e-commerce",
                    "Visa's 3-D Secure Secure Online Payment Authentication": "https://www.giac.org/paper/gsec/4380/visa-039-s-3-d-secure-secure-online-payment-authentication/107245",
                    "Researching Xiaomi's TEE": "https://research.checkpoint.com/2022/researching-xiaomis-tee/",
                    "JazzCash Payment Gateway in PHP (Prevent Amount Tampering)": "https://www.youtube.com/watch?v=JEvYSlwb-yY",
                },
                " Risky Functionality Payment Systems Write-UPS",
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
