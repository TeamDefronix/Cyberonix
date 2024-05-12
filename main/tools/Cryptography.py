from main.tools import banner,colors,template,Sniffing_and_Spoofing
import os
from main.tools import writeup
def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Cryptography Failure")
        list_root_attacks=["Tool","Writeups","go back"]
        for i in range(len(list_root_attacks)):
            print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
        try:
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}")
        except KeyboardInterrupt:
            return
        if option == "1":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Tools")
                list_attacks=["Bettercap","Ettercap (Graphical of bettercap)","sslyze","O-Saft","sslscan","go back"]
                for i in range(len(list_attacks)):
                    print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
                try:
                    option2 = input(f"\n {colors.select}Select An Option ->  {colors.reset}")
                except KeyboardInterrupt:
                    return
                if option2=="1":
                    print(f"\n[+] Bettercap")
                    Sniffing_and_Spoofing.bettercap()
                elif option2=="2":
                    print("\n[+] Ettercap (Graphical of bettercap)")
                    ettercap()            
                elif option2=="3":
                    print("\n[+] sslyze")
                    sslyze()            
                elif option2=="4":
                    print(f"\n[+] O-Saft")
                    o_saft()                
                elif option2=="5":
                    print(f"\n[+] sslscan")
                    sslscan()
                else:
                    break
        elif option == "2":
            os.system("clear")
            writeup.writeup({"SSLLabs (Website)":"https://www.ssllabs.com/ssltest/","A02-2021 Cryptographic Failures by OWASP":"https://owasp.org/Top10/A02_2021-Cryptographic_Failures/","Cryptographic Failures by Synack":"https://www.synack.com/blog/preventing-cryptographic-failures-the-no-2-vulnerability-in-the-owasp-top-10/","Cryptographic Failures by MYF5":"https://my.f5.com/manage/s/article/K00174750","Cryptographic Failures by Qawerk":"https://qawerk.com/blog/cryptographic-failure/"},"Cryptography Failure Write-UPS")
        else:
            return

def sslscan():
    os.system("clear")
    github = "SSLScan is a free tool that helps in identifying SSL/TLS vulnerabilities and misconfigurations in SSL/TLS enabled servers. It scans and evaluates the SSL/TLS connection on the target server and provides a detailed report of any weak ciphers, protocols or configurations that can be exploited by attackers. SSLScan is commonly used by security professionals and penetration testers to assess the security posture of an organization's SSL/TLS infrastructure. It is available for Windows, Linux, and MacOS platforms."
    template.template("sslscan","sslscan",github.strip(),{"SSLSCAN by Oreilly": "https://www.oreilly.com/library/view/web-penetration-testing/9781788623377/285990a3-9992-40b0-ac36-69adc6fb47ce.xhtml"})
                
def o_saft():
    os.system("clear")
    github="O-Saft is an open-source tool designed for analyzing and detecting the security configuration issues in web applications. It mainly focuses on the security headers and their misconfigurations, which might lead to security vulnerabilities. The tool scans the website and generates a report that contains information about the misconfigured security headers, their impact, and how to fix them. O-Saft helps the developers to ensure the security of their web applications and protect them from various cyber threats."
    template.template("o-saft","o-saft --help",github.strip(),{"O-Soft by OWASP": "https://owasp.org/www-project-o-saft/","O-Soft by Kali": "https://www.kali.org/tools/o-saft/"})
                
def sslyze():
    os.system("clear")
    github="SSLyze is a Python-based command-line tool that helps in evaluating the SSL/TLS security posture of a given target. It allows users to analyze SSL/TLS configuration on a server and detect various security issues like weak ciphers, certificate issues, and misconfigurations. SSLyze is useful for system administrators, security professionals, and developers to test and evaluate the security of SSL/TLS implementations. It is an open-source tool and is available for free under the GPL v3 license."
    template.template("sslyze","sslyze -h",github.strip(),{"SSLyze by GeeksforGeeks": "https://www.geeksforgeeks.org/sslyze-fast-and-powerful-ssl-tls-scanning-tool/","SSLyze by Securecodebox": "https://www.securecodebox.io/docs/scanners/sslyze/"},method="pip")
                
def ettercap():
    os.system("clear")
    github="Ettercap is a popular open-source GUI network security tool that is used for monitoring and analyzing network traffic in real-time. It can be used to perform various types of attacks such as ARP spoofing, IP and MAC address spoofing, session hijacking, DNS spoofing, etc. Ettercap is commonly used by network administrators and security experts to test the security of their own networks and to identify potential vulnerabilities. It supports various protocols like TCP, UDP, ICMP, and can also decode SSL traffic. Ettercap can be used on various operating systems including Windows, Linux, and Mac OS X."
    template.template("ettercap-graphical","ettercap -G",github.strip(),{"SSLStriping Using Ettercap by NULL-BYTE": 'https://null-byte.wonderhowto.com/forum/struggling-perform-mitm-attack-using-ettercap-and-sslstrip-0165933/','HSTS Hijacing': "https://github.com/bettercap/caplets/blob/master/hstshijack/README.md",})
                
if __name__ == "__main__":
    main()
