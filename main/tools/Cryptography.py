from main.tools import banner,colors,template
import os
from main.tools import writeup
def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Cryptography Failure")
        list_root_attacks=["Tool","Writeups","go back"]
        for i in range(len(list_root_attacks)):
            print(colors.options, f"{i}) {list_root_attacks[i]}".title(), colors.reset)
        option = input(f"\n {colors.select}Select An Option ->{colors.reset}")
        if option == "0":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Tools")
                list_attacks=["SSLstript","Bettercap","Ettercap (Graphical of bettercap)","sslyze","O-Saft","sslscan","SSLLabs","go back"]
                for i in range(len(list_attacks)):
                    print(colors.options,f"{i}) {list_attacks[i]}".title(),colors.reset)
                option2 = input(f"\n {colors.select}Select An Option ->{colors.reset}")
                if option2=="0":
                    print(f"\n[+] SSLstript")
                    os.system("clear")
                    github = "SSLStrip is a powerful hacking tool that enables an attacker to intercept and manipulate HTTPS traffic between a user and a website. The tool works by downgrading HTTPS connections to insecure HTTP connections, which allows an attacker to eavesdrop on the traffic and steal sensitive information such as login credentials, credit card numbers, and other personal data. SSLStrip is commonly used in phishing attacks and other cybercriminal activities. It can be a potent weapon in the hands of skilled hackers who are looking to exploit vulnerabilities in web security."
                    template.template("sslstrip","sslstrip -h",github.strip(),{"SSLstrip Tutorial Beginner":"https://www.computerweekly.com/tip/Sslstrip-tutorial-for-penetration-testers","SSLstip how awesome tool is ts":"https://infosecwriteups.com/ssl-strip-how-awesome-it-is-a0eb79e28bcc","ARP Spoofing and SSL Stripping":"https://levelup.gitconnected.com/ethical-hacking-part-10-arp-spoofing-ssl-strip-ea5f0cc892f3"})
                elif option2=="1":
                    print(f"\n[+] Bettercap")
                    os.system("clear")
                    github = "Bettercap is a network security tool used for advanced network analysis, monitoring, and penetration testing. It allows users to sniff and intercept network traffic, perform man-in-the-middle attacks, and perform various other types of network-related exploits. Bettercap can be used for various tasks such as ARP spoofing, DNS spoofing, HTTP proxying, packet sniffing, password sniffing, and many more. The tool is highly customizable and offers a user-friendly interface. It is popular among security researchers and penetration testers due to its effectiveness and reliability."
                    template.template('bettercap','bettercap',github.strip(),{"HSTS Hijacking using Bettercap": "https://github.com/bettercap/caplets/blob/master/hstshijack/README.md","SSL Stripping by B14CKY": "https://www.youtube.com/watch?v=Peu0AEpHUVs",})
                elif option2=="2":
                    print("\n[+] Ettercap (Graphical of bettercap)")
                    os.system("clear")
                    github="Ettercap is a popular open-source GUI network security tool that is used for monitoring and analyzing network traffic in real-time. It can be used to perform various types of attacks such as ARP spoofing, IP and MAC address spoofing, session hijacking, DNS spoofing, etc. Ettercap is commonly used by network administrators and security experts to test the security of their own networks and to identify potential vulnerabilities. It supports various protocols like TCP, UDP, ICMP, and can also decode SSL traffic. Ettercap can be used on various operating systems including Windows, Linux, and Mac OS X."
                    template.template("ettercap-graphical","ettercap -h",github.strip(),{"SSLStriping Using Ettercap by NULL-BYTE': 'https://null-byte.wonderhowto.com/forum/struggling-perform-mitm-attack-using-ettercap-and-sslstrip-0165933/','HSTS Hijacing': 'https://github.com/bettercap/caplets/blob/master/hstshijack/README.md",})
                elif option2=="3":
                    print("\n[+] sslyze")
                    os.system("clear")
                    github="SSLyze is a Python-based command-line tool that helps in evaluating the SSL/TLS security posture of a given target. It allows users to analyze SSL/TLS configuration on a server and detect various security issues like weak ciphers, certificate issues, and misconfigurations. SSLyze is useful for system administrators, security professionals, and developers to test and evaluate the security of SSL/TLS implementations. It is an open-source tool and is available for free under the GPL v3 license."
                    template.template("sslyze","sslyze -h",github.strip(),{"SSLyze by GeeksforGeeks": "https://www.geeksforgeeks.org/sslyze-fast-and-powerful-ssl-tls-scanning-tool/","SSLlyze by Hackingvision": "https://hackingvision.com/2017/08/11/sslyze-fast-powerful-ssltls-server-scanning-library/","SSLyze by Securecodebox": "https://www.securecodebox.io/docs/scanners/sslyze/"},method="pip")
                elif option2=="4":
                    print(f"\n[+] O-Saft")
                    os.system("clear")
                    github="O-Saft is an open-source tool designed for analyzing and detecting the security configuration issues in web applications. It mainly focuses on the security headers and their misconfigurations, which might lead to security vulnerabilities. The tool scans the website and generates a report that contains information about the misconfigured security headers, their impact, and how to fix them. O-Saft helps the developers to ensure the security of their web applications and protect them from various cyber threats."
                    template.template("o-saft","o-saft --help",github.strip(),{"O-Soft by OWASP": "https://owasp.org/www-project-o-saft/","O-Soft by Kali": "https://www.kali.org/tools/o-saft/"})
                elif option2=="5":
                    print(f"\n[+] sslscan")
                    os.system("clear")
                    github = "SSLScan is a free tool that helps in identifying SSL/TLS vulnerabilities and misconfigurations in SSL/TLS enabled servers. It scans and evaluates the SSL/TLS connection on the target server and provides a detailed report of any weak ciphers, protocols or configurations that can be exploited by attackers. SSLScan is commonly used by security professionals and penetration testers to assess the security posture of an organization's SSL/TLS infrastructure. It is available for Windows, Linux, and MacOS platforms."
                    template.template("sslscan","sslscan",github.strip(),{"SSLSCAN by Oreilly": "https://www.oreilly.com/library/view/web-penetration-testing/9781788623377/285990a3-9992-40b0-ac36-69adc6fb47ce.xhtml","SSLSCAN by ALASTA": "https://www.alasta.com/tools/2016/07/26/tools-sslscan.html"})
                elif option2=="6":
                    print(f"\n[+] SSLLabs")
                    os.system("clear")
                    github = "Skipfish is an active web application security reconnaissance tool. It prepares an interactive sitemap for the targeted site by carrying out a recursive crawl and dictionary-based probes. The resulting map is then annotated with the output from a number of active (but hopefully non-disruptive) security checks. The final report generated by the tool is meant to serve as a foundation for professional web application security assessments."
                    template.template("SSLLabs (Website)","https://www.ssllabs.com/ssltest/",github.strip(),"no-writeups",method="browser")
                else:
                    break
        elif option == "1":
            os.system("clear")
            writeup.writeup({"A02-2021 Cryptographic Failures by OWASP":"https://owasp.org/Top10/A02_2021-Cryptographic_Failures/","Cryptographic Failures by Synack":"https://www.synack.com/blog/preventing-cryptographic-failures-the-no-2-vulnerability-in-the-owasp-top-10/","Cryptographic Failures by MYF5":"https://my.f5.com/manage/s/article/K00174750","Cryptographic Failures by Qawerk":"https://qawerk.com/blog/cryptographic-failure/"},"Cryptography Failure Write-UPS")
        else:
            return

if __name__ == "__main__":
    main()
