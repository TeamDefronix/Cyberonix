from main.tools import banner, colors, template
import os
import requests
from bs4 import BeautifulSoup


def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Authentication")
        list_vulns = [
            "User enumeration",
            "Authentication bypass",
            "vulnerable remember me functionality",
            "Password reset",
            "Captcha bypass",
            "Autocomplete on ",
            "multifactor authentication",
            "Logout functionality",
            "cache management",
            "Default credentials",
            "Go back",
        ]
        for i in range(len(list_vulns)):
            print(colors.options, f"{i}) {list_vulns[i]}".title(), colors.reset)
        vulns = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        if vulns == "0":
            os.system("clear")
            template.template(
                "Test for User enumeration",
                "no-tools",
                "",
                {
                    "Testing for Account Enumeration and Guessable User Account": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/03-Identity_Management_Testing/04-Testing_for_Account_Enumeration_and_Guessable_User_Account",
                    "What Is User Enumeration?": "https://www.rapid7.com/blog/post/2017/06/15/about-user-enumeration/",
                },
            )
        elif vulns == "1":
            os.system("clear")
            template.template(
                "Testing for authentication bypass",
                "no-tools",
                "",
                {
                    "Testing for Bypassing Authentication Schema": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/04-Testing_for_Bypassing_Authentication_Schema",
                    "5 Unusual Authentication Bypass Techniques": "https://www.synack.com/blog/exploits-explained-5-unusual-authentication-bypass-techniques/",
                    "Authentication vulnerabilities": "https://portswigger.net/web-security/authentication",
                },
            )

        elif vulns == "2":
            os.system("clear")
            template.template(
                "Testing for vulnerable remember me functionality",
                "no-tools",
                "",
                {
                    "Testing for Vulnerable Remember Password": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/05-Testing_for_Vulnerable_Remember_Password",
                    "Exploiting Remember Me Cookie For Account Takeover": "https://gupta-bless.medium.com/exploiting-remember-me-cookie-for-account-takeover-4e8d5fd42d4b",
                },
            )

        elif vulns == "3":
            os.system("clear")
            template.template(
                "Testing for Password reset",
                "no-tools",
                "",
                {
                    "Password reset poisoning": "https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning",
                    "Testing Forgot Password Functionality": "https://twitter.com/tuhin1729_/status/1437471718142976007?t=G7ODwQzc6ON2T6_DDC89jA&s=19",
                    "Exploiting Password Reset Poisoning": "https://infosecwriteups.com/exploiting-password-reset-poisoning-b748797f0661",
                },
            )

        elif vulns == "4":
            os.system("clear")
            template.template(
                "Testing for Captcha bypass",
                "no-tools",
                "",
                {
                    "CAPTCHA BYPASS TECHNIQUES !": "https://honeyakshat999.medium.com/captcha-bypass-techniques-f768521516b2",
                    "Bypass Captcha🤗(Google reCAPTCHA)": "https://twitter.com/Aacle_/status/1586735203481161728?t=Vz4U17f1nHQzoXRUuMVDiA&s=19",
                    "Captcha Bypass Techniques": "https://github.com/harsh-bothra/learn365/blob/main/days/day31.md",
                },
            )

        elif vulns == "5":
            os.system("clear")
            template.template(
                "Test for autocomplete on",
                "no-tools",
                "",
                {
                    " Password field with autocomplete enabled ": "https://portswigger.net/kb/issues/00500800_password-field-with-autocomplete-enabled",
                    "Finding and Fixing Vulnerabilities in AutoComplete Not Disabled ": "https://www.beyondsecurity.com/scan-pentest-network-vulnerabilities-autocomplete-not-disabled",
                },
            )

        elif vulns == "6":
            os.system("clear")
            template.template(
                "Testing for multifactor authentication",
                "no-tools",
                "",
                {
                    "Testing Multi-Factor Authentication (MFA)": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/11-Testing_Multi-Factor_Authentication",
                    "Testing Two-Factor Authentication": "https://research.nccgroup.com/2021/06/10/testing-two-factor-authentication/",
                    "How to Test Two-Factor Authentication: A Guide with Use Cases": "https://www.browserstack.com/guide/test-two-factor-authentication",
                },
            )

        elif vulns == "7":
            os.system("clear")
            template.template(
                "Check SSL Version, Algorithms",
                "no-tools",
                "",
                {
                    "Testing for Logout Functionality": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/06-Testing_for_Logout_Functionality",
                    " Test Cases For Logout | Test Scenarios For Logout ": "https://www.qaacharya.in/2019/06/test-cases-scenarios-for-logout.html",
                },
            )

        elif vulns == "8":
            os.system("clear")
            template.template(
                "Test for cache management",
                "no-tools",
                "",
                {
                    "Testing for Browser Cache Weaknesses": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/06-Testing_for_Browser_Cache_Weaknesses",
                    "Cache Controls Explained": "https://www.virtuesecurity.com/kb/cache-controls-explained/",
                },
            )

        elif vulns == "9":
            template.template(
                "Test for Default credentials",
                "no-tools",
                "",
                {
                    "Testing for Default Credentials": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/02-Testing_for_Default_Credentials",
                    "How default credentials helped this Hacker to get 13337$": "https://medium.com/@ashishrohra/how-default-credentials-helped-this-hacker-to-get-13337-s-d1504ebf95e4",
                },
            )
        else:
            return


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
