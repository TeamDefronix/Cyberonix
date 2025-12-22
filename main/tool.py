#!/usr/bin/env python3
import os
import sys
import subprocess

# --- Ensure project root is in sys.path ---
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# --- Import internal modules ---
from main.tools import *
try:
    from JS_Voyager import main as JS_Voyager
except ImportError:
    JS_Voyager = None


# --- Helper Functions ---
def exit_program():
    os.system("clear")
    banner.main()
    print("\033[38;5;105m", "[+] Thanks for visiting again!".title())


# --- Function to run JS-Voyager ---
def run_js_voyager():
    # clear then show the Cyberonix banner (same behavior as other tools)
    os.system("clear")
    try:
        banner.main()
        banner.attack("JS-Voyager")
    except Exception:
        # if banner for some reason isn't available, keep going quietly
        pass

    print(f"{colors.green}[+] Launching JS-Voyager...{colors.reset}")

    # Path to your run_js_voyager_with_input.py script
    voyager_script = os.path.join(PROJECT_ROOT, "JS_Voyager", "run_js_voyager_with_input.py")

    if not os.path.exists(voyager_script):
        print(f"{colors.red}[-] Error: Script not found at {voyager_script}{colors.reset}")
    else:
        try:
            subprocess.run([sys.executable, voyager_script])
        except Exception as e:
            print(f"{colors.red}[-] Failed to run JS_Voyager: {e}{colors.reset}")

    input(f"\n{colors.options}[!] Press Enter to return to the menu...{colors.reset}")


# --- Main Menu Loop ---
def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("TOOLS")

        list_attacks = [
            "Information Gathering", "Vulnerability Analysis", "Web Application Analysis",
            "Password Attacks", "Wireless Attacks", "Exploitation Tools",
            "Sniffing and Spoofing", "Post Exploitation", "Anonymity",
            "Framework", "Pentesting In Bug-Bounty", "Digital Forensics Tools",
            "JS-Voyager", "Go Back"
        ]

        for i, attack in enumerate(list_attacks, start=1):
            print(colors.options, f"{i}) {attack}", colors.reset)

        try:
            option = input(f"\n{colors.select}Select An Option -> {colors.reset}")
        except KeyboardInterrupt:
            return

        # --- Section Handlers ---
        handlers = {
            "1": information_gathering,
            "2": Vulnerability_Analysis,
            "3": WEB_Application_Analysis,
            "4": Password_Hacking,
            "5": Wireless_Hacking,
            "6": Exploitation_Tools,
            "7": Sniffing_and_Spoofing,
            "8": PostExploitationAttacks,
            "9": Anonymity,
            "10": Framework,
            "11": Pentesting_Bug_Bounty,
            "12": forensic,
            "13": run_js_voyager,   # ✅ now runs your custom script
        }

        if option in handlers:
            os.system("clear")
            # If it’s a module with a .main() method, call it; if it’s a function, just call it directly.
            if hasattr(handlers[option], "main"):
                handlers[option].main()
            else:
                handlers[option]()
        else:
            exit_program()
            return


# --- Entry Point ---
if __name__ == "__main__":
    main()
