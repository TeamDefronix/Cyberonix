from main.tools import banner, colors, template
import os

import requests
from bs4 import BeautifulSoup


def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Secure Transmission")
        list_vulns = [
            "Check SSL Version, Algorithms, Key length",
            "Check for Digital Certificate Validity",
            "Check credentials only delivered over HTTPS",
            "Check session tokens only delivered over HTTPS",
            "Check if HTTP Strict Transport Security (HSTS) in use",
            "Go back",
        ]
        for i in range(len(list_vulns)):
            print(colors.options, f"{i}) {list_vulns[i]}".title(), colors.reset)
        vulns = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        if vulns == "0":
            os.system("clear")
            # github=github_getting_text("","")
            template.template(
                "Check SSL Version, Algorithms",
                "no-tools",
                "",
                {
                    "10 Online Tools to Test SSL, TLS and Latest Vulnerability": "https://geekflare.com/ssl-test-certificate/",
                    "Testing for Weak SSL TLS Ciphers": "https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/01-Testing_for_Weak_SSL_TLS_Ciphers_Insufficient_Transport_Layer_Protection",
                    "How to Verify the SSL Key Length": "https://www.rapidsslonline.com/ssl/how-to-verify-the-ssl-key-length",
                },
            )
            # writeup.writeup({"10 Online Tools to Test SSL, TLS and Latest Vulnerability":"https://geekflare.com/ssl-test-certificate/","Testing for Weak SSL TLS Ciphers":"https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/01-Testing_for_Weak_SSL_TLS_Ciphers_Insufficient_Transport_Layer_Protection","How to Verify the SSL Key Length":"https://www.rapidsslonline.com/ssl/how-to-verify-the-ssl-key-length/"},"Check SSL Version, Algorithms, Key length")
        elif vulns == "1":
            os.system("clear")
            # github
            template.template(
                "Check for Digital Certificate Validity",
                "no-tools",
                "",
                {
                    "A closer look at Digital Certificates": "https://medium.com/@mehulgala77/a-closer-look-at-digital-certificates-9ce5a4c56f75"
                },
            )
        elif vulns == "2":
            os.system("clear")
            template.template(
                "Check credentials only delivered over HTTPS",
                "no-tools",
                "",
                {
                    "Testing for Credentials Transported over an Encrypted Channel": "https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/04-Authentication_Testing/01-Testing_for_Credentials_Transported_over_an_Encrypted_Channel",
                    "Penetration testing of Credential Data over Encrypted Channel": "https://www.hackingloops.com/penetration-testing-of-credential-data-over-encrypted-channel/",
                },
            )
        elif vulns == "3":
            os.system("clear")
            template.template(
                "Check session tokens only delivered over HTTPS",
                "no-tools",
                "",
                {
                    "Testing for Exposed Session Variables": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/04-Testing_for_Exposed_Session_Variables",
                    "Using Burp to Test Session Token Handling": "https://portswigger.net/support/using-burp-to-test-session-token-handling",
                },
            )

        elif vulns == "4":
            os.system("clear")
            template.template(
                "Check if HTTP Strict Transport Security (HSTS) in use",
                "no-tools",
                "",
                {
                    "HSTS (HTTP Strict Transport Security) Test": "https://geekflare.com/tools/hsts-test",
                    "What Is HSTS and Why Should I Use It?": "https://www.acunetix.com/blog/articles/what-is-hsts-why-use-it/",
                },
            )
        else:
            return


def vuln_options():
    print(f"{colors.options}1) Tools")
    print(f"2) Write-ups")
    print(f"3) Go Back..")
    ask = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
    return ask


def github_getting_text(link, selector, indexvalue):
    print(f"Please Wait....\r", end="")
    URL = link
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, "html5lib")
        paras = soup.select(selector)
        # check index value from test file
        return paras[indexvalue].text
    except:
        return "{colors.red}NotLloaded Because No Internet Connection{colors.reset}"


if __name__ == "__main__":
    main()
