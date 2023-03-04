from main.tools import banner,colors,template,waiting,writeup
import os,requests
import requests
from bs4 import BeautifulSoup

def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("WEB Application Analysis")
        list_attacks=["Burp Suite","Owasp ZAP","Nikto","Wapiti","Nessus","dirb","skipfish","Nuclei","go back"]
        for i in range(len(list_attacks)):
            print(colors.options,f"{i}) {list_attacks[i]}".title(),colors.reset)
        option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        if option=="0":
            print(f"\n[+] Burp Suite")
            os.system("clear")
            burp_suite()
            # github = "Burp Suite is an integrated platform for performing security testing of web applications. Its various tools work seamlessly together to support the entire testing process, from initialmapping and analysis of an application's attack surface, through to finding and exploiting security vulnerabilities. Burp gives you full control, letting you combine advanced manual techniques with state-of-the-art automation, to make your work faster, more effective, and more fun."
            # template.template("Burp-Suite","burp",github.strip(),{"Top 10 tips for burpsuite":"https://medium.com/r3d-buck3t/top-10-tips-for-burp-suite-72212d22328f","Setting up burbsuite":"https://thexssrat.medium.com/setting-up-burp-suite-b0a6767d3408","Burp Suite: Do I need the professional edition?":"https://thexssrat.medium.com/burp-suite-do-i-need-the-professional-edition-bf8c87ce236e","Burp Suite Extensions to help you Pentest":"https://medium.com/codex/burp-suite-extensions-to-help-you-pentest-97f22a7d7d4d","FIND MORE resources here":"https://medium.com/search?q=burpsuite"},link="https://github.com/hardikhacker/Burp-Suite",method="github")
        elif option=="1":
            print(f"\n[+] Owasp ZAP")
            os.system("clear")
            github = "The OWASP Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications.\nIt is designed to be used by people with a wide range of security experience and as such is ideal for developers and functional testers who are new to penetration testing as well as being a useful addition to an experienced pen testers toolbox. https://www.owasp.org/index.php/ZAP"
            template.template('zaproxy','zaproxy',github.strip(),{"How to setup OWASP ZAP to scan your web application for security vulnerabilities":"https://www.linkedin.com/pulse/how-setup-owasp-zap-scan-your-web-application-security-botla/","Authenticated Scan using OWASP-ZAP":"https://medium.com/@secureica/authenticated-scan-using-owasp-zap-f0a71dafe41","OWASP ZAP: 6 Key Capabilities and a Quick Tutorial":"https://www.hackerone.com/knowledge-center/owasp-zap-6-key-capabilities-and-quick-tutorial","Initial Setup":"https://infosecgirls.gitbook.io/infosecgirls-training/v/appsec/initial-setup-with-owasp-zap/untitled","Setup OWASP ZAP":"https://infosecgirls.gitbook.io/infosecgirls-training/v/appsec/initial-setup-with-owasp-zap/setup-owasp-zap"})
        elif option=="2":
            print("\n[+] Nikto")
            os.system("clear")
            github=github_getting_text("https://en.wikipedia.org/wiki/Nikto_(vulnerability_scanner)",'p',1)
            template.template("nikto","nikto -h",github.strip(),{'What is Nikto and it’s usages ?':'https://www.geeksforgeeks.org/what-is-nikto-and-its-usages/','Nikto: A Practical Website Vulnerability Scanner':'https://securitytrails.com/blog/nikto-website-vulnerability-scanner','Nikto Official Docs':'https://github.com/sullo/nikto/wiki'})
        elif option=="3":
            print("\n[+] Wapiti")
            os.system("clear")
            github=github_getting_text("https://github.com/wapiti-scanner/wapiti",'p[dir="auto"]',6)
            template.template("wapiti","wapiti",github.strip(),{"wapiti free web application vulnerability scanner":"https://pentestit.medium.com/wapiti-free-web-application-vulnerability-scanner-ce7712adf644","Official docs":"https://github.com/wapiti-scanner/wapiti","wapiti tutorial":"https://www.kalilinux.in/2021/01/wapiti-tutorial.html","complete guide to using wapiti web vulnerability scanner to keep your web applications websites secure":"https://linuxsecurity.com/features/complete-guide-to-using-wapiti-web-vulnerability-scanner-to-keep-your-web-applications-websites-secure"})
        elif option=="4":
            print(f"\n[+] Nessus")
            os.system("clear")
            github=github_getting_text("https://www.techtarget.com/searchnetworking/definition/Nessus",'section[id="content-body"]',0)
            template.template("Nessus","nessus",github.strip(),{"How To: Run Your First Vulnerability Scan with Nessus":"https://www.tenable.com/blog/how-to-run-your-first-vulnerability-scan-with-nessus","A brief introduction to the Nessus vulnerability scanner":"https://resources.infosecinstitute.com/topic/a-brief-introduction-to-the-nessus-vulnerability-scanner/","Beginner’s Guide to Nessus":"https://www.hackingarticles.in/beginners-guide-to-nessus/","Nessus Ubuntu Installation and Tutorial":"https://linuxhint.com/nessus-ubuntu-installation-tutorial/"},link="https://www.tenable.com/downloads/api/v2/pages/nessus/files/Nessus-10.4.2-debian9_amd64.deb",method="deb")
        elif option=="5":
            print(f"\n[+] dirb")
            os.system("clear")
            github = "DIRB IS a Web Content Scanner. It looks for existing (and/or hidden) Web Objects. It basically works by launching a dictionary basesd attack against a web server and analizing the response"
            template.template("dirb","dirb",github.strip(),{"Dirb — A web content scanner":"https://medium.com/tech-zoom/dirb-a-web-content-scanner-bc9cba624c86","Footprinting and Reconnaissance with DIRB Tool (For Security Researcher and Bug Bounty Hunters":"https://www.openbugbounty.org/blog/mas00712/footprinting-and-reconnaissance-with-dirb-tool-for-security-researcher-and-bug-bounty-hunters/","Comprehensive Guide on Dirb Tool":"https://www.hackingarticles.in/comprehensive-guide-on-dirb-tool/"})
        elif option=="6":
            print(f"\n[+] skipfish")
            os.system("clear")
            github = "Skipfish is an active web application security reconnaissance tool. It prepares an interactive sitemap for the targeted site by carrying out a recursive crawl and dictionary-based probes. The resulting map is then annotated with the output from a number of active (but hopefully non-disruptive) security checks. The final report generated by the tool is meant to serve as a foundation for professional web application security assessments."
            template.template("skipfish","skipfish -h",github.strip(),{"Skipfish in Kali Linux":"https://www.javatpoint.com/skipfish-in-kali-linux","Skipfish – Penetration Testing tool in Kali Linux":"https://www.geeksforgeeks.org/skipfish-penetration-testing-tool-in-kali-linux/","skipfish (1) - Linux Man Pages":"https://www.systutorials.com/docs/linux/man/1-skipfish/","Skipfish – Web Application Security Scanner for XSS, SQL Injection, Shell injection":"https://gbhackers.com/skipfish-web-application-security-scanner/"})
        elif option=="7":
            print(f"\n[+] Nuclei")
            os.system("clear")
            github=github_getting_text("https://github.com/projectdiscovery/nuclei",'p[dir="auto"]',3)
            template.template("nuclei","nuclei -h",github.strip(),{"Nuclei - Automated Vulnerability Scanning Tool":"https://allabouttesting.org/nuclei-automated-vulnerability-scanning-tool/","Nuclei – Fast and Customizable Vulnerability Scanner":"https://www.geeksforgeeks.org/nuclei-fast-and-customizable-vulnerability-scanner/","Gauing+Nuclei for Instant Bounties":"https://infosecwriteups.com/gauing-nuclei-for-instant-bounties-7a8a07979fff ","DevSecOps 101 Part 3: Scanning Live Web Applications with Nuclei":"https://escape.tech/blog/devsecops-part-iii-scanning-live-web-applications"},link="https://github.com/projectdiscovery/nuclei@latest",method="go")
        else:
            return

