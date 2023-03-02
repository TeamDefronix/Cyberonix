from bs4 import BeautifulSoup
from main.tools import banner, template, colors
import os
import requests
from bs4 import BeautifulSoup


def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("HTML5")
        list_vulns = [
            "WEB Messaging",
            "WEB Storage SQL Injection",
            "CORS Implementation",
            "Offline Web Applicatipn",
            "Go back",
        ]
        for i in range(len(list_vulns)):
            print(colors.options, f"{i}) {list_vulns[i]}".title(), colors.reset)
        vulns = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        if vulns == "0":
            github = "Web messaging is the ability to send realtime messages from the server to the client browser. It overrides the cross domain communication problem in different domains, protocols or ports"
            template.template(
                "WEB Messaging",
                "no-tools",
                github.strip(),
                {
                    "HTML5 - Web messaging": "https://www.tutorialspoint.com/html5/html5_web_messaging.htm",
                    "Testing Web Messaging": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/11-Testing_Web_Messaging",
                    "Web message manipulation": "https://portswigger.net/web-security/dom-based/web-message-manipulation",
                    "HTML5 Security: Cross Domain Messaging": "https://resources.infosecinstitute.com/topic/html5-security-cross-domain-messaging/",
                    "Testing for DOM XSS using web messages": "https://portswigger.net/burp/documentation/desktop/tools/dom-invader/web-messages",
                },
            )

        elif vulns == "1":
            github = "SQL injection testing checks if it is possible to inject data into the application so that it executes a user-controlled SQL query in the database. Testers find a SQL injection vulnerability if the application uses user input to create SQL queries without proper input validation. "
            template.template(
                "WEB Storage SQL Injection",
                "no-tools",
                github.strip(),
                {
                    "Testing Browser Storage": "https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/12-Testing_Browser_Storage",
                    "Testing for SQL Injection": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection",
                    "Client-side SQL injection": "https://portswigger.net/kb/issues/00200332_client-side-sql-injection-stored-dom-based",
                    "Secure Implementation of HTML5's Web SQL Database": "https://code.google.com/archive/p/html5security/wikis/WebSQLDatabaseSecurity.wiki",
                },
            )

        elif vulns == "2":
            github = "Cross-origin resource sharing (CORS) is a mechanism that allows restricted resources on a web page to be requested from another domain outside the domain from which the first resource was served."
            template.template(
                "WEB Storage SQL Injection",
                "no-tools",
                github.strip(),
                {
                    "What is Web CORS in HTML5 ?": "https://www.geeksforgeeks.org/what-is-web-cors-in-html5/",
                    "Cross-origin resource sharing (CORS)": "https://portswigger.net/web-security/cors",
                    "Testing Cross Origin Resource Sharing": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/07-Testing_Cross_Origin_Resource_Sharing",
                    "CORS Misconfiguration": "https://systemweakness.com/first-bug-bounty-program-found-cors-cross-origin-resource-sharing-misconfiguration-52c1bd3ebfe0",
                    "Advanced CORS Exploitation Techniques": "https://infosecwriteups.com/think-outside-the-scope-advanced-cors-exploitation-techniques-dad019c68397",
                    "Exploiting CORS misconfigurations for Bitcoins and bounties": "https://portswigger.net/research/exploiting-cors-misconfigurations-for-bitcoins-and-bounties",
                    "CORS - Misconfigurations & Bypass": "https://book.hacktricks.xyz/pentesting-web/cors-bypass",
                    "CORS Misconfiguration": "https://0xn3va.gitbook.io/cheat-sheets/web-application/cors-misconfiguration",
                },
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
