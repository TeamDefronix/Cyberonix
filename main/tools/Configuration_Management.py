from main.tools import banner, colors, template,WEB_Application_Analysis,Exploitation_Tools,Vulnerability_Analysis,information_gathering
import os
import requests
from bs4 import BeautifulSoup


# main function
def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Configuration Management")
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
                    " Dirb",
                    " Gobuster",
                    " Nikto",
                    " Wfuzz",
                    " Dirbuster",
                    " Feroxbuster",
                    " Nmap",
                    " HTTPie",
                    " Metasploit",
                    "SecurityHeaders",
                    "SQLmap",
                    "TruffleHog",
                    "SecretFinder",
                    "Go Back"
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
                    print("\n[+] Dirb")
                    WEB_Application_Analysis.dirb()
                elif option == "2":
                    print("\n[+] Gobuster")
                    gobuster()
                elif option == "3":
                    print("\n[+] Nikto")
                    WEB_Application_Analysis.nikto()
                elif option == "4":
                    print("\n[+] Wfuzz")
                    Vulnerability_Analysis.wfuzz()
                elif option == "5":
                    print("\n[+] Dirbuster")
                    dirbuster()
                elif option == "6":
                    print("\n[+] Feroxbuster")
                    feroxbuster()
                elif option == "7":
                    print("\n[+] Nmap")
                    information_gathering.nmap()
                elif option == "8":
                    print("\n[+] HTTPie")
                    httpie()                
                elif option == "9":
                    print("\n[+] Metasploit")
                    Exploitation_Tools.metasploit()
                elif option == "10":
                    print("\n[+] SecurityHeaders")
                    securityheaders()                
                elif option == "11":
                    print("\n[+] Sqlmap")
                    Exploitation_Tools.sqlmap()
                elif option == "12":
                    print("\n[+] TruffleHog")
                    trufflehog()                
                elif option == "13":
                    print("\n[+] SecretFinder")
                    secretfinder()              
                else:
                    break

        elif option == "2":
            print("\n[+] Write-UPS")
            os.system("clear")
            template.template("Writeup","no-tools","Writeups",
                {
            "Configuration management in penetration testing": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/README",
            "How to find Exposed backup and unreferenced files": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/04-Review_Old_Backup_and_Unreferenced_Files_for_Sensitive_Information",
            "Review Old Backup and Unreferenced Files for Sensitive Information": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/04-Review_Old_Backup_and_Unreferenced_Files_for_Sensitive_Information",
            "Multiple Ways to Detect HTTP Options": "https://www.hackingarticles.in/multiple-ways-to-detect-http-options/",
            "security HTTP headers scanning and details": "https://www.atatus.com/tools/security-header",
            "Testing for Content Security Policy": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/12-Test_for_Content_Security_Policy",
            "Test Network Infrastructure Configuration": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/01-Test_Network_Infrastructure_Configuration",
            "Testing applications in production vs. non-production benefits": "https://www.techtarget.com/searchsecurity/tip/Testing-applications-in-production-vs-non-production-benefits",
            "How to Scan GitHub Repository for Credentials": "https://geekflare.com/github-credentials-scanner/",
                },
                "Configuration-Management Writeups",
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
        
def secretfinder():
    os.system("clear")
    github = "SecretFinder is an open-source tool used to scan web applications for sensitive information and secrets, such as API keys, passwords, and tokens. It is designed to identify potential security vulnerabilities that could be exploited by attackers, and can be used in bug bounty hunting and vulnerability assessments. SecretFinder uses a combination of static analysis and dynamic analysis techniques to discover secrets, and can be customized with various options and configurations to suit specific use cases. It generates a report of its findings, which can be used to remediate identified vulnerabilities and improve the overall security of the web application. SecretFinder is a powerful and efficient tool that can help security professionals and developers identify potential security risks in their web applications."
    template.template(
                        "secretFinder",
                        "python3 SecretFinder.py -h",
                        github.strip(),
                        {
                            "SecretFinder demo": "https://www.briskinfosec.com/tooloftheday/toolofthedaydetail/SecretFinder",
                        },
                        method="github",
                        github_install="git clone https://github.com/m4ll0k/SecretFinder.git && cd SecretFinder && pip install -r requirements.txt",
                        github_check="SecretFinder",
                    )
def trufflehog():
    os.system("clear")
    github = "Trufflehog is an open-source tool used for searching and identifying sensitive information and secrets, such as API keys, passwords, and private keys, in source code repositories. It is designed to scan code repositories for potential security vulnerabilities that could be exploited by attackers, and can be used in bug bounty hunting and vulnerability assessments. Trufflehog uses advanced techniques, such as entropy analysis and regular expressions, to identify potential security issues, and generates a report of its findings. It is a powerful and flexible tool that can help security professionals and developers identify potential security risks in their code."
    template.template(
                        "trufflehog",
                        "trufflehog -h",
                        github.strip(),
                        {
                            "Usage": "https://github.com/trufflesecurity/trufflehog",
                            "Finding Secrets in Git Repos with TruffleHog": "https://materials.rangeforce.com/tutorial/2020/03/16/TruffleHog/",
                        },
                    )
def securityheaders():
    os.system("clear")
    github = """SecurityHeaders is a configuration management tool that focuses on securing web applications by helping administrators configure appropriate HTTP security headers. HTTP security headers are additional response headers that can be sent by a web server to a client's browser to instruct it to follow certain security-related behaviors. For example, the "Content-Security-Policy" header can be used to restrict the types of content that a web page can load, helping to prevent cross-site scripting (XSS) attacks."""
    template.template(
                        "securityheaders",
                        "python3 securityheaders.py -h",
                        github.strip(),
                        {
                            "Website": "https://securityheaders.com/",
                            "Securityheaders usage": "https://github.com/koenbuyens/securityheaders",
                        },
                        method="github",
                        github_install="git clone https://github.com/koenbuyens/securityheaders.git && cd securityheaders && pip install -r requirements.txt",
                        github_check="securityheaders",
                    )
def httpie():
    os.system("clear")
    github = "HTTPie is a command-line tool used to send HTTP requests and receive responses from a server. It is designed to be user-friendly and intuitive, with a simple syntax and easy-to-read output. HTTPie can be used to test and debug APIs, as well as interact with web services and applications. It supports various HTTP methods, data formats, and authentication methods, and can be customized with various options and configurations to suit specific use cases."
    template.template(
                        "httpie", "httpie -h", github.strip(), "no-writeups"
                    )
def gobuster():
	os.system("clear")
	github = """Gobuster is an open-source tool used by security professionals and penetration testers to perform web content discovery and directory/file enumeration on a target website. It is a popular tool used in bug bounty hunting and vulnerability assessments. The tool works by launching a series of HTTP requests to the target website and analyzing the responses to discover hidden directories, files, and other web resources that may not be easily discoverable through normal browsing. It uses a wordlist of common directory and file names, as well as brute-force techniques to guess the names of hidden directories and files."""
	template.template(
                        "gobuster",
                        "gobuster -h",
                        github.strip(),
                        {
                            "Gobuster Complete tutorial": "https://hackertarget.com/gobuster-tutorial/",
                            "Scan Websites for Interesting Directories using Gobuster": "https://null-byte.wonderhowto.com/how-to/scan-websites-for-interesting-directories-files-with-gobuster-0197226/",
                            "How to use Gobuster for Scanning Website’s Subdomains & Directories": "https://spinningsecurity.com/how-to-use-gobuster-for-scanning-websites/",
                        },)


def dirbuster():
	os.system("clear")
	github = "DirBuster is a web application scanner designed to brute force directories and files names on web servers. It is a Java-based tool and can be used to discover hidden content, sensitive files, and directories that are not exposed through normal web browsing. DirBuster is also capable of detecting common web application vulnerabilities such as SQL injection, file inclusion, and cross-site scripting. The tool has an easy to use graphical user interface, and users can customize the wordlist to use in the directory and file name brute force. It is widely used by security professionals, penetration testers, and bug bounty hunters to identify security issues in web applications."
	template.template(
                        "dirbuster", "dirbuster -h", github.strip(), "no-writeups"
                    )
                   
def feroxbuster():
	os.system("clear")
	github = "Feroxbuster is an open-source content discovery and directory/file enumeration tool used in bug bounty hunting and web application security assessments. It quickly scans a target website for hidden directories, files, and other resources using a variety of techniques and generates a report of its findings."
	template.template(
                        "feroxbuster", "feroxbuster -h", github.strip(), "no-writeups"
                    )
if __name__ == "__main__":
    main()
