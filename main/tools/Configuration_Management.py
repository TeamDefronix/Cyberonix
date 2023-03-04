from main.tools import banner, colors, template
from main import Cheat_sheet
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
            print(colors.options, f"{i}) {list_attacks[i]}".title(), colors.reset)
        option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        if option == "0":
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
                    " Skipfish",
                    " Dirbuster",
                    " Feroxbuster",
                    " Nmap",
                    " HTTPie",
                    " Metasploit",
                    "SecurityHeaders",
                    "SQLmap",
                    "TruffleHog",
                    "Gitleaks",
                    "SecretFinder",
                ]
                for i in range(len(list_attacks)):
                    print(
                        colors.options, f"{i}) {list_attacks[i]}".title(), colors.reset
                    )
                option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                if option == "0":
                    print("\n[+] Dirb")
                    os.system("clear")
                    github = "Dirb is a web application scanner tool that is commonly used for reconnaissance and information gathering during web application testing. It can be used to brute-force common directory and file names on a web server, and is often used by penetration testers and security professionals to identify potential vulnerabilities in web applications. By running Dirb on a target web application, testers can quickly identify common directories and files that may contain sensitive information or be vulnerable to attack. This can help to guide further testing efforts and improve the overall security posture of the web application."
                    template.template(
                        "dirb",
                        "dirb",
                        github.strip(),
                        {
                            "Using Dirb to Find Hidden Directories": "https://www.hackers-arise.com/post/2016/12/13/web-app-hacling-part-4-using-dirb-to-find-hidden-directories",
                            "Comprehensive Guide on Dirb Tool": "https://www.hackingarticles.in/comprehensive-guide-on-dirb-tool/",
                            "How Dirb works": "https://infosecaddicts.com/dirb-is-a-web-content-scanner/",
                        },
                    )
                elif option == "1":
                    print("\n[+] Gobuster")
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
                        },
                    )
                elif option == "2":
                    print("\n[+] Nikto")
                    os.system("clear")
                    github = "Nikto is an open-source web server scanner used by security professionals and penetration testers to identify vulnerabilities and misconfigurations in web servers and web applications. It is a popular tool used in bug bounty hunting and vulnerability assessments. The tool works by launching a series of HTTP requests to the target website and analyzing the responses to identify potential security issues. It checks for known vulnerabilities and misconfigurations in the web server, including outdated software versions, insecure server configurations, and other common security issues."
                    template.template(
                        "nikto",
                        "nikto --help",
                        github.strip(),
                        {
                            "Nikto overview and usage": "https://securitytrails.com/blog/nikto-website-vulnerability-scanner",
                            "How to find Web Server Vulnerabilities with Nikto Scanner": "https://geekflare.com/nikto-webserver-scanner/",
                            "Nikto Commands in details": "https://www.mankier.com/1/nikto",
                        },
                    )
                elif option == "3":
                    print("\n[+] Wfuzz")
                    os.system("clear")
                    github = "Wfuzz is a web application brute force tool used to identify web application vulnerabilities by scanning web content, such as directories and files, for hidden or non-linked content. Wfuzz can be used to test input validation, error handling, and access control mechanisms. It is a command-line tool and allows users to customize requests to send payloads, which makes it very flexible and powerful for web application penetration testing. Wfuzz is written in Python and can be used on Linux, Windows, and macOS. It is open-source and free to use."
                    template.template(
                        "wfuzz", "wfuzz --help", github.strip(), "no-writeups"
                    )
                elif option == "4":
                    print("\n[+] Skipfish")
                    os.system("clear")
                    github = "Skipfish is an open-source web application security scanner that is commonly used in bug bounty hunting and vulnerability assessments. It is designed to efficiently scan large and complex web applications and identify potential security vulnerabilities. The tool works by launching a series of requests to the target website and analyzing the responses to identify potential vulnerabilities, such as SQL injection, cross-site scripting, and file inclusion vulnerabilities. Skipfish uses a combination of automated and manual techniques to identify vulnerabilities, including fuzzing and signature-based scanning."
                    template.template(
                        "skipfish",
                        "skipfish -h",
                        github.strip(),
                        {
                            "Skipfish commands in details": "https://linux.die.net/man/1/skipfish",
                        },
                    )
                elif option == "5":
                    print("\n[+] Dirbuster")
                    os.system("clear")
                    github = "DirBuster is a web application scanner designed to brute force directories and files names on web servers. It is a Java-based tool and can be used to discover hidden content, sensitive files, and directories that are not exposed through normal web browsing. DirBuster is also capable of detecting common web application vulnerabilities such as SQL injection, file inclusion, and cross-site scripting. The tool has an easy to use graphical user interface, and users can customize the wordlist to use in the directory and file name brute force. It is widely used by security professionals, penetration testers, and bug bounty hunters to identify security issues in web applications."
                    template.template(
                        "dirbuster", "dirbuster -h", github.strip(), "no-writeups"
                    )
                elif option == "6":
                    print("\n[+] Feroxbuster")
                    os.system("clear")
                    github = "Feroxbuster is an open-source content discovery and directory/file enumeration tool used in bug bounty hunting and web application security assessments. It quickly scans a target website for hidden directories, files, and other resources using a variety of techniques and generates a report of its findings."
                    template.template(
                        "feroxbuster", "feroxbuster -h", github.strip(), "no-writeups"
                    )
                elif option == "7":
                    print("\n[+] Nmap")
                    os.system("clear")
                    github = "Nmap (Network Mapper) is a network scanner created by Gordon Lyon (also known by his pseudonym Fyodor Vaskovich). Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses."
                    template.template(
                        "nmap",
                        "nmap",
                        github.strip(),
                        {
                            "Official website": "https://nmap.org/",
                            "How To Test your Firewall Configuration with Nmap": "https://www.digitalocean.com/community/tutorials/how-to-test-your-firewall-configuration-with-nmap-and-tcpdump",
                            "Nmap Vulnerability Scanning": "https://nira.com/nmap-vulnerability-scanning/",
                            "How to test Firewall Configuration with Nmap on Linux Cloud Servers": "https://www.layerstack.com/resources/tutorials/How-to-test-Firewall-Configuration-with-Nmap-on-Linux-Cloud-Servers",
                        },
                    )
                elif option == "8":
                    print("\n[+] HTTPie")
                    os.system("clear")
                    github = "HTTPie is a command-line tool used to send HTTP requests and receive responses from a server. It is designed to be user-friendly and intuitive, with a simple syntax and easy-to-read output. HTTPie can be used to test and debug APIs, as well as interact with web services and applications. It supports various HTTP methods, data formats, and authentication methods, and can be customized with various options and configurations to suit specific use cases."
                    template.template(
                        "HTTPie", "httpie -h", github.strip(), "no-writeups"
                    )
                elif option == "9":
                    print("\n[+] Metasploit")
                    os.system("clear")
                    github = "The Metasploit Framework is an open-source tool for developing and executing exploit code against a remote target machine. It can be used to test the security of a computer system by finding and exploiting vulnerabilities. The framework includes a large collection of exploit modules, as well as various tools for payload generation, post-exploitation, and more. It can be used by security professionals for penetration testing, as well as by attackers for malicious purposes."
                    template.template(
                        "metasploit-framework",
                        "msfconsole",
                        github.strip(),
                        "no-writeups",
                    )
                elif option == "10":
                    print("\n[+] SecurityHeaders")
                    os.system("clear")
                    github = """SecurityHeaders is a configuration management tool that focuses on securing web applications by helping administrators configure appropriate HTTP security headers. HTTP security headers are additional response headers that can be sent by a web server to a client's browser to instruct it to follow certain security-related behaviors. For example, the "Content-Security-Policy" header can be used to restrict the types of content that a web page can load, helping to prevent cross-site scripting (XSS) attacks."""
                    template.template(
                        "securityheaders",
                        "pip install -r requirements.txt > /dev/null 2>&1 && python3 securityheaders.py -h",
                        github.strip(),
                        {
                            "Website": "https://securityheaders.com/",
                            "Securityheaders usage": "https://github.com/koenbuyens/securityheaders",
                        },
                        method="github",
                        github_install="git clone https://github.com/koenbuyens/securityheaders.git",
                        github_check="securityheaders",
                    )
                elif option == "11":
                    print("\n[+] Sqlmap")
                    os.system("clear")
                    github = github_getting_text("https://sqlmap.org/", "p", 0)
                    template.template(
                        "sqlmap",
                        "sqlmap",
                        github.strip(),
                        {
                            "Usage Of Sqlmap": "https://github.com/sqlmapproject/sqlmap/wiki/Usage",
                            "SQLmap Complete Tutorial": "https://hackertarget.com/sqlmap-tutorial/",
                        },
                    )
                elif option == "12":
                    print("\n[+] TruffleHog")
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
                elif option == "13":
                    print("\n[+] Gitleaks")
                    os.system("clear")
                    github = "Gitleaks is an open-source tool used to scan Git repositories for sensitive information and secrets, such as passwords, API keys, and private keys. It is designed to identify potential security vulnerabilities that could be exploited by attackers, and can be used in bug bounty hunting and vulnerability assessments. Gitleaks uses a comprehensive set of rules and checks to detect potential security issues, and can be customized with various options and configurations to suit specific use cases. It generates a report of its findings, which can be used to remediate identified vulnerabilities and improve the overall security of the Git repositories. Gitleaks is a powerful and efficient tool that can help security professionals and developers identify potential security risks in their code repositories."
                    template.template(
                        "gitleaks", "gitleaks -h", github.strip(), "no-writeups"
                    )
                elif option == "14":
                    print("\n[+] SecretFinder")
                    os.system("clear")
                    github = "SecretFinder is an open-source tool used to scan web applications for sensitive information and secrets, such as API keys, passwords, and tokens. It is designed to identify potential security vulnerabilities that could be exploited by attackers, and can be used in bug bounty hunting and vulnerability assessments. SecretFinder uses a combination of static analysis and dynamic analysis techniques to discover secrets, and can be customized with various options and configurations to suit specific use cases. It generates a report of its findings, which can be used to remediate identified vulnerabilities and improve the overall security of the web application. SecretFinder is a powerful and efficient tool that can help security professionals and developers identify potential security risks in their web applications."
                    template.template(
                        "secretFinder",
                        "pip install -r requirements.txt > /dev/null 2>&1 && python3 SecretFinder.py -h",
                        github.strip(),
                        {
                            "SecretFinder demo": "https://www.briskinfosec.com/tooloftheday/toolofthedaydetail/SecretFinder",
                        },
                        method="github",
                        github_install="git clone https://github.com/m4ll0k/SecretFinder.git",
                        github_check="SecretFinder",
                    )
                else:
                    break

        elif option == "1":
            print("\n[+] Write-UPS")
            os.system("clear")
            banner.main()
            Cheat_sheet.cheat(
                {
                    "Configuration management in penetration testing": "https://www.jasonclause.com/configuration-management-cybersecurity/#:~:text=Configuration%20management%20is%20the%20process,software%20and%20the%20associated%20settings.",
                    "How to find Exposed backup and unreferenced files": "https://securityboulevard.com/2021/08/exposed-backup-and-unreferenced-files-and-how-to-find-them/",
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
        soup = BeautifulSoup(r.content, "html5lib")
        paras = soup.select(selector)
        # check index value from test file
        return paras[indexvalue].text
    except:
        return f"{colors.red}Not Loaded Because No Internet Connection{colors.reset}"


if __name__ == "__main__":
    main()
