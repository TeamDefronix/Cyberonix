from xml.dom.minidom import parse
from main.tools import banner, colors, template
import os
import requests
from bs4 import BeautifulSoup


def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Information_gathering")
        list_attacks = [
            " Useful Website",
            " Nmap     \t\t (Recommended)",
            " subfinder \t\t (Recommended)",
            " Maltego \t\t (Recommended)",
            " Dracnmap",
            " RED_HAWK",
            " Th3inspector \t (Recommended)",
            " Hping3",
            " Arping",
            "Netdiscover",
            "The Harvester",
            "Wafw00f",
            "Recon-ng",
            "Spiderfoot",
            "amass",
            "Sublist3r",
            "go back",
        ]
        for i in range(len(list_attacks)):
            print(colors.options, f"{i+1}) {list_attacks[i]}".title(), colors.reset)
        try:
            option = input(
                f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            return
        if option == "1":
            print("\n[+] Useful Websites")
            os.system("clear")
            template.template("Useful Websites", "no-tools", 'This is website for information gathering', {
                " Social-Search Website": "https://www.social-searcher.com/",
                " IP2info": "https://ipinfo.io/",
                " Viewdns": "https://viewdns.info/",
                " Shodan search engine": "https://www.shodan.io/",
                " Hunter Search Engine": "https://hunter.how/",
                " AHMIA Search Engine": "https://ahmia.fi/",
                " Censys Search Engine": "https://censys.com/",
                " Wayback Machine": "https://archive.org/web/",
                " Dnsdumpster": "https://dnsdumpster.com/",
                "MXToolbox": "https://mxtoolbox.com/",
                "Lopseg": "https://www.lopseg.com.br/osint",
                "Arin whois": "https://whois.arin.net/ui/",
                "Dnschecker": "https://dnschecker.org/",
                "BGP-Toolkit": "https://bgp.he.net/",
                "Mattw.io": "https://mattw.io/",
                "Searchftps": "https://www.searchftps.net/",
                "Security Headers": "https://securityheaders.com/",
                "Robtex": "https://www.robtex.com/",
                "Builtwith": "https://builtwith.com/",
                "Intodns": "https://www.intodns.com/",
                "Serachdns": "https://searchdns.netcraft.com/",
                "Hackertarget": "https://hackertarget.com/",
                "Vulners": "https://vulners.com/",
                "cvedetails": "https://www.cvedetails.com/",
                "Zero Day initiative": "https://www.zerodayinitiative.com/",


            })

        elif option == "2":
            print("\n[+] Nmap")
            nmap()
        elif option == "3":
            print("\n[+] subfinder")
            subfinder()
        elif option == "4":
            print("\n[+] Maltego")
            maltego()
        elif option == "5":
            print("\n[+] Dracnmap")
            dracnmap()
        elif option == "6":
            print("\n[+] RED_HAWK")
            redhawk()
        elif option == "7":
            print("\n[+] Th3inspector")
            th3inspector()
        elif option == "8":
            print("\n[+] Hping3")
            hping3()
        elif option == "9":
            print("\n[+] Arping")
            arping()
        elif option == "10":
            print("\n[+] Netdiscover")
            netdiscover()
        elif option == "11":
            print("\n[+] The Harvester")
            theharvester()
        elif option == "12":
            print("\n[+] Wafw00f")
            wafw00f()
        elif option == "13":
            print("\n[+] Recon-ng")
            recon_ng()
        elif option == "14":
            print("\n[+] spiderfoot")
            spiderfoot()
        elif option == "15":
            print("\n[+] amass")
            amass()
        elif option == "16":
            print("\n[+] Sublist3r")
            sublist3r()
        else:
            return


def github_getting_text(link, selector, indexvalue):
    print("Please Wait....\r", end="")
    URL = link
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    try:
        r = requests.get(URL,headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        paras = soup.select(selector)
    #for i in paras:
    #    print(i.text)
    # check index value from test file
        return paras[indexvalue].text
    except:
        return f"{colors.red}Not Loaded Because No Internet Connection{colors.reset}"

def arping():
    os.system("clear")
    github = "arping is a tool for probing hosts in a network. Unlike the ping command, which operates at the network layer, arping operates at the data link layer and uses the Address Resolution Protocol (ARP). Using it involves sending ARP requests to a destination host and waiting for ARP replies."        
    template.template(
                "arping",
                "arping --help",
                github.strip(),
                {
                    "First resource": "https://www.networkworld.com/article/3601693/using-the-linux-arping-command-to-ping-local-systems.html",
                    "How to use this command": "https://linuxhint.com/use-arping-command-linux/",
                    "Other resources": "https://www.baeldung.com/linux/arping-command",
                },
            )
def wafw00f():
    os.system("clear")
    github = "WAFW00F is a Python tool to help you fingerprint and identify Web Application Firewall (WAF) products. It is an active reconnaissance tool as it actually connects to the web server, but it starts out with a normal HTTP response and escalates as necessary."
    template.template(
                "wafw00f",
                "wafw00f --help",
                github.strip(),
                {
                    "First resource": "https://www.briskinfosec.com/tooloftheday/toolofthedaydetail/wafw00f-tool-to-fingerprint-and-identify-web-application-firewall",
                    "Second resource": "https://null-byte.wonderhowto.com/how-to/identify-web-application-firewalls-with-wafw00f-nmap-0198145/",
                    "Third resource": "https://www.geeksforgeeks.org/identification-of-web-application-firewall-using-wafw00f-in-kali-linux/",
                    "Github resource": "https://github.com/EnableSecurity/wafw00f",
                    "Video resource": "https://www.youtube.com/watch?v=EmWXfq51pE0",
                },
            )


def nmap():
    os.system("clear")
    github = "Nmap (Network Mapper) is a network scanner created by Gordon Lyon (also known by his pseudonym Fyodor Vaskovich). Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses. "
    template.template("nmap", "nmap -h", github.strip(), {"Nmap Cheat-Sheet": "https://www.stationx.net/nmap-cheat-sheet/",
                      "Official website": "https://nmap.org/ ", "Other resources": "https://linux.die.net/man/1/nmap", },)


def recon_ng():
    os.system("clear")
    github_p1 = github_getting_text(
        "https://github.com/lanmaster53/recon-ng", 'p[dir=auto]', 1)
    github_p2 = github_getting_text(
        "https://github.com/lanmaster53/recon-ng", 'p[dir=auto]', 2)
    github = github_p1+github_p2
    template.template("recon-ng", "recon-ng --help", github.strip(),
                      {"How to us Reco-ng": "https://hackertarget.com/recon-ng-tutorial/", },)


def theharvester():
    os.system("clear")
    github = "theHarvester is a simple to use, yet powerful tool designed to be used during the reconnaissance stage of a red team assessment or penetration test. It performs open source intelligence (OSINT) gathering to help determine a domain's external threat landscape. The tool gathers names, emails, IPs, subdomains, and URLs by using multiple public resources that include."
    template.template(
        "theharvester",
        "theharvester",
        github.strip(),
        {
            "The harvester CheatSheet": "https://cheatography.com/classassignment124/cheat-sheets/theharvester-cheat-sheet/",
            "How to use ": "https://thecybersecurityman.com/2018/08/01/pentest-edition-using-theharvester-to-gather-e-mail-accounts-subdomains-hosts-linkedin-users-banner-information-and-more/",
            "Information Gathering using theHarvester in Kali Linux": "https://www.hacking-tutorial.com/tips-and-trick/information-gathering-using-theharvester-in-kali-linux/#google_vignette",
            "theHarvester: a Classic Open Source Intelligence Tool": "https://securitytrails.com/blog/theharvester-tool",
            "The Harvester OSINT Reconnaissance": "https://medium.com/hacker-toolbelt/the-harvester-osint-reconnaissance-91a18a294a30", },)


def subfinder():
    os.system("clear")
    github = "subfinder is a subdomain discovery tool that returns valid subdomains for websites, using passive online sources. It has a simple, modular architecture and is optimized for speed. subfinder is built for doing one thing only - passive subdomain enumeration, and it does that very well."
    template.template(
        "subfinder",
        "subfinder",
        github.strip(),
        {
            "subfinder CheatSheet": "https://highon.coffee/blog/subfinder-cheat-sheet/",
            "How to use ": "https://blog.projectdiscovery.io/do-you-really-know-subfinder-an-in-depth-guide-to-all-features-of-subfinder-beginner-to-advanced/",
            "Uncover the Hidden Web: Discover the Power of Subfinder for Efficient Subdomain Enumeration": "https://medium.com/@cuncis/uncover-the-hidden-web-discover-the-power-of-subfinder-for-efficient-subdomain-enumeration-aad6fc05bcdd", },)


def sublist3r():
    os.system("clear")
    github = "Sublist3r is a python tool designed to enumerate subdomains of websites using OSINT. It helps penetration testers and bug hunters collect and gather subdomains for the domain they are targeting. Sublist3r enumerates subdomains using many search engines such as Google, Yahoo, Bing, Baidu and Ask. Sublist3r also enumerates subdomains using Netcraft, Virustotal, ThreatCrowd, DNSdumpster and ReverseDNS."
    template.template(
        "sublist3r",
        "sublist3r -h",
        github.strip(),
        {
            "Sublist3r Cheatsheet": "https://github.com/shreyaschavhan/pentest-tools-cheatsheet/blob/main/sublist3r.md",
            "Sublist3r – Fast Subdomains Enumeration Tool for Penetration Testers": "https://pentesttools.net/sublist3r-fast-subdomains-enumeration-tool-for-penetration-testers/", },)


def spiderfoot():
    os.system("clear")
    github = github_getting_text(
        "https://github.com/smicallef/spiderfoot", 'p[dir=auto]', 2)
    template.template(
        "spiderfoot",
        "spiderfoot --help",
        github.strip(),
        {
            "How to use Spiderfoot ": "https://www.geeksforgeeks.org/spiderfoot-a-automate-osint-framework-in-kali-linux/",
        },)


def amass():
    os.system("clear")
    github = "The OWASP Amass Project performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques."
    template.template(
        "amass",
        "amass --help",
        github.strip(),
        {
            "Amass tutorial": "https://techyrick.com/amass-full-tutorial/",
            "How to use amass ": "https://blog.intigriti.com/2021/06/08/hacker-tools-amass-hunting-for-subdomains/",
            "amass user's guide": "https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md", },)


def netdiscover():
    os.system("clear")
    github = "Netdiscover is a command-line oriented TCP/IP packet assembler/analyzer. It supports TCP, UDP, ICMP and RAW-IP protocols, has a traceroute mode, the ability to send files between a covered channel, and many other features."
    template.template(
        "netdiscover",
        "netdiscover -help",
        github.strip(),
        {
            "Usage in details": "https://linuxcommandlibrary.com/man/netdiscover",
            "Second resource": "https://www.cyberpratibha.com/blog/netdiscover/",
            "Video resources": "https://www.youtube.com/watch?v=yMSq7QzQcX4", },)


def maltego():
    os.system("clear")
    github = "Maltego is software used for open-source intelligence and forensics, developed by Paterva from Pretoria, South Africa. Maltego focuses on providing a library of transforms for discovery of data from open sources, and visualizing that information in a graph format, suitable for link analysis and data mining"
    template.template(
        "maltego",
        "maltego",
        github.strip(),
        {
            "Official website": "https://www.maltego.com/ ",
            "How to use it": "https://www.geeksforgeeks.org/maltego-tool-in-kali-linux/ ",
            "How to Conduct Person of Interest Investigations Using OSINT and Maltego": "https://www.maltego.com/blog/how-to-conduct-person-of-interest-investigations-using-osint-and-maltego/",
            "How to Use Maltego: A Beginner’s Guide to OSINT Analysis": "https://www.stationx.net/how-to-use-maltego/",
            "How to use Maltego": "https://medium.com/hengky-sanjaya-blog/how-to-use-maltego-f57fe77e36e2",
            "Other resources": "https://www.cybervie.com/blog/what-is-maltego-how-to-use-it-for-information-gathering/", }, )


def dracnmap():
        os.system("clear")
        github = "Dracnmap is an open source program which is using to exploit the network and gathering information with nmap help. Nmap command comes with lots of options that can make the utility more robust and difficult to follow for new users. Hence Dracnmap is designed to perform fast scaning with the utilizing script engine of nmap and nmap can perform various automatic scanning techniques with the advanced commands."
        template.template(
                "Dracnmap",
                "./dracnmap-v2.2.sh",
                github.strip(),
                {
                    "Github website": "https://github.com/Screetsec/Dracnmap",
                    "How to use": "https://www.geeksforgeeks.org/dracnmap-information-gathering-and-network-exploitation-tool/ ",
                    "Other resources": "https://www.hacking.land/2016/10/dracnmap-exploit-network-and-gathering.html?utm_source=dlvr.it&utm_medium=facebook&m=1 ",
                },
                method="github",
                github_install="git clone https://github.com/Screetsec/Dracnmap.git && cd Dracnmap && chmod +x dracnmap-v2.2.sh",
                github_check="Dracnmap",
            )
        

def redhawk():
        os.system("clear")
        github = "Red Hawk is a free and open-source tool available on GitHub. Red Hawk is used to scanning websites for information gathering and finding vulnerabilities. Red Hawk is written in PHP. It uses PHP script to do reconnaissance. Red Hawk is so powerful that it can detect content management system while scanning, it can detect IP address, it can detect webserver record, it can detect Cloudflare information, and can detect robots.txt. Red Hawk can detect WordPress, Drupal, Joomla, and Magento CMS. Red Hawk looks for error-based SQL injections, WordPress sensitive files, and WordPress version-related vulnerabilities. RedHawk uses different modules for doing all the scannings."
        template.template(
                "RED_HAWK",
                "php rhawk.php",
                github.strip(),
                {
                    "How to use": "https://systemweakness.com/red-hawk-an-information-gathering-tool-d12a66da7c63 ",
                    "Other resources": "https://www.geeksforgeeks.org/red-hawk-information-gathering-and-vulnerability-scanning-tool-in-kali-linux/ ",
                },
                method="github",
                github_install="git clone https://github.com/Tuhinshubhra/RED_HAWK.git",
                github_check="RED_HAWK",
            )

def th3inspector():
        os.system("clear")
        github = "Th3inspector is an open source program which is using to exploit the network and gathering information with nmap help. Nmap command comes with lots of options that can make the utility more robust and difficult to follow for new users. Hence Dracnmap is designed to perform fast scaning with the utilizing script engine of nmap and nmap can perform various automatic scanning techniques with the advanced commands."
        template.template(
                "Th3inspector",
                "perl Th3inspector.pl",
                github.strip(),
                {
                    "github Website": "https://github.com/Moham3dRiahi/Th3inspector ",
                    "First resource": "https://www.geeksforgeeks.org/th3inspector-osint-tool-for-reconnaissance/ ",
                    "Second resource": "https://pentesttools.net/th3inspector-tool-for-information-gathering/",
                },
                method="github",
                github_install="git clone https://github.com/Moham3dRiahi/Th3inspector.git",
                github_check="Th3inspector",
            )

def hping3():
        os.system("clear")
        github = "hping is a command-line oriented TCP/IP packet assembler/analyzer. It supports TCP, UDP, ICMP and RAW-IP protocols, has a traceroute mode, the ability to send files between a covered channel, and many other features."
        template.template(
                "hping3",
                "hping3 -h",
                github.strip(),
                {
                    "First resource": "https://linux.die.net/man/8/hping3",
                    "Hping Tips and Tricks": "https://iphelix.medium.com/hping-tips-and-tricks-85698751179f",
                    "Hping3: Full tutorial from noob to pro": "https://techyrick.com/hping3-full-tutorial-for-dummies-to-pro/",
                },
            )


if __name__ == "__main__":
    main()
