from main.tools import banner, colors, template, waiting, writeup, Configuration_Management
import os
import requests
import requests
import re
from bs4 import BeautifulSoup


def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("WEB Application Analysis")
        list_attacks = [" Burp Suite\t\t(Recommended)", " Dirsearch", " Owasp ZAP", " Dirbuster\t\t(Recommended)",
                        " Nikto", " Wapiti", " Nessus\t\t(Recommended)", " dirb", " Nuclei", "ffuf", "go back"]
        for i in range(len(list_attacks)):
            print(colors.options, f"{i+1}) {list_attacks[i]}".title(), colors.reset)
        try:
            option = input(
                f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            return
        if option == "1":
            print(f"\n[+] Burp Suite")
            burp_suite()
        elif option == "2":
            print(f"\n[+] Dirsearch")
            dirsearch()
        elif option == "3":
            print(f"\n[+] Owasp ZAP")
            owasp_zap()
        elif option == "4":
            Configuration_Management.dirbuster()
        elif option == "5":
            print("\n[+] Nikto")
            nikto()
        elif option == "6":
            print("\n[+] Wapiti")
            wapiti()
        elif option == "7":
            print(f"\n[+] Nessus")
            nessus()
        elif option == "8":
            print(f"\n[+] dirb")
            dirb()
        elif option == "9":
            print(f"\n[+] Nuclei")
            nuclei()
        elif option == "10":
            print("\n[+] ffuf")
            ffuf()
        else:
            return


def github_getting_text(link, selector, indexvalue):
    print(f"Please Wait....\r", end="")
    URL = link
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')
        paras = soup.select(selector)
        # check index value from test file
        return paras[indexvalue].text
    except:
        return "{colors.red}NotLloaded Because No Internet Connection{colors.reset}"


def nikto():
    os.system("clear")
    github = github_getting_text(
                "https://en.wikipedia.org/wiki/Nikto_(vulnerability_scanner)", 'p', 1)
    template.template("nikto", "nikto ", github.strip(), {'What is Nikto and it’s usages ?': 'https://www.geeksforgeeks.org/what-is-nikto-and-its-usages/',
                              'Nikto: A Practical Website Vulnerability Scanner': 'https://securitytrails.com/blog/nikto-website-vulnerability-scanner', 'Nikto Official Docs': 'https://github.com/sullo/nikto/wiki'})


def nuclei():
    os.system("clear")
    github = "Nuclei is a fast vulnerability scanner designed to probe modern applications, infrastructure, cloud platforms, and networks, aiding in the identification and mitigation of exploitable vulnerabilities.At its core, Nuclei uses templates—expressed as straightforward YAML files, that delineate methods for detecting, ranking, and addressing specific security flaws."
    template.template("nuclei", "nuclei", github.strip(), {"Nuclei - Automated Vulnerability Scanning Tool": "https://allabouttesting.org/nuclei-automated-vulnerability-scanning-tool/", "Nuclei – Fast and Customizable Vulnerability Scanner": "https://www.geeksforgeeks.org/nuclei-fast-and-customizable-vulnerability-scanner/",
                              "Gauing+Nuclei for Instant Bounties": "https://infosecwriteups.com/gauing-nuclei-for-instant-bounties-7a8a07979fff ", "DevSecOps 101 Part 3: Scanning Live Web Applications with Nuclei": "https://escape.tech/blog/devsecops-part-iii-scanning-live-web-applications"})

def ffuf():
    os.system("clear")
    github = "ffuf - Fuzz Faster U Fool.The usage examples below show just the simplest tasks you can accomplish using ffuf."
    template.template("ffuf", "ffuf", github.strip(), {"How to Fuzz Web Applications using FFuf – Web Security Tutorial": "https://www.freecodecamp.org/news/web-security-fuzz-web-applications-using-ffuf/",
                                                               "github fuff": "https://github.com/ffuf/ffuf/blob/master/README.md", })
        


def burp_suite():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Burp Suite")
        banner.description("Burp Suite is an integrated platform for performing security testing of web applications. Its various tools work seamlessly together to support the entire testing process, from initialmapping and analysis of an application's attack surface, through to finding and exploiting security vulnerabilities. Burp gives you full control, letting you combine advanced manual techniques with state-of-the-art automation, to make your work faster, more effective, and more fun.")
        ask = template.tool_writeups("burp", " ", " ")
        if ask == "1":
            try:
                professional = input(
                    f"{colors.blue}[+] Do You Want It's Professional Version?(Y/N){colors.reset}")
            except KeyboardInterrupt:
                return
            if professional == "y" or professional == "Y" or professional == "Yes" or professional == "yes":
                # clone repo
                path = 'Burp-Suite'
                isExist = os.path.exists(path)
                if isExist:
                    print(f"{colors.green}[+] It Is Installed{colors.reset}")
                    try:
                        professional = input(
                            f"{colors.blue}[+] Do You Want Run It?(Y/N){colors.reset}")
                    except KeyboardInterrupt:
                        return
                    if professional == "y" or professional == "Y" or professional == "Yes" or professional == "yes":
                        print(
                            f"{colors.yellow}[+] Please Wait....{colors.reset}")
                        os.system(
                            "cd Burp-Suite && bash installed.sh > /dev/null 2>&1")
                else:
                    os.system(
                        "git clone https://github.com/hardikhacker/Burp-Suite")
                    try:
                        professional = input(
                            f"{colors.blue}[+] Do You Want Run It?(Y/N){colors.reset}")
                    except:
                        template.exit_program()
                    if professional == "y" or professional == "Y" or professional == "Yes" or professional == "yes":
                        print(
                            f"{colors.yellow}[+] Please Wait....{colors.reset}")
                        os.system(
                            "cd Burp-Suite && chmod +x * && ./Kali_Linux_Setup.sh > /dev/null 2>&1")
            else:
                print(
                    f"{colors.blue}[+] CHECKING OF COMMUNITY VERSION IS INSTALLED OR NOT{colors.reset}")
                # check for installation
                template.check_installed("burpsuite", "burpsuite")
                waiting.waiting()
        elif ask == "2":
            # first argument for dictionary(key=title,value=url) second argument for banner
            writeup.writeup({"Setting up Burpsuite Professional": "https://github.com/THECH13F/Burp-Suite/blob/main/Readme.md","Top 10 tips for burpsuite": "https://medium.com/r3d-buck3t/top-10-tips-for-burp-suite-72212d22328f", "Setting up burbsuite": "https://thexssrat.medium.com/setting-up-burp-suite-b0a6767d3408", "Burp Suite: Do I need the professional edition?":
                            "https://thexssrat.medium.com/burp-suite-do-i-need-the-professional-edition-bf8c87ce236e", "Burp Suite Extensions to help you Pentest": "https://medium.com/codex/burp-suite-extensions-to-help-you-pentest-97f22a7d7d4d", "FIND MORE resources here": "https://medium.com/search?q=burpsuite"}, "Brup Suit writeup.writeup")
        elif ask == "3":
            template.uninstall_tool("","burp")
        else:
            break


def owasp_zap():
    os.system("clear")
    github = "The OWASP Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications.It is designed to be used by people with a wide range of security experience and as such is ideal for developers and functional testers who are new to penetration testing as well as being a useful addition to an experienced pen testers toolbox. https://www.owasp.org/index.php/ZAP"
    template.template('zaproxy', 'zaproxy', github.strip(), {"How to setup OWASP ZAP to scan your web application for security vulnerabilities": "https://www.linkedin.com/pulse/how-setup-owasp-zap-scan-your-web-application-security-botla/", "Authenticated Scan using OWASP-ZAP in Windows.": "https://medium.com/@secureica/authenticated-scan-using-owasp-zap-f0a71dafe41",
                      "OWASP ZAP: 6 Key Capabilities and a Quick Tutorial": "https://www.hackerone.com/knowledge-center/owasp-zap-6-key-capabilities-and-quick-tutorial", "Initial Setup": "https://infosecgirls.gitbook.io/infosecgirls-training/v/appsec/initial-setup-with-owasp-zap/untitled", "Setup OWASP ZAP": "https://infosecgirls.gitbook.io/infosecgirls-training/v/appsec/initial-setup-with-owasp-zap/setup-owasp-zap"})


def nessus():
    os.system("clear")
    version_grab = github_getting_text("https://www.tenable.com/downloads/nessus?loginAttempted=true",
                                          'div[class="multi-select__single-value css-1uccc91-singleValue"]', 0).strip()
    version = version_grab.strip().replace(" ", "")
    github = "Nessus is a platform developed by Tenable that scans for security vulnerabilities in devices, applications, operating systems, cloud services and other network resources.Originally launched as an open source tool in 1998, its enterprise edition became a commercial product in 2005. Nessus now encompasses several products that automate point-in-time vulnerability assessments of a network's attack surface, with the goal of enabling enterprise IT teams to stay ahead of cyber attackers by proactively identifying and fixing vulnerabilities as the tool discovers them, rather than after attackers exploit them.Nessus identifies software flaws, missing patches, malware, denial-of-service vulnerabilities, default passwords and misconfiguration errors, among other potential flaws. When Nessus discovers vulnerabilities, it issues an alert that IT teams can then investigate and determine what -- if any -- further action is required."
    template.template("nessus", "nessus", github.strip(), {"How To: Run Your First Vulnerability Scan with Nessus": "https://www.tenable.com/blog/how-to-run-your-first-vulnerability-scan-with-nessus", "A brief introduction to the Nessus vulnerability scanner": "https://resources.infosecinstitute.com/topic/a-brief-introduction-to-the-nessus-vulnerability-scanner/",
                      "Beginner’s Guide to Nessus": "https://www.hackingarticles.in/beginners-guide-to-nessus/", "Nessus Ubuntu Installation and Tutorial": "https://linuxhint.com/nessus-ubuntu-installation-tutorial/"}, link=f"https://www.tenable.com/downloads/api/v2/pages/nessus/files/{version}-debian10_amd64.deb", method="deb")



def dirb():
    os.system("clear")
    github = "DIRB IS a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching a dictionary basesd attack against a web server and analizing the response"
    template.template("dirb", "dirb", github.strip(), {"Dirb — A web content scanner": "https://medium.com/tech-zoom/dirb-a-web-content-scanner-bc9cba624c86", "Footprinting and Reconnaissance with DIRB Tool (For Security Researcher and Bug Bounty Hunters":
                      "https://www.openbugbounty.org/blog/mas00712/footprinting-and-reconnaissance-with-dirb-tool-for-security-researcher-and-bug-bounty-hunters/", "Comprehensive Guide on Dirb Tool": "https://www.hackingarticles.in/comprehensive-guide-on-dirb-tool/"})


def dirsearch():
    os.system("clear")
    github = "As a feature-rich tool, dirsearch gives users the opportunity to perform a complex web content discovering, with many vectors for the wordlist, high accuracy, impressive performance, advanced connection/request settings, modern brute-force techniques and nice output."
    template.template("dirsearch", "dirsearch --help ", github.strip(), {"Dirserach helpfile": "https://www.kali.org/tools/dirsearch/",
                      "Find Hidden Web Directories with Dirsearch ": "https://null-byte.wonderhowto.com/how-to/find-hidden-web-directories-with-dirsearch-0201615/", })


def wapiti():
    os.system("clear")
    github = github_getting_text("https://wapiti-scanner.github.io/", 'p', 6)
    github = re.sub(r'\s+', ' ', github).strip()
    template.template("wapiti", "wapiti", github.strip(), {"wapiti free web application vulnerability scanner": "https://pentestit.medium.com/wapiti-free-web-application-vulnerability-scanner-ce7712adf644", "Official docs": "https://github.com/wapiti-scanner/wapiti", "wapiti tutorial":
                      "https://www.kalilinux.in/2021/01/wapiti-tutorial.html", "complete guide to using wapiti web vulnerability scanner to keep your web applications websites secure": "https://linuxsecurity.com/features/complete-guide-to-using-wapiti-web-vulnerability-scanner-to-keep-your-web-applications-websites-secure"})


if __name__ == "__main__":
    main()
