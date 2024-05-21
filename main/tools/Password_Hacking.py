import os
from main.tools import template, banner, colors, WEB_Application_Analysis,Configuration_Management


def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Password Hacking")
        list_root_attacks = ["Useful Sites","Brute Force Attacks", "Dictionary Attacks", "Rainbow Table Attack",
                             "Wordlist Generator", "Phishing Attacks", "Keylogger Attacks", "go back"]
        for i in range(len(list_root_attacks)):
            print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
        try:
            option = input(
                f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            return
        if option == "1":
            print("\n[+] Useful Websites")
            os.system("clear")
            template.template("Useful Websites", "no-tools", 'This is website for information gathering', {
                "Salted Password Hashing - Doing it Right": "https://crackstation.net/hashing-security.htm", 
                "CrackStation's Password Cracking Dictionary":"https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm", 
                "Wordlist Download": "https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm",
                "CyberChef - A must have security tool": "https://www.youtube.com/watch?v=rT_CjwKN380",
                "CyberChef – Data decoding made easy": "https://www.csnp.org/post/cyberchef-data-decoding-made-easy",


            })
        elif option == "2":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Brute Force")
                banner.description("A brute force attack is a method of attempting to gain unauthorized access to a computer or network by systematically trying every possible combination of charactersor words in order to discover a valid password or key. In a 'pure' brute force attack, all possible combinations are tried one after another until the correct one is found. This can be a time-consuming process, but it is often effective because many people use easily-guessed passwords.")
                list_root_attacks = ["Hashcat\t\t(Recommended)", "John The Ripper\t(Recommended)", "Hydra\t\t(Recommended)", "Dirsearch",
                                     "Johnny (GUI John)","Dirbuster", "Reaver", "go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(
                        f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    hashcat()
                elif ask == "2":
                    john_the_ripper()
                elif ask == "3":
                    hydra()
                elif ask == "4":
                    WEB_Application_Analysis.dirsearch()
                elif ask == "5":
                    johnny()
                elif ask == "6":
                    Configuration_Management.dirbuster()
                elif ask == "7":
                    reaver()
                else:
                    break

        elif option == "3":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Dictionary Attacks")
                banner.description("A dictionary attack is a type of brute force attack that involves trying every word in a predefined list (a dictionary) as a password. This method is more efficient than a traditional brute force attack, where every possible combination of characters is tried, because most people use common words or phrases as passwords. The attacker can also use a list of commonly used passwords or publicly available information about the target (such as their name, birthdate, etc.) to create a custom dictionary.")
                list_root_attacks = ["Hashcat\t\t(Recommended)", "John The Ripper\t(Recommended)", "Hydra\t\t(Recommended)",
                                     "Medusa", "Ncrack", "Johnny (GUI John)", "go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    hashcat()
                elif ask == "2":
                    john_the_ripper()    
                elif ask == "3":
                    hydra()    
                elif ask == "4":
                    medusa()
                elif ask == "5":
                    ncrack()
                elif ask == "6":
                    johnny()
                else:
                    break
        elif option == "4":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Rainbow Table Attack")
                banner.description("A rainbow table attack is a method of cracking password hashes by using precomputed tables of hash values, which can be faster than traditional brute force attack. It is particularly effective against hash functions that are fast to compute and vulnerable to collisions, but less effective against stronger hash functions.")
                list_root_attacks = ["RainbowCrack", "ophCrack", "go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(
                        f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    rainbowcrack()   
                elif ask == "2":
                    ophcrack()
                else:
                    break

        elif option == "5":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Wordlist Generator")
                banner.description("A wordlist generator is a tool that generates a list of words or phrases that can be used in a dictionary attack. The list can be generated from a predefined dictionary, real-world data such as web pages, or by using a combination of commonly used words or patterns. This list of words is then used to try as potential passwords in a dictionary attack, which can be more efficient than a traditional brute force attack as it tries only words that are likely to be used as passwords.")
                list_root_attacks = ["Crunch", "Cupp", "bopscrk", "go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(
                        f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    crunch()
                elif ask == "2":
                    cupp()
                elif ask == "3":
                    bopscrk()
                else:
                    break

        elif option == "6":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Phishing Attacks")
                banner.description("A phishing attack is a type of cyber attack in which an attacker uses fraudulent emails, websites, or other means of communication to trick a victim into providing sensitive information such as login credentials, personal information, or financial details. The attacker often poses as a trustworthy entity and attempts to convince the victim to click on a link, download an attachment, or enter information into a fake website. The goal of a phishing attack is to steal sensitive information or install malware on the victim's device.")
                list_root_attacks = ["Social-Engineer Toolkit (SET)", "HiddenEye", "r3bu5", "zphisher\t\t(Recommended)",
                                     "Shellphish", "Gophish (GUI)\t(Recommended)", "Camphish\t\t(Recommended)", "go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(
                        f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    setoolkit()
                elif ask == "2":
                    hiddeneye()
                elif ask == "3":
                    r3bu5()
                elif ask == "4":
                    zphisher()
                elif ask == "5":
                    shellphish()
                elif ask == "6":
                    gophish()
                elif ask == "7":
                    camphish()
                else:
                    break

        elif option == "7":
            while True:
                os.system("clear")
                banner.main()
                banner.attack("Keylogger Attacks")
                banner.description("A keylogger attack is a type of cyber attack in which an attacker uses malicious software, called a keylogger, to record every keystroke made by a victim on their computer or mobile device. This includes passwords, credit card numbers, personal information, and other sensitive data. The keylogger can also take screenshots of the victim's screen, record their internet browsing history, and even capture audio and video. The attacker can use this information to steal personal identities, login credentials, and financial information, or to gain access to sensitive systems. Keyloggers can be installed through malware, email attachments,or social engineering tactics like phishing.")
                list_root_attacks = ["Keylogger", "go back"]
                for i in range(len(list_root_attacks)):
                    print(colors.options, f"{i+1}) {list_root_attacks[i]}".title(), colors.reset)
                try:
                    ask = input(
                        f"\n {colors.select}Select An Option ->{colors.reset}  ")
                except KeyboardInterrupt:
                    return
                if ask == "1":
                    keylogger()    
                else:
                    break
        else:
            return
        


def medusa():
    github = "Medusa is a password cracking tool that is used to perform brute-force attacks on login credentials. It is a command-line tool that can be used to test the security of login systems by trying a large number of possible username and password combinations. Medusa is capable of testing various protocols such as HTTP, HTTPS, FTP, SSH, and more. It is mainly used by penetration testers and security professionals to identify weak passwords in a network and help improve the overall security of an organization. However, like other password cracking tools, it can also be used by malicious actors for illegal activities."
    template.template("medusa", "medusa", github.strip(), {"A Detailed Guide on Medusa": "https://www.hackingarticles.in/a-detailed-guide-on-medusa/",
                                      "Bruteforce Password Cracking with Medusa": "https://www.yeahhub.com/bruteforce-password-cracking-medusa-kali-linux/"})
                
def ncrack():
    github = "Ncrack is a network authentication cracking tool. It is designed to perform efficient brute-force and dictionary attacks against a variety of different network protocols, including Telnet, FTP, HTTP, HTTPS, SMB, and RDP. It can be used to test the security of networks and remote systems by attempting to log in with a large number of different username and password combinations.Ncrack is similar to other password cracking tools such as John the Ripper and Hydra, but it is specifically designed to work with network protocols. It can run on Windows, Linux, and macOS and is often used by security professionals and penetration testers to test the security of networks and web applications"
    template.template("ncrack", "ncrack", github.strip(), {"Comprehensive Guide on Ncrack – A Brute Forcing Tool": "https://www.hackingarticles.in/comprehensive-guide-on-ncrack-a-brute-forcing-tool/",
                                      "Ncrack – Network Authentication and Password Cracking Tool": "https://secnhack.in/ncrack-network-authentication-and-password-cracking-tool/"})
               
def reaver():
    github = "Reaver implements a brute force attack against Wifi Protected Setup (WPS) registrar PINs in order to recover WPA/WPA2 passphrases, as described in Brute forcing Wi-Fi Protected Setup When poor design meets poor implementation. by Stefan Viehböck. Reaver has been designed to be a robust and practical attack against Wi-Fi Protected Setup (WPS) registrar PINs in order to recover WPA/WPA2 passphrases and has been tested against a wide variety of access points and WPS implementations."
    template.template("reaver", "reaver", github.strip(), {
                                      "Revear cheatsheet": "https://cheatography.com/jlunz/cheat-sheets/reaver-cheat-sheet/", "Revear github": "https://github.com/t6x/reaver-wps-fork-t6x/blob/master/README.md", })
                
def johnny():
    github = "Johnny is a GUI (Graphical User Interface) for the John the Ripper password cracking tool. It provides a user-friendly interface for managing and running John the Ripper's cracking tasks, rather than using command line commands. It is designed to make the process of cracking passwords more efficient and user-friendly. It can run on Windows, Linux and MacOS."
    template.template("johnny", "johnny", github.strip(), {
                                      "How to use the Johnny GUI for password cracking": "https://andregodinho1.medium.com/how-to-use-johnny-an-advanced-password-cracker-recovery-gui-soft-61736c8cb1ca", "Password cracking with Johnny": "https://www.youtube.com/watch?v=Wrg6XZu6Luw"})
                
def hydra():
    github = "Hydra is a password cracking tool that performs brute-force and dictionary attacks on network protocols such as Telnet, FTP, HTTP, and SSH. It is used to test the security of remote systems by attempting to log in with multiple username and password combinations. It can run on multiple operating systems and is commonly used by security professionals and penetration testers."
    template.template("hydra", "hydra", github.strip(), {"How to use the hydra for password cracking": "https://www.techtarget.com/searchsecurity/tutorial/How-to-use-the-Hydra-password-cracking-tool",
                                      "Hydra Tool For Brute- force attack": "https://systemweakness.com/hydra-tool-for-brute-force-attack-72653db7abe9?gi=efe05fea34af"})
                
def john_the_ripper():
    github = "John the Ripper is a free and open-source password cracking software tool. It can be run on a variety of operating systems, including Windows, macOS, and Linux. It uses a combination of wordlists and rules to try and guess the password for a given hash or file, and can support a variety of different hash types, including those used for Unix and Windows passwords. John the Ripper is commonly used by security professionals and system administrators to audit the security of their systems and detect weak or easily guessable passwords."
    template.template("john", "john -h", github.strip(), {"How to Crack Passwords using John The Ripper – Pentesting Tutorial": "https://www.freecodecamp.org/news/crack-passwords-using-john-the-ripper-pentesting-tutorial/", "How to use the John the Ripper password cracker": "https://www.techtarget.com/searchsecurity/tutorial/How-to-use-the-John-the-Ripper-password-cracker", "Unveiling the Power of John the Ripper: A Beginner’s Guide to Password Cracking":
                                      "https://infosecwriteups.com/unveiling-the-power-of-john-the-ripper-a-beginners-guide-to-password-cracking-a9846172b35a", "Open-wall John": "https://www.openwall.com/john/", "Password Cracking With John The Ripper": "https://medium.com/@mohitdeswal_35470/john-the-ripper-a-comprehensive-guide-to-password-cracking-9335f44ed3f5", "Tips and Tutorials of John": "https://www.varonis.com/blog/john-the-ripper"})
                
def hashcat():
    github = "Hashcat is an open-source password cracking tool that can perform dictionary, brute force and combination attacks, it uses the power of GPUs to accelerate the cracking process, supports a wide variety of hashing algorithms and it can run on Windows, Linux and macOS. It's widely used for password recovery, security testing and penetration testing."
    template.template("hashcat", "hashcat -h", github.strip(), {"Hashcat tutorial for beginners": "https://resources.infosecinstitute.com/topic/hashcat-tutorial-beginners/",
                                      "How to Crack Passwords Using Hashcat Tool?": "https://geekflare.com/password-cracking-with-hashcat/"})
                
def rainbowcrack():
    github = "RainbowCrack is a password cracking tool that uses a large precomputed table of hash values to speed up the process of cracking passwords. It is commonly used to crack Windows LM hashes and NTLM hashes, as well as other types of hashes such as those used in Linux and Unix-based systems. The tool is named after the 'rainbow table' data structure it uses to efficiently store the precomputed hash values."
    template.template("rainbowcrack", "rcrack", github.strip(), {"How to use rainbow-crack tool": "https://null-byte.wonderhowto.com/how-to/rainbow-tables-create-use-them-crack-passwords-0131470/",
                                      "Rainbow Tables & Rainbow-crack Cracking Passwords": "https://www.kalilinux.in/2021/03/rainbow-tables-rainbowcrack-kali-linux.html"})

def ophcrack():
    github = "Ophcrack is a free, open-source password cracking tool specifically designed to crack Windows login passwords. It uses rainbow tables, a precomputed table of hash values, to crack passwords quickly. It can also recover LM and NTLM hashes, and it supports a variety of hash algorithms such as LM, NTLM, and MD5. The tool is available as a bootable CD or USB drive and can be used to recover lost or forgotten Windows passwords."
    template.template("ophcrack", "ophcrack", github.strip(), {
                                      "Crack Windows Passwords With Ophcrack and Rainbow Tables": "https://www.wikihow.com/Crack-Windows-Passwords-With-Ophcrack-and-Rainbow-Tables/"})
                
def crunch():
    github = "Crunch is a wordlist generator tool that can be used to generate a list of all possible combinations of characters for a given set of parameters. It can be used to generate a wordlist for password cracking, testing password policies and other security related tasks. It is a simple command line tool that can be used to generate wordlists with different character sets, lengths, patterns and other parameters. It can also use a standard or a custom character set to generate the wordlist and can be used to generate a wordlist of any size."
    template.template("crunch", "crunch", github.strip(), {"Create Wordlist Using Crunch": "https://null-byte.wonderhowto.com/how-to/tutorial-create-wordlists-with-crunch-0165931/",
                                      "Crunch Password List Generation": "https://www.hackingtutorials.org/general-tutorials/crunch-password-list-generation/", "Complete Guide on Crunch Tool": "https://secnhack.in/complete-guide-on-crunch-tool/"})
                
def cupp():
    github = "CUPP (Common User Passwords Profiler) is a tool that generates a custom wordlist based on personal information about a target. It can be used to generate a wordlist based on information such as the target's name, birthdate, address, and other personal details. CUPP can be used to perform a dictionary attack on a password hash, trying all the generated words as passwords, in order to crack the password. CUPP is written in Python and it's open source."
    template.template("cupp", "cupp", github.strip(), {"Cybrary CUPP Tool": "https://www.cybrary.it/blog/0p3n/using-cupp-tool-generate-powerful-password-lists/", "How To Create Password List Using CUPP Tool":
                                      "https://programmercave0.github.io/blog/2019/10/10/How-to-create-Password-list-using-CUPP-tool-on-ubuntu", "CUPP Tool Password Generator)": "https://www.geeksforgeeks.org/cupp-common-user-passwords-profiler/"})
                
def bopscrk():
        github = "Bopscrk (Before Outset Password Cracking) is a tool to generate smart and powerful wordlists for targeted attacks. It is part of Black Arch Linux for as long as we can remember. It introduces personal information related to the target and combines every word and transforms it into possible passwords. It also contains a lyric pass module which allows it to search lyrics related to the favourite artist of the target and then include them into the wordlists."
        template.template("bopscrk", "bopscrk -i", github.strip(), {"Create Wordlist Like Pro by Zsecurity": "https://zsecurity.org/create-password-wordlists-like-a-pro-2/",
                                      "Wordlist For Pentester": "https://www.hackingarticles.in/wordlists-for-pentester/"}, method="pip")
                

def setoolkit():
    github = "The Social Engineering Toolkit (SET) is an open-source penetration testing framework that is used to perform various social engineering attacks. It is designed to be used for the purposes of penetration testing and vulnerability assessments, and it can be used to perform attacks such as phishing, website attacks, and other forms of social engineering. The toolkit is written in Python and is available for Windows, Linux, and Mac OS X. It can be used to test the security of an organization's employees and to evaluate the effectiveness of security awareness training programs."
    template.template("set", "setoolkit", github.strip(), {"Phishing using SET": "https://www.golinuxcloud.com/social-engineering-toolkit-phishing/",
                                      "Phishing using SET by Hengky Sanjaya": "https://medium.com/hengky-sanjaya-blog/social-engineering-toolkit-set-23be8b66aa18"})


def hiddeneye():
    github = "HiddenEye is a modern phishing tool with advanced functionality. It is written in Python and can be run on Windows, Linux, and Mac OS X. It allows you to perform various phishing attacks."
    template.template("HiddenEye", "python HiddenEye.py", github.strip(), {"HiddenEye by GeeksForGeeks": "https://www.geeksforgeeks.org/hiddeneye-modern-phishing-tool-with-advanced-functionality/", "HiddenEye by Zsecurity": "https://zsecurity.org/hiddeneye-with-ngrok-all-in-one-phishing-solution/",
                                      "HiddenEye by Null-Byte": "https://null-byte.wonderhowto.com/forum/phish-with-hiddeneye-tool-with-advanced-feature-0323221/"}, method="github", github_install="git clone https://github.com/Morsmalleo/HiddenEye && cd HiddenEye && pip install -r requirements.txt && pip install pyngrok", github_check="HiddenEye")
def r3bu5():
    github = "It is a Phishing tool that has latest and updated login pages, Mask URL support, Beginners Friendly, Multiple tunneling options"
    template.template("r3bu5", "./r3bu5.sh", github.strip(), {"Github Repo of r3bu5": " https://github.com/k46-db0y/r3bu5"}, method="github",
                                      github_install="git clone https://github.com/k46-db0y/r3bu5.git && cd r3bu5 && chmod +x r3bu5.sh", github_check="r3bu5")
        
def zphisher():
    github = "Zphisher is an open-source phishing tool that automates the process of creating and deploying phishing pages. It allows users to easily create phishing pages for various popular websites, such as Google, Facebook, and LinkedIn, and can be used to perform phishing attacks on targeted individuals or organizations. It can also be used to test the security awareness of an organization's employees. Zphisher is written in Shell Script and it's available for Linux and Termux."
    template.template("zphisher", "bash zphisher.sh", github.strip(), {"Zphisher – Automated Phishing Tool in Kali Linux": "https://www.geeksforgeeks.org/zphisher-automated-phishing-tool-in-kali-linux/",
                                      "Creating Phishing Links with Zphisher": "https://medium.com/@jbtechmaven/creating-phishing-links-with-zphisher-db7cc8a1f013"}, method="github", github_install="git clone git://github.com/htr-tech/zphisher.git && cd zphisher && chmod +x zphisher.sh", github_check="zphisher")        
def gophish():
    github = "Gophish is an open-source tool for conducting phishing campaigns. It allows users to create, send and track phishing campaigns, including the ability to create custom phishing templates and landing pages, as well as track user interactions with the phishing emails. Gophish is often used by penetration testers and security professionals to test the security of an organization's email system and educate employees on how to spot and avoid phishing attempts. However, like other phishing tools, it can also be used by malicious actors for illegal activities."
    template.template("Gophish", "gophish]", github.strip(), {"Create phishing campaign gophish": "https://www.golinuxcloud.com/create-phishing-campaign-gophish/", "Phishing attack using gophish": "https://www.techrepublic.com/article/how-to-run-a-phishing-attack-simulation-with-gophish/"},
                                      method="github", github_install="git clone https://github.com/gophish/gophish.git && cd gophish && chmod +x gophish.go && go run gophish.go", github_check="Gophish")
def shellphish():
    github = "Shellphish is a tool used for phishing attacks, specifically for the purpose of stealing login credentials. It automates the process of creating phishing pages for various websites, such as social media platforms and email services. The tool is typically used by ethical hackers and penetration testers to test the security of a system, but can also be used by malicious actors for illegal activities."    
    template.template("ShellPhish", "./shellphish.sh", github.strip(), {"Shellphish Tool": "https://www.kalilinux.in/2019/04/shellphish-phishing-page-creator.html"},
                                      method="github", github_install="git clone https://github.com/AbirHasan2005/ShellPhish && cd ShellPhish && chmod +x shellphish.sh", github_check="ShellPhish")


def keylogger():
    github = "Welcome to the simple keylogger repo! A keylogger is a program that records your keystrokes, and this program saves them in a log file on your local computer."
    template.template("Keylogger", "python Keylogger.py", github.strip(), {
                                      "How to Set Up Keylogging on Your Linux Computer": "https://www.makeuseof.com/set-up-keylogging-on-linux/"}, method="github",github_install="git clone https://github.com/GiacomoLaw/Keylogger.git && cd Keylogger/linux && pip install -r requirements.txt ", github_check="Keylogger")

def camphish():
    github = "CamPhish is techniques to take cam shots of target's phone front camera or PC webcam. CamPhish Hosts a fake website on in built PHP server and uses ngrok & serveo to generate a link which we will forward to the target, which can be used on over internet. website asks for camera permission and if the target allows it, this tool grab camshots of target's device."
    template.template("CamPhish", "camphish", github.strip(), {"How To Access Android Phone Camera Using Kali Linux": "https://blog.hackerassociate.com/how-to-access-android-phone-camera-using-kali-linux/", "Hack Android Phone Camera using CamPhish":
                                      "https://systemweakness.com/hack-android-phone-camera-using-camphish-9d6126ae7786"}, method="github", github_install="git clone https://github.com/techchipnet/CamPhish && cd CamPhish && bash camphish.sh", github_check="camphish")


if __name__ == "__main__":
    main()
