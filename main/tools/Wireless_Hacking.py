import threading
from bs4 import BeautifulSoup
from main.tools import banner,colors,template
import os
import requests
from bs4 import BeautifulSoup

def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Wireless Hacking")
        list_attacks = ["Kismet", "Wifite", "Fern Wifi Cracker",
                        "Aircrack-ng", "Fluxion", "Wifiphisher", "go back"]
        for i in range(len(list_attacks)):
            print(colors.options,f"{i}) {list_attacks[i]}".title(),colors.reset)
        option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        if option == "0":
            print("\n[+] Kismet")
            github = github_getting_text("https://github.com/kismetwireless/kismet-docs/blob/master/readme/000-intro.md", 'p[dir="auto"]', 0)
            template.template("Kismet","kismet",github.strip(),{"Kismet -- WiFi Sniffer": "https://www.kalilinux.in/2019/02/kismet-wifi-sniffer.html", "Use Kismet to Watch Wi-Fi User Activity": "https://null-byte.wonderhowto.com/how-to/use-kismet-watch-wi-fi-user-activity-through-walls-0182214/",
                    "HACKING WIFI USING KISMET": "https://www.bookofnetwork.com/hacking-tutorials/Kismet-Wireless", "How To Use Kismet Kali Linux?": "https://www.systranbox.com/how-to-use-kismet-kali-linux/"})
        elif option == "1":
            print("\n[+] Wifite")
            github = github_getting_text("https://www.kali.org/tools/wifite/", 'p', 1)
            template.template("Wifite","wifite -h",github.strip(),{"Wifite walkthrough Part-1": "https://resources.infosecinstitute.com/topic/wifite-walkthrough-part-1/", "Wifite walkthrough Part-2": "https://resources.infosecinstitute.com/topic/wifite-walkthrough-part-2/",
                    "Wireless pentesting with Wifite": "https://www.hackingarticles.in/wireless-penetration-testing-wifite/", "Wifite - Automated Wifi hacking tool": "https://kalitut.com/wifite-automated-wi-fi-hacking-tool/"})
        elif option == "2":
            print("\n[+] Fern Wifi Cracker")
            github = github_getting_text("https://github.com/savio-code/fern-wifi-cracker", 'p[dir="auto"]', 0)
            template.template("Fern-Wifi-Cracker","fern-wifi-cracker",github.strip(),{"What is Fern Wifi Cracker": "https://www.kalilinux.in/2020/09/fern-wifi-cracker.html", "Hacking Wifi networks using Fern Wifi Cracker": "https://www.studocu.com/en-au/document/western-sydney-university/it-product-support-and-services/fern-wifi-cracker-hacking-wifi-networks-using-fern-wifi-cracker-easily/10772514",
                    "Wireless penetration testing - Fern ": "https://www.hackingarticles.in/wireless-penetration-testing-fern/", "Cracking wifi passwords using Fern": "https://hacking84.rssing.com/chan-13108703/article238.html"})
        elif option == "3":
            print("\n[+] Aircrack-ng")
            github = github_getting_text("https://www.kali.org/tools/aircrack-ng/", 'p', 32)
            template.template("Aircrack-ng","aircrack-ng --help",github.strip(),{"How to use Aircrack-ng": "https://linuxhint.com/how_to_aircrack_ng/", "Aircrack-ng Practical Demonstration Tutorial": "https://techofide.com/blogs/how-to-use-aircrack-ng-aircrack-ng-tutorial-practical-demonstration/",
                    "Hacking the wireless network in 5 simple steps": "https://www.hackingloops.com/how-to-use-aircrack-kali/", "Crack WPA/WPA2 WiFi Passwords using Aircrack-ng & Kali Linux": "https://nooblinux.com/crack-wpa-wpa2-wifi-passwords-using-aircrack-ng-kali-linux/"})
        elif option == "4":
            print("\n[+] Fluxion")
            github = github_getting_text("https://github.com/FluxionNetwork/fluxion", 'p[dir="auto"]', 1)
            template.template("flucion","kismet -h",github.strip(),{"Fluxion kali linux tutorial": "https://linuxhint.com/fluxion-kali-linux-tutorial/", "Fluxion - Wifi security auditing tool": "https://www.hackingloops.com/fluxion/", "Fluxion -- Crack WiFi Passwords in Minutes": "https://www.kalilinux.in/2020/07/fluxion-kali-linux-crack-wifi.html",
                    "Cracking WPA/WPA2 Passwords in Minutes with Fluxion": "https://gbhackers.com/cracking-wpawpa2-passwords-fluxion/amp/", "Wireless Penetration Testing: Fluxion": "https://www.hackingarticles.in/wireless-penetration-testing-fluxion/", "Fluxion in Kali Linux usage": "https://www.cyberpratibha.com/blog/fluxion-wpa-wpa2-hacking/"},method="github")
        elif option == "5":
            print("\n[+] Wifiphisher")
            github = github_getting_text("https://github.com/wifiphisher/wifiphisher", 'p[dir="auto"]', 2)
            template.template("Wifiphisher","wifiphisher -h",github.strip(),{"WiFi Exploitation with WifiPhisher": "https://www.hackingarticles.in/wifi-exploitation-wifiphisher/", "wifiphisher Description": "https://en.kali.tools/?p=90", "Read Team engagement on Wifi with Wifiphisher": "https://whitehatinstitute.com/conduct-red-team-engagements-on-wifi-with-wifiphisher/", "Wireless Hacking with WifiPhisher": "https://cntemngwa.medium.com/wireless-hacking-with-wifiphisher-d4b857414146", "WifiPhisher – WiFi Crack and Phishing Framework": "https://latesthackingnews.com/2018/10/02/wifiphisher-wifi-crack-and-phishing-framework/", "Wifiphisher Evil Twin Attack": "https://kalitut.com/wifiphisher-evil-twin-attack/"})
                    
        else:
            return


def github_getting_text(link,selector,indexvalue):
    print("Please Wait....\r",end="")
    URL = link
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        paras = soup.select(selector)
        #check index value from test file
        return paras[indexvalue].text
    except:
        return f"{colors.red}Not Loaded Because No Internet Connection{colors.reset}"

if __name__=='__main__':
    main()