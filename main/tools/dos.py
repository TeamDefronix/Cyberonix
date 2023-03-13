from bs4 import BeautifulSoup
from main.tools import banner, colors, template
import os
import requests


def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Deniel of Service Attack")
        list_attacks = [
            "GoldenEye",
            "SlowHTTPTest",
            "THC-SSL-DOS",
            "Slowloris",
            "go back",
        ]
        for i in range(len(list_attacks)):
            print(colors.options, f"{i}) {list_attacks[i]}".title(), colors.reset)
        try:
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            template.exit_program()
        if option == "0":
            print("\n[+] GoldenEye")
            github = github_getting_text(
                "https://www.kali.org/tools/goldeneye/", "p", 0
            )
            template.template(
                "goldeneye",
                "goldeneye -h",
                github.strip(),
                {
                    "Goldeneye DDos Tool in Kali Linux": "https://www.geeksforgeeks.org/goldeneye-ddos-tool-in-kali-linux/",
                    "Golden Eye DDoS Tool: Installation and Tool usage with examples": "https://allabouttesting.org/golden-eye-ddos-tool-installation-and-tool-usage-with-examples/",
                    "DoS website in Kali Linux using GoldenEye": "https://www.blackmoreops.com/2015/05/18/dos-website-in-kali-linux-using-goldeneye/",
                    "DoS website with GoldenEye - Layer 7 DoS tool": "https://www.darkmoreops.com/2014/11/22/dos-website-with-goldeneye/",
                },
            )  # method=kali
        elif option == "1":
            print("\n[+] Slowhttptest")
            github = github_getting_text(
                "https://www.kali.org/tools/slowhttptest/", "p", 1
            )
            template.template(
                "slowhttptest",
                "slowhttptest -h",
                github.strip(),
                {
                    'How to perform a DoS attack "Slow HTTP" with SlowHTTPTest': "https://ourcodeworld.com/articles/read/949/how-to-perform-a-dos-attack-slow-http-with-slowhttptest-test-your-server-slowloris-protection-in-kali-linux",
                    "slowhttptest Usage Example": "https://www.kali.org/tools/slowhttptest/",
                    "DoS website using slowhttptest in Kali Linux ": "https://www.blackmoreops.com/2015/06/07/attack-website-using-slowhttptest-in-kali-linux/",
                    "Kali Linux - Stressing Tools": "https://www.tutorialspoint.com/kali_linux/kali_linux_stressing_tools.htm",
                    "How to perform SlowHTTPtest DOS attack ": "https://support.tetcos.com/support/solutions/articles/14000130254-how-to-perform-slowhttptest-dos-attack-through-netsim-emulator-",
                },
            )  # method is kali
        elif option == "2":
            print("\n[+] THC-SSL-DOS")
            github = github_getting_text(
                "https://www.kali.org/tools/thc-ssl-dos/", "p", 1
            )
            github += github_getting_text(
                "https://www.kali.org/tools/thc-ssl-dos/", "p", 2
            )
            github += github_getting_text(
                "https://www.kali.org/tools/thc-ssl-dos/", "p", 3
            )
            template.template(
                "thc-ssl-dos",
                "thc-ssl-dos -h",
                github.strip(),
                {
                    "THC-SSL DoS": "https://www.radware.com/security/ddos-knowledge-center/ddospedia/thc-ssl-dos/",
                    "thc-ssl-dos Usage Example": "https://www.kali.org/tools/thc-ssl-dos/",
                    "THC-SSL-DOS – DoS Tool Against Secure Web-Servers and for Testing SSL-Renegotiation": "https://kalilinuxtutorials.com/thc-ssl-dos/",
                    "The THC SSL DoS Threat": "https://resources.infosecinstitute.com/topic/thc-ssl-dos-threat/",
                },
            )  # method is kali
        elif option == "3":
            print("\n[+] SlowLoris")
            github = "Slowloris is a Low bandwidth  HTTP Denial of Service attack that affects threaded servers"
            template.template(
                "Slowloris",
                "python slowloris.py -h",
                github.strip(),
                {
                    "Slowloris DDOS Attack Tool in Kali Linux": "https://www.geeksforgeeks.org/slowloris-ddos-attack-tool-in-kali-linux/",
                    "What is Slowloris?": "https://www.imperva.com/learn/ddos/slowloris/",
                    "Performing a genuine slowloris attack": "https://ourcodeworld.com/articles/read/962/performing-a-genuine-slowloris-attack-slowhttp-of-indefinite-length-in-kali-linux",
                },
                link="https://github.com/gkbrk/slowloris.git",
                method="github",
                github_install="git clone https://github.com/gkbrk/slowloris.git",
                github_check="slowloris",
            )

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


if __name__ == "__main__":
    main()
