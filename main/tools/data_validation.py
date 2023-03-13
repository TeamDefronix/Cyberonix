from bs4 import BeautifulSoup
from main.tools import banner, template, writeup,colors
import os
import requests
from bs4 import BeautifulSoup


def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Data Validation Vulnerabilities")
        list_vulns = [
            "XSS",
            "XXE - XML",
            "HTML Injection",
            "SQL Injection",
            "Command Injection",
            "HTTP Smuggling",
            "HTTP Parameter Pollution",
            "Open Redirection",
            "LFI",
            "Go Back",
        ]
        for i in range(len(list_vulns)):
            print(colors.options, f"{i}) {list_vulns[i]}".title(), colors.reset)
        try:
            vulns = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            template.exit_program()
        if vulns == "0":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("XSS")
                # name,command,discription,writeups,link="",method="kali",github_install="",github_check=""
                ask = vuln_options()
                if ask == "1":
                    while True:
                        os.system("clear")
                        banner.main()
                        banner.attack("XSS")
                        des = "It is recommended to test manually for XSS vulnerability to get better understanding & results.\nCheck out the writeup section to to learn about Cross Site Scripting"
                        banner.description(des)
                        list_tools = ["Dalfox", "XSStrike", "Xsser", "go back"]
                        for i in range(len(list_tools)):
                            print(
                                colors.options,
                                f"{i}) {list_tools[i]}".title(),
                                colors.reset,
                            )
                        option = input(
                            f"\n {colors.select}Select an Option ->{colors.reset} "
                        )
                        if option == "0":
                            print("\n[+] Dalfox")
                            github = github_getting_text(
                                "https://github.com/hahwul/dalfox", 'p[dir="auto"]', 1
                            )
                            template.template(
                                "dalfox",
                                "dalfox -h",
                                github.strip(),
                                {
                                    "DalFox - Parameter Analysis and XSS Scanning tool": "https://www.geeksforgeeks.org/dalfox-parameter-analysis-and-xss-scanning-tool/",
                                    "Automating XSS using Dalfox, GF and Waybackurls": "https://infosecwriteups.com/automating-xss-using-dalfox-gf-and-waybackurls-bc6de16a5c75",
                                    "Dalfox - Hacker Tools: XSS Scanning Made Easy": "https://blog.intigriti.com/2021/09/14/hacker-tools-dalfox/",
                                    "Offensive Security Tool: Dalfox": "https://www.blackhatethicalhacking.com/tools/dalfox",
                                },
                                link="github.com/hahwul/dalfox/v2@latest",
                                method="go",
                            )
                        elif option == "1":
                            print("\n[+] XSStrike")
                            github = github_getting_text(
                                "https://github.com/s0md3v/XSStrike", "p[dir=auto]", 3
                            )
                            template.template(
                                "XSStrike",
                                "python3 xsstrike.py -h",
                                github.strip(),
                                {
                                    "XSStrike – Hunting for low-hanging fruits in Kali Linux": "https://www.geeksforgeeks.org/xsstrike-hunting-for-low-hanging-fruits-in-kali-linux/",
                                    "Hacker tools: XSStrike – Hunting for low-hanging fruits.": "https://blog.intigriti.com/2021/06/29/hacker-tools-xsstrike-hunting-for-low-hanging-fruits/",
                                    "XSS Tools - XSStrike": "https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting/xss-tools",
                                    "XSStrike Usage Example (v3.x)": "https://www.cyberpunk.rs/xsstrike-usage-example-v3-x",
                                    "Advanced XSS Detection Suite – XSStrike": "https://www.cyberpunk.rs/advanced-xss-detection-suite-xsstrike",
                                },
                                link="https://github.com/s0md3v/XSStrike.git",
                                method="github",
                                github_install="git clone https://github.com/s0md3v/XSStrike.git",
                                github_check="XSStrike",
                            )
                        elif option == "2":
                            print("\n[+] Xsser")
                            github = github_getting_text(
                                "https://www.kali.org/tools/xsser/", "p", 3
                            )
                            template.template(
                                "xsser",
                                "xsser -h",
                                github.strip(),
                                {
                                    "Detecting and Exploiting XSS Injections using XSSer Tool": "https://securityxploded.com/detecting-exploiting-xss-using-xsser-tool.php",
                                    "XSSer - Detect and Exploit XSS vulnerabilities": "https://gbhackers.com/xsser-automated-framework-detectexploit-report-xss-vulnerabilities/",
                                    "XSSer- Cross Site Scripting Penetration Tool": "https://www.ehacking.net/2011/02/xsser-cross-site-scripting-penetration.html",
                                },
                            )

                        else:
                            # print(f"{colors.red}[-]Wrong Input{colors.reset}")
                            break
                elif ask == "2":
                    writeup.writeup(
                        {
                            "The popping history of XSS": "https://thexssrat.medium.com/the-popping-history-of-xss-4122e34ac586",
                            "Reflected Cross Site Scripting": "https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting",
                            "XXS HackerOne Report": "https://www.hacker101.com/sessions/xss",
                            "From P5 to P2, from nothing to 1000+$": "https://medium.com/@mohameddaher/from-p5-to-p5-to-p2-from-nothing-to-1000-bxss-4dd26bc30a82",
                            "Reflected XSS on Microsoft.com via Angular Js template injection": "https://infosecwriteups.com/reflected-xss-on-microsoft-com-via-angular-template-injection-2e26d80a7fd8",
                            "From Self-XSS to Persistent XSS on Login Portal": "https://medium.com/@nnez/always-escalate-from-self-xss-to-persistent-xss-on-login-portal-54265b0adfd0",
                            "Self XSS to Account Takeover": "https://medium.com/@Ch3ckM4te/self-xss-to-account-takeover-72c89775cf8f",
                            "Blind Xss (A mind game to win the battle)": "https://medium.com/@dirtycoder0124/blind-xss-a-mind-game-to-win-the-battle-4fc67c524678?",
                            "BugBounty | A Dom Xss": "https://jinone.github.io/bugbounty-a-dom-xss/",
                            "How I turned Self XSS to Stored via CSRF": "https://medium.com/@abhishekY495/how-i-turned-self-xss-to-stored-via-csrf-d12eaaf59f2e",
                            "XSS will never die": "https://medium.com/@Lekssik/xss-will-never-die-eb3584081a5f",
                            "Cookie-based XSS exploitation": "https://medium.com/@ISecMax/cookie-based-xss-exploitation-2300-bug-bounty-story-9bc532ffa564",
                            "Self XSS To Evil XSS": "https://saadahmedx.medium.com/self-xss-to-evil-xss-bcf2494a82a4",
                            "CSRF Attack can lead to Stored XSS": "https://infosecwriteups.com/csrf-attack-can-lead-to-stored-xss-f40ba91f1e4f",
                            "The 5000$ Google XSS": "https://blog.it-securityguard.com/bugbounty-the-5000-google-xss/",
                            "XSS by Tossing Cookies": "https://wesecureapp.com/blog/xss-by-tossing-cookies/",
                            "Medium Content Spoofing Leads to XSS": "https://ahussam.me/Medium-content-spoofing-xss/",
                            "3 Minutes & XSS!": "https://infosecwriteups.com/3-minutes-xss-71e3340ad66b",
                            "The 2.5 BTC Stored XSS": "https://medium.com/@khaled.hassan/the-2-5-btc-stored-xss-f2f9393417f2",
                        },
                        "XSS",
                    )
                else:
                    break

        elif vulns == "1":
            os.system("clear")
            banner.main()
            banner.attack("XXE - XML External Entity")
            # name,command,discription,writeups,link="",method="kali",github_install="",github_check=""
            github = "No tools available for this Vulnerability type.\nIt is recommended to test manually for XML External Entity (XXE) to get better understanding & results.\nCheck out the writeup section to to learn about XXE"
            template.template(
                "XXE",
                "no-tools",
                github.strip(),
                {
                    "XXE": "https://phonexicum.github.io/infosec/xxe.html",
                    "XML External Entity Injection Processing (Intigriti)": "https://blog.intigriti.com/hackademy/xml-external-entity-processing-xxe/",
                    "XML external entity (XXE) injection": "https://portswigger.net/web-security/xxe",
                    "Exploitation: XXE Injection": "https://depthsecurity.com/blog/exploitation-xml-external-entity-xxe-injection",
                    "XML External Entity Injection Processing (OWASP)": "https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing",
                    "XML External Entity Prevention Cheat Sheet": "https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html",
                    "Testing for XML Injection": "https://wiki.owasp.org/index.php/Testing_for_XML_Injection_(OTG-INPVAL-008)",
                    "XXE Injection Payload List": "https://github.com/payloadbox/xxe-injection-payload-list",
                },
            )

        elif vulns == "2":
            os.system("clear")
            banner.main()
            banner.attack("HTML Injection")
            # name,command,discription,writeups,link="",method="kali",github_install="",github_check=""
            github = "No tools available for this Vulnerability type.\nIt is recommended to test manually for HTML Injection to get better understanding & results.\nCheck out the writeup section to to learn about HTML Injection"
            template.template(
                "HTML Injection",
                "no-tools",
                github.strip(),
                {
                    "Comprehensive Guide on HTML Injection": "https://www.hackingarticles.in/comprehensive-guide-on-html-injection/",
                    "HTML Injection(Unique Exploitation)": "https://medium.com/@pratiky054/html-injection-unique-exploitation-a5c3d4e6fed8",
                    "Better Exfiltration via HTML Injection": "https://d0nut.medium.com/better-exfiltration-via-html-injection-31c72a2dae8b",
                    "HTML injection via email confirmation!": "https://medium.com/cyberverse/got-easiest-bounty-with-html-injection-via-email-confirmation-b1b10575a105",
                    "HTML Injection Tutorial": "https://www.softwaretestinghelp.com/html-injection-tutorial/",
                },
            )

        elif vulns == "3":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("SQL Injection")
                # name,command,discription,writeups,link="",method="kali",github_install="",github_check=""
                ask = vuln_options()
                if ask == "1":
                    while True:
                        os.system("clear")
                        banner.main()
                        banner.attack("SQL Injection")
                        des = "It is recommended to test manually for SQL Injection to get better understanding & results.\nCheck out the writeup section to to learn about SQL Injection"
                        banner.description(des)
                        list_tools = ["SqlMap", "go back"]
                        for i in range(len(list_tools)):
                            print(
                                colors.options,
                                f"{i}) {list_tools[i]}".title(),
                                colors.reset,
                            )
                        option = input(
                            f"\n {colors.select}Select an Option ->{colors.reset} "
                        )
                        if option == "0":
                            print("\n[+] SQLMap")
                            github = github_getting_text("https://sqlmap.org/", "p", 0)
                            template.template(
                                "sqlmap",
                                "sqlmap -h",
                                github.strip(),
                                {
                                    "What is SQL Injection? How to do it with sqlmap?": "https://medium.com/@feat7/what-is-sql-injection-how-to-do-it-with-sqlmap-1e630e8220b7",
                                    "SQL injection using Sqlmap": "https://auntoracharja.medium.com/sql-injection-using-sqlmap-44aa84f7779",
                                    "SQLmap Full Guide For Beginners": "https://systemweakness.com/sqlmap-full-guide-for-beginners-920934cdedac",
                                    "How to use SQLMAP to test a website for SQL Injection vulnerability": "https://www.geeksforgeeks.org/use-sqlmap-test-website-sql-injection-vulnerability/",
                                    "SQLMap - Cheetsheat": "https://book.hacktricks.xyz/pentesting-web/sql-injection/sqlmap",
                                    "TryHackMe : SQLMAP Writeup": "https://nareshlamgade.com.np/2021/05/tryhackme-sqlmap-writeup/",
                                    "Sqlmap - InfoSec": "https://infosecwriteups.com/tagged/sqlmap",
                                },
                            )
                        else:
                            # print(f"{colors.red}[-]Wrong Input{colors.reset}")
                            break
                elif ask == "2":
                    writeup.writeup(
                        {
                            "SQL Injection Cheatsheet": "https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/",
                            "SQL Injection payload lits": "https://infosecwriteups.com/sql-injection-payload-list-b97656cfd66b",
                            "Admin Panel Accessed Via SQL Injection": "https://medium.com/@ratnadip1998/admin-panel-accessed-via-sql-injection-ezy-boooom-57dc60c2815f",
                            "SQL Injection & Remote Code Execution": "https://shahjerry33.medium.com/sql-injection-remote-code-execution-double-p1-6038ca88a2ec",
                            "Double quote Injection (Exploiting SQL Injection)": "https://medium.com/sud0root/bug-bounty-writeups-exploiting-sql-injection-vulnerability-20b019553716",
                            "Hey WAF! Better Luck Next Time! ": "https://akashroxstarz.medium.com/hey-waf-better-luck-next-time-a1df7f444863",
                            "Blind (time-based) SQLi": "https://jspin.re/fileupload-blind-sqli/",
                            "Exploiting “Google BigQuery” SQLI Vulnerability": "https://hackemall.live/index.php/2020/03/31/akamai-web-application-firewall-bypass-journey-exploiting-google-bigquery-sql-injection-vulnerability/",
                        },
                        "SQL Injection",
                    )
                else:
                    break

        elif vulns == "4":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Command Injection")
                # name,command,discription,writeups,link="",method="kali",github_install="",github_check=""
                ask = vuln_options()
                if ask == "1":
                    while True:
                        os.system("clear")
                        banner.main()
                        banner.attack("Command Injection")
                        des = "It is recommended to test manually for Command Injection to get better understanding & results.\nCheck out the writeup section to to learn about Command Injection"
                        banner.description(des)
                        list_tools = ["Commix", "go back"]
                        for i in range(len(list_tools)):
                            print(
                                colors.options,
                                f"{i}) {list_tools[i]}".title(),
                                colors.reset,
                            )
                        option = input(
                            f"\n {colors.select}Select an Option ->{colors.reset} "
                        )
                        if option == "0":
                            print("\n[+] Commix")
                            github = github_getting_text(
                                "https://github.com/commixproject/commix",
                                "p[dir=auto]",
                                3,
                            )
                            template.template(
                                "commix",
                                "python commix.py -h",
                                github.strip(),
                                {
                                    "Commix-Command Injection Exploiter (Beginner’s Guide)": "https://www.hackingarticles.in/commix-command-injection-exploiter-beginners-guide/",
                                    "Commix – OS Command Injection and Exploitation Tool": "https://www.geeksforgeeks.org/commix-os-command-injection-and-exploitation-tool/",
                                    "Commix - Automate Exploiting Command Injection Flaws in Web Applications": "https://null-byte.wonderhowto.com/how-to/use-commix-automate-exploiting-command-injection-flaws-web-applications-0189044/",
                                    "Commix : Detecting & Exploiting Command Injection Flaws.": "https://www.blackhat.com/docs/eu-15/materials/eu-15-Stasinopoulos-Commix-Detecting-And-Exploiting-Command-Injection-Flaws.pdf",
                                },
                                link="https://github.com/commixproject/commix.git",
                                method="github",
                                github_install="git clone https://github.com/commixproject/commix.git",
                                github_check="commix",
                            )
                        else:
                            # print(f"{colors.red}[-]Wrong Input{colors.reset}")
                            break
                elif ask == "2":
                    writeup.writeup(
                        {
                            "Breaking down — Command Injections": "https://infosecwriteups.com/breaking-down-command-injections-97d1029576",
                            "Command Injection Payload List": "https://github.com/payloadbox/command-injection-payload-list",
                            "Command Injection - PayloadAllTheThings": "https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection",
                            "Comprehensive Guide on OS Command Injection": "https://www.hackingarticles.in/comprehensive-guide-on-os-command-injection/",
                            "Command Injection - OWASP": "https://owasp.org/www-community/attacks/Command_Injection",
                        },
                        "Command Injection",
                    )
                else:
                    break

        elif vulns == "5":
            os.system("clear")
            banner.main()
            banner.attack("HTTP Request Smuggling")
            github = "No tools available for this Vulnerability type.\nIt is recommended to test manually for HTTP Req. Smuggling to get better understanding & results.\nCheck out the writeup section to to learn about HTTP Req. Smuggling"
            template.template(
                "HTTP Request Smuggling",
                "no-tools",
                github.strip(),
                {
                    "HTTP request smuggling Explained": "https://infosecwriteups.com/http-request-smuggling-explained-and-exploited-part-0x1-89ce2956534f",
                    "HTTP request smuggling": "https://portswigger.net/web-security/request-smuggling",
                    "HTTP Request Smuggling - Cheat Sheet": "https://0xn3va.gitbook.io/cheat-sheets/web-application/http-request-smuggling",
                    "Write up of two HTTP Requests Smuggling": "https://medium.com/@cc1h2e1/write-up-of-two-http-requests-smuggling-ff211656fe7d",
                    "HTTP Request Smuggling - HackTricks": "https://book.hacktricks.xyz/pentesting-web/http-request-smuggling",
                },
            )

        elif vulns == "6":
            os.system("clear")
            banner.main()
            banner.attack("HTTP Parameter Pollution")
            github = "No tools available for this Vulnerability type.\nIt is recommended to test manually for HTTP Parameter Pollution to get better understanding & results.\nCheck out the writeup section to to learn about HTTP Parameter Pollution"
            template.template(
                "HTTP Parameter Pollution",
                "no-tools",
                github.strip(),
                {
                    "Behind the Scene : HTTP Parameter Pollution": "https://infosecwriteups.com/behind-the-scene-http-parameter-pollution-534b4fa2449c",
                    "Testing for HTTP Parameter Pollution": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution",
                    "HTTP Parameter Pollution - HackTricks": "https://book.hacktricks.xyz/pentesting-web/parameter-pollution",
                    "HTTP Parameter Pollution - Intigiti": "https://blog.intigriti.com/hackademy/http-parameter-pollution/",
                    "Client-side HTTP parameter pollution": "https://portswigger.net/kb/issues/00501400_client-side-http-parameter-pollution-reflected",
                },
            )

        elif vulns == "7":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Open Redirection")
                # name,command,discription,writeups,link="",method="kali",github_install="",github_check=""
                ask = vuln_options()
                if ask == "1":
                    while True:
                        os.system("clear")
                        banner.main()
                        banner.attack("Open Redirection")
                        des = "It is recommended to test manually for Open Redirection to get better understanding & results.\nCheck out the writeup section to to learn about Open Redirection"
                        banner.description(des)
                        list_tools = ["OpenRedireX", "Oralyzer", "go back"]
                        for i in range(len(list_tools)):
                            print(
                                colors.options,
                                f"{i}) {list_tools[i]}".title(),
                                colors.reset,
                            )
                        option = input(
                            f"\n {colors.select}Select an Option ->{colors.reset} "
                        )
                        if option == "0":
                            print("\n[+] OpenRedireX")
                            github = github_getting_text(
                                "https://github.com/devanshbatham/OpenRedireX",
                                "ul[dir=auto]",
                                0,
                            )
                            template.template(
                                "OpenRedireX",
                                "python3 openredirex.py -h",
                                github.strip(),
                                {
                                    "OpenRedireX – Open Redirection Vulnerability Finder Tool in Linux": "https://www.geeksforgeeks.org/openredirex-open-redirection-vulnerability-finder-tool-in-linux/",
                                    "OpenRedireX – A Open Redirection Vulnerability Finder": "https://secnhack.in/openredirex-a-open-redirection-vulnerability-finder/",
                                    "Open Redirect Scanner with Uber.com": "https://infosecwriteups.com/open-redirect-scanner-c72cd60d0bf",
                                    "OpenRedireX – Asynchronous Open redirect Fuzzer for Humans": "https://pentesttools.net/openredirex-asynchronous-open-redirect-fuzzer-for-humans/",
                                },
                                link="https://github.com/devanshbatham/OpenRedireX",
                                method="github",
                                github_install="git clone https://github.com/devanshbatham/OpenRedireX.git",
                                github_check="OpenRedireX",
                            )
                        elif option == "1":
                            print("\n[+] Oralyzer")
                            github = github_getting_text(
                                "https://github.com/r0075h3ll/Oralyzer",
                                "p[dir=auto]",
                                0,
                            )
                            template.template(
                                "Oralyzer",
                                "python3 oralyzer.py -h",
                                github.strip(),
                                {
                                    "Oralyzer : Linux Tool To Identify Open Redirection": "https://www.geeksforgeeks.org/oralyzer-linux-tool-to-identify-open-redirection/",
                                    "Oralyzer – A Automatic Open Redirection Vulnerability Finder": "https://secnhack.in/oralyzer-a-automatic-open-redirection-vulnerability-finder/",
                                    "Oralyzer : Tool To Identify Open Redirection": "https://kalilinuxtutorials.com/oralyzer",
                                    "Oralyzer – Tool To Identify Open Redirection": "https://pentesttools.net/oralyzer-tool-to-identify-open-redirection/",
                                },
                                link="https://github.com/r0075h3ll/Oralyzer.git",
                                method="github",
                                github_install="git clone https://github.com/r0075h3ll/Oralyzer.git",
                                github_check="Oralyzer",
                            )
                        else:
                            # print(f"{colors.red}[-]Wrong Input{colors.reset}")
                            break
                elif ask == "2":
                    writeup.writeup(
                        {
                            "Open redirect - Improper validation of front-end provided redirect links": "https://learn.snyk.io/lessons/open-redirect/javascript/",
                            "Open Redirect - Intigriti": "https://blog.intigriti.com/hackademy/open-redirect/",
                            "Top 25 Open Redirect Bug Bounty Reports": "https://corneacristian.medium.com/top-25-open-redirect-bug-bounty-reports-5ffe11788794",
                            "Open Redirect Payload List": "https://github.com/payloadbox/open-redirect-payload-list",
                            "Open Redirect PayloadAllThethings": "https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Open%20Redirect",
                            "Open-redirection leads to a bounty": "https://infosecwriteups.com/open-redirection-leads-to-a-bounty-d94029e11d17",
                            "Strange Redirect (Fixed but no bounty)": "https://medium.com/@abhishekY495/strange-redirect-fixed-but-no-bounty-54425aea7f19",
                            "Open Redirect To XSS on Login Page": "https://nassimchami.medium.com/1st-bug-bounty-writeup-open-redirect-to-xss-on-login-page-313221da2879",
                        },
                        "Open Redirection",
                    )
                else:
                    break

        elif vulns == "8":
            os.system("clear")
            banner.main()
            banner.attack("LFI - Local File Inclusion")
            github = "No tools available for this Vulnerability type.\nIt is recommended to test manually for LFI to get better understanding & results.\nCheck out the writeup section to to learn about Local File Inclusion"
            template.template(
                "LFI",
                "no-tools",
                github.strip(),
                {
                    "LFI Attack Examples": "https://brightsec.com/blog/lfi-attack-real-life-attacks-and-attack-examples/",
                    "What is Local File Inclusion (LFI)?": "https://www.acunetix.com/blog/articles/local-file-inclusion-lfi/",
                    "Testing for Local File Inclusion": "https://wiki.owasp.org/index.php/Testing_for_Local_File_Inclusion",
                    "CVV #1: Local File Inclusion": "https://infosecwriteups.com/cvv-1-local-file-inclusion-ebc48e0e479a",
                },
            )

        else:
            return


def vuln_options():
    print(f"{colors.options}1) Tools")
    print(f"2) Write-ups")
    print(f"3) Go Back")
    try:
        ask = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
    except KeyboardInterrupt:
        template.exit_program()
    return ask


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
