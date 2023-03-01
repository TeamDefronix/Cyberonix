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
            " Nmap",
            " Maltego",
            " Dracnmap",
            " RED_HAWK",
            " Th3inspector",
            " Hping3",
            " Arping",
            " Netdiscover",
            " Wafw00f",
            " go back",
        ]
        for i in range(len(list_attacks)):
            print(colors.options, f"{i}) {list_attacks[i]}".title(), colors.reset)
        option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        if option == "0":
            print("\n[+] Nmap")
            os.system("clear")
            # name,command,discription,writeup,link=True,method="kali",github_install="",github_check=True
            github = "Nmap (Network Mapper) is a network scanner created by Gordon Lyon (also known by his pseudonym Fyodor Vaskovich). Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses. "
            template.template(
                "Nmap",
                "nmap -h",
                github.strip(),
                {
                    "Nmap Cheat-Sheet": "https://www.stationx.net/nmap-cheat-sheet/",
                    "Official website": "https://nmap.org/ ",
                    "Other resources": "https://linux.die.net/man/1/nmap",
                },
            )
        elif option == "1":
            print("\n[+] Maltego")
            os.system("clear")
            github = "Maltego is software used for open-source intelligence and forensics, developed by Paterva from Pretoria, South Africa. Maltego focuses on providing a library of transforms for discovery of data from open sources, and visualizing that information in a graph format, suitable for link analysis and data mining"
            template.template(
                "Maltego",
                "maltego",
                github.strip(),
                {
                    "Official website": "https://www.maltego.com/ ",
                    "How to use it": "https://www.geeksforgeeks.org/maltego-tool-in-kali-linux/ ",
                    "Other resources": "https://www.cyberpratibha.com/information-gathering-with-maltego/ ",
                },
            )
        elif option == "2":
            print("\n[+] Dracnmap")
            os.system("clear")
            github = "Dracnmap is an open source program which is using to exploit the network and gathering information with nmap help. Nmap command comes with lots of options that can make the utility more robust and difficult to follow for new users. Hence Dracnmap is designed to perform fast scaning with the utilizing script engine of nmap and nmap can perform various automatic scanning techniques with the advanced commands."
            template.template(
                "Dracnmap",
                "chmod +x dracnmap-v2.2.sh && ./dracnmap-v2.2.sh",
                github.strip(),
                {
                    "Github website": "https://github.com/Screetsec/Dracnmap",
                    "How to use": "https://www.geeksforgeeks.org/dracnmap-information-gathering-and-network-exploitation-tool/ ",
                    "Other resources": "https://www.hacking.land/2016/10/dracnmap-exploit-network-and-gathering.html?utm_source=dlvr.it&utm_medium=facebook&m=1 ",
                },
                method="github",
                github_install="git clone https://github.com/Screetsec/Dracnmap.git",
                github_check="Dracnmap",
            )
        elif option == "3":
            print("\n[+] RED_HAWK")
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
        elif option == "4":
            print("\n[+] Th3inspector")
            os.system("clear")
            github = "Th3inspector is an open source program which is using to exploit the network and gathering information with nmap help. Nmap command comes with lots of options that can make the utility more robust and difficult to follow for new users. Hence Dracnmap is designed to perform fast scaning with the utilizing script engine of nmap and nmap can perform various automatic scanning techniques with the advanced commands."
            template.template(
                "Th3inspector",
                "perl Th3inspector.pl",
                github.strip(),
                {
                    "github Website": "https://github.com/Moham3dRiahi/Th3inspector ",
                    "First resource": "https://www.geeksforgeeks.org/red-hawk-information-gathering-and-vulnerability-scanning-tool-in-kali-linux/ ",
                    "Second resource": "https://pentesttools.net/th3inspector-tool-for-information-gathering/",
                },
                method="github",
                github_install="git clone https://github.com/Moham3dRiahi/Th3inspector.git",
                github_check="Th3inspector",
            )
        elif option == "5":
            print("\n[+] Hping3")
            os.system("clear")
            github = "hping is a command-line oriented TCP/IP packet assembler/analyzer. It supports TCP, UDP, ICMP and RAW-IP protocols, has a traceroute mode, the ability to send files between a covered channel, and many other features."
            template.template(
                "Hping3",
                "hping3 -h",
                github.strip(),
                {
                    "First resource": "https://hacksheets.in/all-categories/useful-resources-main/hping3/"
                },
            )
        elif option == "6":
            print("\n[+] Arping")
            os.system("clear")
            github = "arping is a tool for probing hosts in a network. Unlike the ping command, which operates at the network layer, arping operates at the data link layer and uses the Address Resolution Protocol (ARP). Using it involves sending ARP requests to a destination host and waiting for ARP replies."
            template.template(
                "Arping",
                "arping --help",
                github.strip(),
                {
                    "First resource": "https://www.networkworld.com/article/3601693/using-the-linux-arping-command-to-ping-local-systems.html",
                    "How to use this command": "https://linuxhint.com/use-arping-command-linux/",
                    "Other resources": "https://www.baeldung.com/linux/arping-command",
                },
            )
        elif option == "7":
            print("\n[+] Netdiscover")
            os.system("clear")
            github = "Netdiscover is a command-line oriented TCP/IP packet assembler/analyzer. It supports TCP, UDP, ICMP and RAW-IP protocols, has a traceroute mode, the ability to send files between a covered channel, and many other features."
            template.template(
                "Netdiscover",
                "netdiscover -help",
                github.strip(),
                {
                    "Usage in details": "https://linuxcommandlibrary.com/man/netdiscover",
                    "Second resource": "https://www.cyberpratibha.com/blog/netdiscover/",
                    "Video resources": "https://www.youtube.com/results?search_query=netdiscover+usage",
                },
            )
        elif option == "8":
            print("\n[+] Wafw00f")
            os.system("clear")
            github = ""
            template.template(
                "Wafw00f",
                "wafw00f --help",
                github.strip(),
                {
                    "First resource": "https://www.briskinfosec.com/tooloftheday/toolofthedaydetail/wafw00f-tool-to-fingerprint-and-identify-web-application-firewall",
                    "Second resource": "https://null-byte.wonderhowto.com/how-to/identify-web-application-firewalls-with-wafw00f-nmap-0198145/",
                    "Third resource": "https://www.geeksforgeeks.org/identification-of-web-application-firewall-using-wafw00f-in-kali-linux/",
                    "Github resource": "https://github.com/EnableSecurity/wafw00f",
                    "Video resource": "https://www.youtube.com/results?search_query=wafw00f+command+usage",
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
