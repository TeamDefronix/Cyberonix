from main.tools import banner, colors, template, banner,Recommended_Tool
import os
import requests
from bs4 import BeautifulSoup
import subprocess


def main():
    
    while True:
        
        os.system("clear")
        banner.main()
        banner.attack("Anonymity")
        list_attacks = ["Tor", "Anonsurf", "Proxychain", "Nipe ", "go back"]
        for i in range(len(list_attacks)):
            print(colors.options, f"{i+1}) {list_attacks[i]}".title(), colors.reset)
        try:
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            return
        if option == "1":
            os.system("clear")
            banner.main()
            banner.attack("Tor")
            Recommended_Tool.recommended("tor")

        elif option == "2":
            print("\n[+] Anonsurf")
            anonsurf()
        elif option == "3":
            print("\n[+] ProxyChains ")
            proxychains()        
        elif option == "4":
            print("\n[+] nipe")
            nipe()        
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

def anonsurf():
    github = "This repo contains the sources of both the anonsurf and pandora packages from ParrotSec combined into one.Modifications have been made to use the DNS servers of Private Internet Access (instead of FrozenDNS), and fixes for users who don't use the resolvconf application. I have removed some functionality such as the gui and iceweasel in ram.This repo can be compiled into a deb package to correctly install it on a Kali system."
    template.template(
                "kali-anonsurf",
                "anonsurf -h ",
                github.strip(),
                {"How To Setup And Use Anonsurf On kali Linux": "https://www.geeksforgeeks.org/how-to-setup-and-use-anonsurf-on-kali-linux/", "Anonsurf Detail": "https://linuxhint.com/anonsurf/", "How to install and use anonsurf on Kali Linux": "https://www.linuxfordevices.com/tutorials/kali-linux/install-anonsurf",
                 }, method="github", github_install="git clone https://github.com/Und3rf10w/kali-anonsurf.git && cd kali-anonsurf && bash installer.sh", github_check="kali-anonsurf")
        


def proxychains():
    os.system("clear")
    github = github_getting_text(
                "https://github.com/haad/proxychains", 'p[dir=auto]', 1)
    template.template(
                "proxychains",
                "proxychains ",
                github.strip(),
                {
                    "Proxychain github": "https://github.com/haad/proxychains/tree/master",
                    "Proxychain How to use": "https://proxychains.sourceforge.net/howto.html",
                },
            )
def nipe():
    os.system("clear")
    github = github_getting_text(
                "https://github.com/htrgouvea/nipe", 'p[dir=auto]', 4)
    template.template(
                "nipe",
                "nipe",
                github.strip(),
                {
                    "nipe github": "https://github.com/htrgouvea/nipe/blob/main/README.md",
                    "How to Install Nipe tool in Kali Linux?": "https://www.geeksforgeeks.org/how-to-install-nipe-tool-in-kali-linux/",
                }, method="github", github_install="git clone https://github.com/htrgouvea/nipe.git && cd nipe &&  sudo cpan install Try::Tiny Config::Simple JSON && sudo perl nipe.pl install", github_check="nipe")

if __name__ == "__main__":
    main()
