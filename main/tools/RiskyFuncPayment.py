from main.tools import banner, colors, template,information_gathering,WEB_Application_Analysis,Vulnerability_Analysis,Exploitation_Tools,Session_Management
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
                        colors.options, f"{i+1}) {list_attacks[i]}".title(), colors.reset
                    )
                try:
                    option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if option == "1":
                    print(f"\n[+] Burp Suite")
                    WEB_Application_Analysis.burp_suite()
                elif option == "2":
                    print(f"\n[+] WireShark")
                    Vulnerability_Analysis.wireshark()
                elif option == "3":
                    print(f"\n[+] OwaspZap")
                    WEB_Application_Analysis.owasp_zap()
                elif option == "4":
                    print(f"\n[+] nessus")
                    WEB_Application_Analysis.nessus()
                elif option == "5":
                    print(f"\n[+] Sqlmap")
                    Exploitation_Tools.sqlmap()
                elif option == "6":
                    print(f"\n[+] Fiddler")
                    Session_Management.fiddler()
                elif option == "7":
                    print(f"\n[+] Metasploit")
                    Exploitation_Tools.metasploit()
                elif option == "8":
                    print(f"\n[+] Nmap")
                    information_gathering.nmap()
                elif option == "9":
                    print(f"\n[+] The PenTesters Framework (PTF)")
                    Session_Management.ptf()
                else:
                    break

        elif option == "2":
            print("\n[+] Write-UPS")
            os.system("clear")
            template.template("Writeup","no-tools","Writeups",
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

if __name__ == "__main__":
    main()
