from main.tools import banner,run_on_browser,colors
import os
import threading

def main():  
    os.system("clear")
    banner.main()
    banner.attack("Cheat Sheet")
    cheat({"Nmap cheatsheet" : "https://www.tutorialspoint.com/nmap-cheat-sheet","Maltego cheatsheet" : "https://static.maltego.com/cdn/Case%20studies/Building-Integrations-for-Maltego-Cheat-Sheet.pdf","Hping3 cheatsheet" : "https://cyberwar.nl/d/cheatsheets/hping3_cheatsheet_v1.0-ENG.pdf","Netdiscover cheatsheet" : "https://linuxcommandlibrary.com/man/netdiscover","Wafw00f cheatsheet" : "https://cheatsheet.haax.fr/web-pentest/applicative-scans/web_application_firewall/", "Metasploit-Framework cheatsheet" : "https://cdn.comparitech.com/wp-content/uploads/2019/06/Metasploit-Cheat-Sheet-1.webp", "Wireshark cheatsheet" : "https://www.stationx.net/wireshark-cheat-sheet/", "Bettercap cheatsheet" : "https://www.bettercap.org/usage/interactive/", "Tcpdump cheatsheet" : "https://cdn.comparitech.com/wp-content/uploads/2019/06/tcpdump-cheat-sheet-1.pdf", "Scapy cheatsheet" : "https://wiki.sans.blue/Tools/pdfs/ScapyCheatSheet_v0.2.pdf", "Responder cheatsheet" : "https://www.ivoidwarranties.tech/posts/pentesting-tuts/responder/cheatsheet/", "Airgeddon cheatsheet" : "https://liodeus.github.io/2020/10/29/OSWP-personal-cheatsheet.html#airgeddon", "Wpscan cheatsheet" : "https://linuxcommandlibrary.com/man/wpscan","Wapiti cheatsheet" : "https://wapiti.limsi.fr/manual.html","Legion cheatsheet" : "https://theory.stanford.edu/~aiken/LegionRetreat21/slides/Tools.pdf","Nikto cheatsheet" : "https://cdn.comparitech.com/wp-content/uploads/2019/07/NIkto-Cheat-Sheet.pdf", "Burp Suite cheatsheet" : "https://portswigger.net/burp/documentation/desktop","Owasp ZAP cheatsheet" : "https://www.zaproxy.org/docs/desktop/cmdline/","Nessus cheatsheet" : "https://limberduck.github.io/nessus-cheat-sheet/nessus-cheat-sheet.pdf","dirb cheatsheet" : "https://man7.org/linux/man-pages/man1/dir.1.html","skipfish cheatsheet" : "https://linux.die.net/man/1/skipfish","Nuclei cheatsheet" : "https://cheatsheet.haax.fr/web-pentest/tools/nuclei/", "Wifite cheatsheet" : "https://cheatography.com/socket23/cheat-sheets/wifite/", "Aircrack-ng cheatsheet" : "https://www.cyberfella.co.uk/rhel/aircrack-ng-suite.pdf"}, "cheatSheet")



def cheat(cheatSheet,name):
    while True:
        os.system("clear")
        banner.main()   
        banner.attack(name.title())

        key=list(cheatSheet.keys())
        key.append("go back".title())
        for i in range(len(key)):
            print(colors.options,f"{i}) {key[i]}".title(),colors.reset)
        option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        try:
            threading.Thread(target=run_on_browser.main, args=(cheatSheet[key[int(option)]],)).start()
                
        except:
            return

if __name__ == "__main__": 
    main()

