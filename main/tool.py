from main.tools import *
import os

def exit_program():
        os.system("clear")
        banner.main()
        print("\033[38;5;105m","[+] Thanks visit again".title())

def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("TOOLS")
        # import information_gathering

        list_attacks=["Information Gathering","Vulnerability Analysis","Web Application Analysis","Password Attacks","Wireless Attacks","Exploitation Tools","Sniffing and Spoofing","Post Exploitation","Pentesting and Bug-Bounty","go back"]
        #for output with index
        for i in range(len(list_attacks)):
                print(colors.options,f"{i}) {list_attacks[i]}".title(),colors.reset)
        try:
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            template.exit_program()
        if option == "0":
            print("\n[+] Information Gathering Section")
            os.system("clear")
            information_gathering.main()
        elif option == "1":
            print("\n[+] Vulnerability Analysis")
            os.system("clear")
            Vulnerability_Analysis.main()
        elif option == "2":
            print("\n[+] Web Application Analysis")
            os.system("clear")
            WEB_Application_Analysis.main()
        elif option == "3":
            print("\n[+] Password Attacks")
            os.system("clear")
            Password_Hacking.main()
        elif option == "4":
            print("\n[+] Wireless Attacks")
            os.system("clear")
            Wireless_Hacking.main()
        elif option == "5":
            print("\n[+] Exploitation Tools")
            os.system("clear")
            Exploitation_Tools.main()
        elif option == "6":
            print("\n[+] Sniffing and Spoofing")
            os.system("clear")
            Sniffing_and_Spoofing.main()
        elif option == "7":
            print("\n[+] Post Exploitation")
            os.system("clear")
            PostExploitationAttacks.main()
        elif option == "8":
            print("\n[+] Pentesting and Bug-Bounty")
            os.system("clear")
            Pentesting_Bug_Bounty.main()
        else:
            print("[-] going back")
            return

if __name__ == "__main__": 
    main()
