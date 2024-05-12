from bs4 import BeautifulSoup
from main.tools import banner, colors, template
import os
import requests
from bs4 import BeautifulSoup


def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Wireless Hacking")
        list_attacks = ["Kismet\t\t(Recommended)", "Wifite", "Fern Wifi Cracker",
                        "Aircrack-ng\t\t(Recommended)", "Fluxion", "Wifiphisher\t\t(Recommended)", "go back"]
        for i in range(len(list_attacks)):
            print(colors.options, f"{i+1}) {list_attacks[i]}".title(), colors.reset)
        try:
            option = input(
                f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            return
        if option == "1":
            print("\n[+] Kismet")
            kismet()        
        elif option == "2":
            print("\n[+] Wifite")
            wifite()        
        elif option == "3":
            print("\n[+] Fern Wifi Cracker")
            fernwificracker()        
        elif option == "4":
            print("\n[+] Aircrack-ng")
            aircrack_ng()    
        elif option == "5":
            print("\n[+] Fluxion")
            fluxion()    
        elif option == "6":
            print("\n[+] Wifiphisher")
            wifiphisher()        
        else:
            return


def github_getting_text(link, selector, indexvalue):
    print("Please Wait....\r", end="")
    URL = link
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')
        paras = soup.select(selector)
        # check index value from test file
        return paras[indexvalue].text
    except:
        return f"{colors.red}Not Loaded Because No Internet Connection{colors.reset}"

def kismet():
    github = github_getting_text(
                "https://www.kismetwireless.net/docs/readme/intro/kismet/", 'p', 1)
    template.template("kismet", "kismet", github.strip(), {"Kismet -- WiFi Sniffer": "https://www.kalilinux.in/2019/02/kismet-wifi-sniffer.html", "Use Kismet to Watch Wi-Fi User Activity": "https://null-byte.wonderhowto.com/how-to/use-kismet-watch-wi-fi-user-activity-through-walls-0182214/",
                                                                   "HACKING WIFI USING KISMET": "https://www.bookofnetwork.com/hacking-tutorials/Kismet-Wireless", "How To Use Kismet Kali Linux?": "https://www.systranbox.com/how-to-use-kismet-kali-linux/"})
        
def wifite():
    github = github_getting_text(
                "https://www.kali.org/tools/wifite/", 'p', 1)
    template.template("wifite", "wifite -h", github.strip(), {"Wifite walkthrough Part-1": "https://resources.infosecinstitute.com/topic/wifite-walkthrough-part-1/", "Wifite walkthrough Part-2": "https://resources.infosecinstitute.com/topic/wifite-walkthrough-part-2/",
                                                                      "Wireless pentesting with Wifite": "https://www.hackingarticles.in/wireless-penetration-testing-wifite/", "Wifite - Automated Wifi hacking tool": "https://kalitut.com/wifite-automated-wi-fi-hacking-tool/"})
        
def fernwificracker():
    github = "Fern Wifi Cracker is a Wireless security auditing and attack software program written using the Python Programming Language and the Python Qt GUI library. The program is able to crack and recover WEP/WPA/WPS keys and also run other network based attacks on wireless or ethernet based networks."
    template.template("fern-wifi-cracker", "fern-wifi-cracker", github.strip(), {"What is Fern Wifi Cracker": "https://www.kalilinux.in/2020/09/fern-wifi-cracker.html", "Hacking Wifi networks using Fern Wifi Cracker": "https://www.studocu.com/en-au/document/western-sydney-university/it-product-support-and-services/fern-wifi-cracker-hacking-wifi-networks-using-fern-wifi-cracker-easily/10772514",
                                                                                         "Wireless penetration testing - Fern ": "https://www.hackingarticles.in/wireless-penetration-testing-fern/", "Cracking wifi passwords using Fern": "https://hacking84.rssing.com/chan-13108703/article238.html"})
        
def aircrack_ng():
    github = github_getting_text(
                "https://www.kali.org/tools/aircrack-ng/", 'p', 32)
    template.template("aircrack-ng", "aircrack-ng", github.strip(), {"How to use Aircrack-ng": "https://linuxhint.com/how_to_aircrack_ng/", "Aircrack-ng Practical Demonstration Tutorial": "https://techofide.com/blogs/how-to-use-aircrack-ng-aircrack-ng-tutorial-practical-demonstration/",
                                                                                    "Hacking the wireless network in 5 simple steps": "https://www.hackingloops.com/how-to-use-aircrack-kali/", "Crack WPA/WPA2 WiFi Passwords using Aircrack-ng & Kali Linux": "https://nooblinux.com/crack-wpa-wpa2-wifi-passwords-using-aircrack-ng-kali-linux/"})
        
def fluxion():
    github = github_getting_text(
                "https://fluxionnetwork.github.io/fluxion/", 'p', 1)
    template.template("fluxion", "./fluxion.sh", github.strip(), {"Fluxion kali linux tutorial": "https://linuxhint.com/fluxion-kali-linux-tutorial/", "Fluxion - Wifi security auditing tool": "https://www.hackingloops.com/fluxion/", "Fluxion -- Crack WiFi Passwords in Minutes": "https://www.kalilinux.in/2020/07/fluxion-kali-linux-crack-wifi.html",
                                                                             "Cracking WPA/WPA2 Passwords in Minutes with Fluxion": "https://gbhackers.com/cracking-wpawpa2-passwords-fluxion/amp/", "Wireless Penetration Testing: Fluxion": "https://www.hackingarticles.in/wireless-penetration-testing-fluxion/", "Fluxion in Kali Linux usage": "https://www.cyberpratibha.com/blog/fluxion-wpa-wpa2-hacking/"},method="github", github_install="git clone https://github.com/FluxionNetwork/fluxion.git && cd fluxion", github_check="fluxion")
        
def wifiphisher():
    github = github_getting_text("https://wifiphisher.org/", 'p', 0)
    template.template("wifiphisher", "wifiphisher -h", github.strip(), {"WiFi Exploitation with WifiPhisher": "https://www.hackingarticles.in/wifi-exploitation-wifiphisher/", "wifiphisher Description": "https://en.kali.tools/?p=90", "Read Team engagement on Wifi with Wifiphisher": "https://whitehatinstitute.com/conduct-red-team-engagements-on-wifi-with-wifiphisher/",
                              "Wireless Hacking with WifiPhisher": "https://cntemngwa.medium.com/wireless-hacking-with-wifiphisher-d4b857414146", "WifiPhisher – WiFi Crack and Phishing Framework": "https://latesthackingnews.com/2018/10/02/wifiphisher-wifi-crack-and-phishing-framework/", "Wifiphisher Evil Twin Attack": "https://kalitut.com/wifiphisher-evil-twin-attack/"})


if __name__ == '__main__':
    main()