def github_getting_text(link,selector,indexvalue):
    print(f"Please Wait....\r",end="")
    URL = link
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        paras = soup.select(selector)
        #check index value from test file
        return paras[indexvalue].text
    except:
        return "{colors.red}NotLloaded Because No Internet Connection{colors.reset}"
def burp_suite():
        while True:
            os.system("clear")
            banner.main()
            banner.attack("Burp Suite")
            banner.description("Burp Suite is an integrated platform for performing security testing of web applications. Its various tools work seamlessly together to support the entire testing process, from initialmapping and analysis of an application's attack surface, through to finding and exploiting security vulnerabilities. Burp gives you full control, letting you combine advanced manual techniques with state-of-the-art automation, to make your work faster, more effective, and more fun.")
            ask=template.tool_writeups("burp"," "," ")
            if ask=="1":
                    professional=input(f"{colors.blue}[+] Do You Want It's Professional Version?(Y/N){colors.reset}")
                    if professional=="y" or professional=="Y" or professional=="Yes" or professional=="yes":
                        #clone repo
                        path = 'Burp-Suite'
                        isExist = os.path.exists(path)
                        if isExist:
                            print(f"{colors.green}[+] It Is Installed{colors.reset}")
                            professional=input(f"{colors.blue}[+] Do You Want Run It?(Y/N){colors.reset}")
                            if professional=="y" or professional=="Y" or professional=="Yes" or professional=="yes":
                                print(f"{colors.yellow}[+] Please Wait....{colors.reset}")
                                os.system("cd Burp-Suite && bash installed.sh > /dev/null 2>&1")
                        else:
                            os.system("git clone https://github.com/hardikhacker/Burp-Suite")
                            professional=input(f"{colors.blue}[+] Do You Want Run It?(Y/N){colors.reset}")
                            if professional=="y" or professional=="Y" or professional=="Yes" or professional=="yes":
                                print(f"{colors.yellow}[+] Please Wait....{colors.reset}")
                                os.system("cd Burp-Suite && chmod +x * && ./Kali_Linux_Setup.sh > /dev/null 2>&1")
                    else:
                        print(f"{colors.blue}[+] CHECKING OF COMMUNITY VERSION IS INSTALLED OR NOT{colors.reset}")
                        #check for installation
                        template.check_installed("burpsuite","burpsuite")
                        waiting.waiting()
            elif ask=="2":
                #first argument for dictionary(key=title,value=url) second argument for banner 
                writeup.writeup({"Top 10 tips for burpsuite":"https://medium.com/r3d-buck3t/top-10-tips-for-burp-suite-72212d22328f","Setting up burbsuite":"https://thexssrat.medium.com/setting-up-burp-suite-b0a6767d3408","Burp Suite: Do I need the professional edition?":"https://thexssrat.medium.com/burp-suite-do-i-need-the-professional-edition-bf8c87ce236e","Burp Suite Extensions to help you Pentest":"https://medium.com/codex/burp-suite-extensions-to-help-you-pentest-97f22a7d7d4d","FIND MORE resources here":"https://medium.com/search?q=burpsuite"},"Brup Suit writeup.writeup")
            else:
                break

if __name__ == "__main__": 
    main()
