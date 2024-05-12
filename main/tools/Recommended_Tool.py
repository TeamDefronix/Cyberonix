from main.tools import banner, waiting, writeup, colors, run_on_browser, Recommended_Tool,template
import os
import readline
targets = []
# Function for recommmended tools
def recommended(name):
    #print(f"{name}")
    if name.lower() == "nmap":
        nmap(name)
    elif name.lower() == "subfinder":
        subfinder(name)
    elif name.lower() == "red_hawk":
        os.system("cd Tools/RED_HAWK && php rhawk.php")
    elif name.lower() == "dracnmap":
        os.system("cd Tools/Dracnmap && ./dracnmap-v2.2.sh")
    elif name.lower() == "hping3":
        hping3(name)
    elif name.lower() == "arping":
        arping(name)
    elif name.lower() == "netdiscover":
        netdiscover(name)
    elif name.lower() == "theharvester":
        theHarvester(name)
    elif name.lower() == "wafw00f":
        wafw00f(name)
    elif name.lower() == "spiderfoot":
        spiderfoot(name)
    elif name.lower() == "th3inspector":
        os.system("cd Tools/Th3inspector && perl ./Th3inspector.pl")
    elif name.lower() == "amass":
        amass(name)
    elif name.lower() == "sublist3r":  
        sublist3r(name)

####################################   Vulnerability Analysis Tools   ##########################################################
    elif name.lower() == "wpscan":
        wpscan(name)
    elif name.lower() == "wapiti":
        wapiti(name)
    elif name.lower() == "nikto":
        nikto(name)
    elif name.lower() == "wfuzz":
        wfuzz(name)
    
####################################   Web Application Analysis Tools   ########################################################
    elif name.lower() == "dirb":
        dirb(name)
    elif name.lower() == "ffuf":
        ffuf(name)
    elif name.lower() == "nuclei":
        nuclei(name)
    elif name.lower() == "dirsearch":
        dirsearch(name)

####################################  Password Hacking Tools   ##################################################################
    elif name.lower() == "hydra":
        hydra(name)
    elif name.lower() == "reaver":
        reaver(name)
    elif name.lower() == "hashcat":
        hashcat(name)
    elif name.lower() == "john":
        john(name)
    elif name.lower() == "medusa":
        medusa(name)
    elif name.lower() == "ncrack":
        ncrack(name)
    elif name.lower() == "rainbowcrack":
        rainbowcrack(name)
    elif name.lower() == "cupp":
        os.system("cupp -i")
    elif name.lower() == "keylogger":
        print(f"{colors.options}keylogger is started...{colors.reset}\n")
        print(f"{colors.red} press ctrl + c to stop keylogger  {colors.reset}\n")
        os.system("cd Tools/Keylogger/linux && python3 keylogger.py ")
        path = template.check_path("Cyberonix")
        print(f"Output saved to {path}/Tools/Keylogger/")
        print(f"\nOutput saved to {path}/Tools/Keylogger/")
    elif name.lower() == "shellphish":
        os.system("cd Tools/ShellPhish && ./shellphish.sh")

    elif name.lower() == "r3bu5":
        os.system("cd Tools/r3bu5 && chmod +x r3bu5.sh && ./r3bu5.sh")
    elif name.lower() == "zphisher":
        os.system("cd Tools/zphisher  && chmod +x zphisher.sh && bash zphisher.sh")
    elif name.lower() == "camphish":
        os.system("cd Tools/CamPhish && bash camphish.sh")
    elif name.lower() == "hiddeneye":
        os.system("cd Tools/HiddenEye && python HiddenEye.py")
    elif name.lower() == "crunch":
        print("Please refer crunch writeups for wordlist Generation")
        command_line(name)
    elif name.lower() == "set":
        os.system("setoolkit")
    elif name.lower() == "gophish":
        os.system("cd Tools/Gophish && gophish")  
####################################  wireless attack   #######################################################################
    elif name.lower() == "fluxion":
        os.system("cd Tools/fluxion && ./fluxion.sh")

    elif name.lower() == "aircrack-ng":
        aircrack_ng(name)

####################################  Exploiation Tools   #######################################################################
    elif name.lower() == "metasploit-framework":
        os.system("msfconsole")
    elif name.lower() == "crackmapexec":
        crackmapexec(name)
    elif name.lower() == "exploitdb":
        searchsploit("searchsploit")
    elif name.lower() == "sqlmap":
        sqlmap(name)

####################################  sniffing and spoofing Tools   ###################################################################
    elif name.lower() == "macchanger":
        command_line(name)
    elif name.lower() == "responder":
        command_line(name)
####################################  Post Exploitation Tools   #######################################################################
    elif name.lower() == "linpeas":
        linpeas(name)
    elif name.lower() == "linenum":
        linenum(name)
    elif name.lower() == "sudo killer":
        sudo_killer(name)
    elif name.lower() == "beroot":
        os.system("cd Tools/BeRoot/Linux && chmod u+x * && ./beroot.py")
    elif name.lower() == "linux-exploit-suggester-2":
        linux_exploit_suggester_2(name)
    elif name.lower() == "linux-smart-enumeration":
        linux_smart_enumeration(name)
    elif name.lower() == "pspy64":
        pspy64(name)
    elif name.lower() == "upx (ultimate packer for executable)":
        upx(name)
    elif name.lower() == "linux-private-i":
        os.system("cd Tools/linux-private-i && ./private-i.sh")

###################################  Anonimity Tools   #######################################################################
    elif name.lower() == "kali-anonsurf":
        anonsurf(name)
    elif name.lower() == "proxychains":
        print("proxychains is running...")
        os.system("proxychains firefox")
    elif name.lower() == "nipe":
        nipe(name)
    elif name.lower() == "tor":
        tor(name)

###################################  configuration management #######################################################################
    elif name.lower() == "gobuster":
        gobuster(name)
    elif name.lower() == "securityheaders":
        os.system("cd Tools/securityheaders && python3 securityheaders.py")
    elif name.lower() == "secretfinder":
        secretfinder(name)
    
    elif  name.lower() == "httpie":
        httpie(name)
    elif name.lower() == "feroxbuster":
        feroxbuster(name)
    elif name.lower() == "ptf":
        os.system("cd Tools/ptf && ./ptf")


###################################      Data validation #######################################################################

    elif name.lower() == "xsstrike":
        xsstrike(name)
    elif name.lower() == "dalfox":
        dalfox(name)
###################################  Data validation #######################################################################
    elif name.lower() == "oralyzer":
        oralyzer(name)

    elif name.lower() == "openredirex":
        openredirex(name)
    elif name.lower() == "xsser":
        choice = input(f"{colors.select} Press 1 for GUI interface and press 2 for command line interface: {colors.reset}")
        if choice ==  '1':
            os.system("xsser --gtk")
        elif choice ==   '2':
            os.system("xsser  --wizard")

##################################  DOS ATTACK  #######################################################################
    
    elif name.lower() == "goldeneye":
        goldeneye(name)
    elif name.lower() == "thc-ssl-dos":
        thcssldos(name)
    elif name.lower() == "slowloris":
        slowloris(name)
    elif name.lower() == "slowhttptest":
        slowhttptest(name)
###################################  Cryptography  #######################################################################
    elif name.lower() == "sslyze":
        sslyze(name)

    elif name.lower() == "sslscan":
        sslscan(name)        
    elif name.lower() == "o-saft":
        o_saft(name)
    elif name.lower() == "ettercap-graphical":
        os.system("ettercap -G")
###################################  File Upload  #######################################################################

    elif name.lower() == "fuxploider":
        fuxploider(name)
###################################  Risk func payment #######################################################################
    elif name.lower() == "fiddler":
        os.system("cd Tools/fiddler && mono Fiddler.exe")
###################################  NEW Bug BOUNTY SECITON #######################################################################
###################################  Exploitation #######################################################################
    elif name.lower() == "masscan":
        masscan(name)
    elif name.lower()  == "unicornscan":
        unicornscan(name)

    elif name.lower() == "dnsrecon":
        dnsrecon(name)
  
###################################  Reporting Tools #######################################################################    
    elif name.lower() == "recordmydesktop":
        recordmydesktop(name)
    elif name.lower() == "pipal":
        pipal(name)
###################################  Digital Forensic Tool #######################################################################
    elif name.lower() == "autopsy":
        autopsy()
    elif name.lower() == "hashdeep":
        hashdeep(name)
    elif name.lower() == "binwalk":
        binwalk(name)
    elif name.lower() == "bulk-extractor":
        bulk_extractor(name)
    else:
        os.system(f"{name}")

    

def ip_valid(user_input):
        parts = user_input.split(".")
        for part in parts:
            try:
                part=int(part)
                if len(parts) == 4:
                    is_ip_address = True
                    for part in parts:
                        if not part.isdigit() or not (0 <= int(part) <= 255):
                            is_ip_address = False
                            break
                    if is_ip_address:
                        return 1
                    else:
                        return 2
                else:
                    return 2
            except Exception as e:
                return 2       
#command_line function
def command_line(name):
    try:
        template.load_banner(name)
        command=""
        while not command:
            command = input(f"\n {colors.select}Enter a command : {colors.reset}")
            if "exit" in command:
                break
            elif not command.strip(): 
                template.load_banner(name)
                continue
            elif name not in command:
                template.load_banner(name)
                print(f"\n{colors.red} please use only {name} command {colors.reset}\n")
                command = None
                continue
            else:
                template.load_banner(name)
                os.system(command)
    except KeyboardInterrupt:
        return
    
def change_target(name):
    try:
        template.load_banner(name)
        target = input(f"\n{colors.select}Enter a target : {colors.reset}")
        while not target:
            print(f"\n{colors.red} Please valid enter the target{colors.reset}\n")
            target = input(f"\n{colors.select}Enter a target : {colors.reset}")
        targets.clear()
        targets.append(target)
    except KeyboardInterrupt:
        return
#change target function
def change_ip(name):
    try:
        while True:
            template.load_banner(name)
            target = input(f"\n{colors.select}Enter a ip : {colors.reset}")
            if not target:
                print(f"\n{colors.red} Please enter the ip{colors.reset}\n")
                continue
            valid = ip_valid(target)
            if valid == 2:
                template.load_banner(name)
                print(f"\n{colors.red}Please enter a valid IP. {colors.reset}\n")
                continue
            # If the target is valid, clear the targets list and append the new target
            targets.clear()
            targets.append(target)
            break  # Break out of the loop since a valid target has been entered

    except KeyboardInterrupt:
        return
####################################   Information Gathering Tools   ###############################
def nmap(name):
    try:
        template.load_banner(name)
        while True:
            # To check target is empty
            if not targets:
                target = input(f"\n{colors.select}Enter a target : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nTarget : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Aggressive scan \t\t (Recommended)","Efficient Scan ", "Fast Scan", "Intense Scan","Scan for Vulnerabilities using NSE Scripts","Change Target" ,"Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Aggressive Scan is running",colors.reset)
                os.system(f"cd output && nmap -A -T4 {targets[0]} -oN nmap")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/nmap \n")
                continue
            elif option=="2":
                template.load_banner(name)
                print(colors.options,f"\nEfficient Scan is running",colors.reset)
                os.system(f"cd output && nmap -sV -A -T4 -p- --script=default,auth,vuln,safe {targets[0]} -oN nmap ") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/nmap \n")
                continue
            elif option=="3":
                template.load_banner(name)
                print(colors.options,f"Fast Scan is running",colors.reset)
                os.system(f"cd output && nmap -F -T4 {targets[0]} -oN nmap ")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/nmap \n")
                continue
            elif option=="4":
                template.load_banner(name)
                print(colors.options,f"Intense Scan is running",colors.reset)
                os.system(f"cd output && nmap -p- -sV -sS -A -T4 {targets[0]} -oN nmap ")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/nmap \n")
                continue
            elif option=="5":
                template.load_banner(name)
                print(colors.options,f"Scan for Vulnerabilities using NSE Scripts:",colors.reset)
                os.system(f"cd output && nmap --script=vuln  {targets[0]} -oN nmap")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/nmap \n")
                continue
            elif option=="6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option=="8":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def subfinder(name):
    try:
        template.load_banner(name)
        while True:
            # To check target is empty
            if not targets:
                target = input(f"\n{colors.select}Enter a domain : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Subdomain discovery \t\t (Recommended)","Efficient subdomain discovery","Fast Scan", "Only Active Subdomain","Advanced subfinder Command","Change Target" ,"Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
                            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Subdomain discovery is running",colors.reset)
                os.system(f"cd output && subfinder -d {targets[0]} -o output.txt -nW  -timeout 30 -t 100 -recursive -o subfinder")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/subfinder \n")
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Efficient subdomain discovery running",colors.reset)
                os.system(f"cd output && subfinder -d {targets[0]} -o output.txt  -recursive -sources censys,shodan -r 1.1.1.1,8.8.8.8 -t 100 -max-time 5 -o subfinder")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/subfinder \n")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Fast discovery running",colors.reset)
                os.system(f"cd output && subfinder -d {targets[0]} -o output.txt  -max-time 5 -o subfinder")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/subfinder \n")
                continue
            elif option=="4":
                template.load_banner(name)
                print(colors.options,f"Active Subdomain discovery is running",colors.reset)
                os.system(f"cd output && subfinder -d {targets[0]}  -o {targets[0]}.json -nW -o subfinder")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/subfinder \n")
                continue
            elif option=="5":
                template.load_banner(name)
                print(colors.options,f"Advanced subfinder Command is running...",colors.reset)
                os.system(f"cd output && subfinder -d {targets[0]}  | grep -oE '[a-zA-Z0-9.-]+\.[a-zA-Z]{{2,}}' -o subfinder")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/subfinder \n")
                continue
            elif option=="6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option=="8":
                break
            else:
                break
    except KeyboardInterrupt:
        return
        
def hping3(name):
    try:
        template.load_banner(name)
        while True:  # Infinite loop until explicitly broken 
            if not targets:
                target = input(f"\n{colors.select}Enter an IP : {colors.reset}")
                if not target:
                    continue  # If target is empty, restart the loop
                valid = ip_valid(target)
                if valid == 2:
                    template.load_banner(name)
                    print(f"\n{colors.red}Please enter a valid IP. {colors.reset}")  
                    continue  # If the IP is invalid, restart the loop
                targets.append(target)

            print(colors.options, f"\nDomain: {targets[0]}", colors.reset)
            print(f"\n{colors.select}Select an option:", colors.reset)
            list_attacks = [
                "Create a SYN package and use scan mode to scan port 1 through 1000 \t\t (Recommended)",
                "Perform a charge test on port",
                "Ping an IP address over TCP on a specific port",
                "DoS Attack with Hping3",
                "Change Target",
                "Command Line",
                "Exit"
            ]
            for i, attack in enumerate(list_attacks, 1):
                print(colors.options, f"{i}) {attack.title()}", colors.reset)

            option = input(f"\n{colors.select}Select an option: {colors.reset}")

              # If option is empty, restart the loop

            if option == "1":
                template.load_banner(name)
                port = int(input("\nEnter the Port Number: "))
                print(colors.options, "hping3 is running...", colors.reset)
                os.system(f"hping3 {targets[0]} -8 1-1024 -S")
                continue
            elif option == "2":
                template.load_banner(name)
                port = int(input("\nEnter the Port Number: "))
                print(colors.options, "hping3 is running with flooding...", colors.reset)
                os.system(f"hping3 --flood -p {port} -S {targets[0]}")
                continue
            elif option == "3":
                template.load_banner(name)
                port = int(input("\nEnter the Port Number: "))
                print(colors.options, "hping3 is running...", colors.reset)
                os.system(f"hping3 -p {port} -S {targets[0]} ")
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options, "hping3's DOS Attack is running...", colors.reset)
                os.system(f"hping3 --flood -S -V --rand-source {targets[0]}")
                continue
            elif option == "5":
                change_target(name)
                continue  # Placeholder for change_target function
            elif option == "6":
                command_line(name)
                continue  # Placeholder for command_line function
            elif option == "7":
                break   
            else:
                break
    except KeyboardInterrupt:
        return


def arping(name):
    try:
       template.load_banner(name)
       while True:
            if not targets:
                target = input(f"\n{colors.select}Enter an IP : {colors.reset}")
                if not target:
                    continue  # If target is empty, restart the loop
                valid = ip_valid(target)
                if valid == 2:
                    template.load_banner(name)
                    print(f"\n{colors.red}Please enter a valid IP. {colors.reset}")  
                    continue  # If the IP is invalid, restart the loop
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["ARP Request to Single Host \t\t (Recommended)","ARP Request with Custom Packet Size","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"ARP request is running",colors.reset )
                os.system(f"arping -c 4 {targets[0] }") 
                continue
            elif option == "2":
                template.load_banner(name)
                timeout=int(input("Enter Timeout value : "))
                print(colors.options,f"ARP request is running",colors.reset )
                os.system(f"arping -c 4 -p {targets[0] } -w {timeout}")
                continue
            elif option=="3":
                change_ip(name)
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option=="5":
                break
            else:
                break
    except KeyboardInterrupt:
        return



def netdiscover(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target IP : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Discover Devices on the Local Network \t\t (Recommended)","Specify the Network Interface","Enable Passive Mode","Scan in Fast Mode","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")

            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Netdiscover is scanning for Discover Devices on the Local Network",colors.reset )
                os.system("sudo netdiscover") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Netdiscover is scanning for Specify the Network Interface",colors.reset)
                os.system("sudo netdiscover -i eth0")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Netdiscover is scanning in Passive Mode",colors.reset )
                os.system("sudo netdiscover -p")
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Netdiscover is scanning in fast mode",colors.reset )
                os.system(f"sudo netdiscover -r {targets[0] }") 
                continue
            
            elif option == "5":
                command_line(name)
                continue
            elif option=="6":
                break
            else:
                break
    except KeyboardInterrupt:
        return
def theHarvester(name):
    try:
        template.load_banner(name)
        while True:
            # To check target is empty
            if not targets:
                target = input(f"\n{colors.select}Enter a domain : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Full Scan \t\t (Recommended)","Normal Scan","Advanced scan","Advanc scan + shodan ","Complete scan","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Full Scan is running...",colors.reset )
                os.system(f"cd output && theHarvester -d {targets[0]} -b anubis,baidu,bevigil,binaryedge,bing,bingapi,bufferoverun,brave,censys,certspotter,criminalip,crtsh,dnsdumpster,duckduckgo,fullhunt,github-code,hackertarget,hunter,hunterhow,intelx,netlas,onyphe,otx,pentesttools,projectdiscovery,rapiddns,rocketreach,securityTrails,sitedossier,subdomaincenter,subdomainfinderc99,threatminer,tomba,urlscan,virustotal,yahoo,zoomeye -f testing -l 500 -n -f theharvester") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/subfinder \n")
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Normal Scan is running...",colors.reset)
                os.system(f" cd output && theHarvester -d {targets[0]} -b anubis,baidu,bevigil,binaryedge,bing,bingapi,bufferoverun,brave,censys,certspotter,criminalip,crtsh,dnsdumpster,duckduckgo,fullhunt,github-code,hackertarget,hunter,hunterhow,intelx,netlas,onyphe,otx,pentesttools,projectdiscovery,rapiddns,rocketreach,securityTrails,sitedossier,subdomaincenter,subdomainfinderc99,threatminer,tomba,urlscan,virustotal,yahoo,zoomeye -f theharvester")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/subfinder \n")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Advanced scan is running...",colors.reset )
                os.system(f"cd output && theHarvester -d {targets[0]} -b anubis,baidu,bevigil,binaryedge,bing,bingapi,bufferoverun,brave,censys,certspotter,criminalip,crtsh,dnsdumpster,duckduckgo,fullhunt,github-code,hackertarget,hunter,hunterhow,intelx,netlas,onyphe,otx,pentesttools,projectdiscovery,rapiddns,rocketreach,securityTrails,sitedossier,subdomaincenter,subdomainfinderc99,threatminer,tomba,urlscan,virustotal,yahoo,zoomeye -f Testing -f theharvester")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/subfinder \n")
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Advanc scan + shodan scan is running...",colors.reset )
                os.system(f"cd output && theHarvester -d {targets[0]} -b anubis,baidu,bevigil,binaryedge,bing,bingapi,bufferoverun,brave,censys,certspotter,criminalip,crtsh,dnsdumpster,duckduckgo,fullhunt,github-code,hackertarget,hunter,hunterhow,intelx,netlas,onyphe,otx,pentesttools,projectdiscovery,rapiddns,rocketreach,securityTrails,sitedossier,subdomaincenter,subdomainfinderc99,threatminer,tomba,urlscan,virustotal,yahoo,zoomeye -f test -l 1000 -s -f theharvester") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/subfinder \n")
                continue
            elif option == "5":
                template.load_banner(name)
                print(colors.options,f"Complete scan is running...",colors.reset )
                os.system(f"cd output && theHarvester -d {targets[0]} -b anubis,baidu,bevigil,binaryedge,bing,bingapi,bufferoverun,brave,censys,certspotter,criminalip,crtsh,dnsdumpster,duckduckgo,fullhunt,github-code,hackertarget,hunter,hunterhow,intelx,netlas,onyphe,otx,pentesttools,projectdiscovery,rapiddns,rocketreach,securityTrails,sitedossier,subdomaincenter,subdomainfinderc99,threatminer,tomba,urlscan,virustotal,yahoo,zoomeye -f testing -l 1000 -s -n -r -t -f theharvester")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/subfinder \n")
                continue
            elif option=="6":
                change_target(name)
                continue
            elif option == "7":
                command_line("theHarvester")
                continue
            elif option=="8":
                break
            else:
                break
    except KeyboardInterrupt:
        return
def wafw00f(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Scan Multiple URLs from a File \t\t (Recommended)","Basic scan","No Redirects","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                file = input(f"\n {colors.select}Enter the path of url file : {colors.reset}")
                print(colors.options,f"wafw00f scanning multiple url's",colors.reset )
                os.system(f"wafw00f -i {file}") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"wafw00f basic scan is running",colors.reset)
                os.system(f"wafw00f {targets[0]}")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"wafw00f No Redirects scan is running",colors.reset )
                os.system(f"wafw00f -r {targets[0] }")
                continue
            elif option=="4":
                change_target(name)
                continue
            elif option == "5":
                command_line(name)
                continue
            elif option == "6":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def spiderfoot(name):
    try:
       template.load_banner(name)
       while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target Domain (like example.com): {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Full scan \t\t (Recommended)", "Advance Scan" ,"Normal scan","Debug scan or module ","Aggressive scan ","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Full scan is running...",colors.reset )
                os.system(f"spiderfoot -s {targets[0]} -d -m mod1,mod2 -n -t type1,type2") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Advance Scan is running...",colors.reset )
                os.system(f"spiderfoot -s {targets[0]} -u all -F domain,dns,dns-resolver,ipv4,ipv6,whois,service,open-port,netblock,ip-block") 
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Normal scan is running...",colors.reset )
                os.system(f" spiderfoot -s {targets[0]}") 
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Debug scan or module is running...",colors.reset )
                os.system(f"spiderfoot -s {targets[0]} -d -m mod1,mod2") 
                continue
            elif option == "5":
                template.load_banner(name)
                print(colors.options,f"Aggressive scan is running...",colors.reset )
                os.system(f"spiderfoot -m sfp_dnsresolve,sfp_whois,sfp_censysio,sfp_shodanhost,sfp_virustotal,sfp_googlesearch -s {targets[0]} -o json ") 
                continue
            elif option== "6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option == "8":
                break
            else:
                break
    except KeyboardInterrupt:
        return
def amass(name):
    try:
       template.load_banner(name)
       while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Active Reconnaissance \t\t (Recommended)", "IP discovery" ,"Custom port scan","Custom proxy","Aggressive Scan","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Full scan is running...",colors.reset )
                os.system(f"cd output && amass enum -active -r 8.8.8.8,1.1.1.1 -d {targets[0]} -o amass.txt ") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/amass.txt \n")
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"IP discovery scan is running...",colors.reset )
                os.system(f"cd output && amass intel -ip -whois -v -d {targets[0]} -o amass.txt ") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/amass.txt \n")
                continue
            elif option == "3":
                template.load_banner(name)
                port = input("Enter the port number: ")
                print(colors.options,f"Custom port scan is running...",colors.reset )
                os.system(f"cd output && amass enum -active -p {port} -max-dns-queries 2500 -d {targets[0]} -o amass.txt ") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/amass.txt \n")
                continue
            elif option == "4":
                template.load_banner(name)
                proxy = input("Enter proxy url : ")
                print(colors.options,f"scan with custom proxy is running...",colors.reset )
                os.system(f"cd output && amass enum -active --proxy {proxy} -d {targets[0]} -o amass.txt ") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/amass.txt \n")
                continue
            elif option == "5":
                template.load_banner(name)
                print(colors.options,f"Aggressive scan is running...",colors.reset )
                os.system(f"cd output &&amass enum  -brute -max-depth 5 -dns-qps 1000  -d {targets[0]} -o amass.txt ") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/amass.txt \n")
                continue
            elif option== "6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option == "8":
                break
            else:
                break
    except KeyboardInterrupt:
        return
    
def sublist3r(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter the domain: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Full scan \t\t (Recommended)", "Advance Scan" ,"Normal scan","Aggressive scan ","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                port = input("Enter port number: ")
                print(colors.options,f"Full scan is running...",colors.reset )
                os.system(f"cd output && sublist3r -d {targets[0]} -b -p {port} -v -t 500 -e bing.com,google.com -o sublister") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/sublister \n")
                continue
            elif option == "2":
                template.load_banner(name)
                port = input("Enter port number: ")
                print(colors.options,f"Advance Scan is running...",colors.reset )
                os.system(f"cd output && sublist3r -d {targets[0]} -b -p {port} -v -t 500 -o sublistert") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/sublister \n")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Normal scan is running...",colors.reset )
                os.system(f"cd output && sublist3r -d {targets[0]} -o sublister") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/sublister \n")
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Aggressive scan is running...",colors.reset )
                os.system(f"cd output && sublist3r -d {targets[0]} -b -p 80 -e google.com,bing.com -v -o sublister") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/sublister \n")
                continue
            elif option== "5":
                change_target(name)
                continue
            elif option == "6":
                command_line(name)
                continue
            elif option =="7":
                break
            else:
                break
    except KeyboardInterrupt:
        return
####################################   Vulnerability Analysis Tools   ##########################################################
def wpscan(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Enumerate Plugins \t\t (Recommended)","Enumerate user","Basic Scan","vulnerable plugins","vulnerable themes","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"wpscan running for enumerate plugin",colors.reset )
                os.system(f"wpscan --url {targets[0]} --enumerate p --random-user-agent") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"wpscan running for enumerate user",colors.reset )
                os.system(f"wpscan --url {targets[0]} --enumerate u --random-user-agent") 
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"wpscan running on Basic scan",colors.reset )
                os.system(f"wpscan --url {targets[0]}") 
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"wpscan running on Vulnerable plugins",colors.reset )
                os.system(f"wpscan --url {targets[0]} --enumerate vp") 
                continue
            elif option == "5":
                template.load_banner(name)
                print(colors.options,f"wpscan running on Vulnerable themes",colors.reset )
                os.system(f"wpscan --url {targets[0]} --enumerate vt") 
                continue
            elif option== "6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option == "8":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def wapiti(name):
    targets = []
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url like https://example.com: {colors.reset}")
                if not target:
                    template.load_banner(name)
                    continue
                targets.append(target)
            print (colors.options,f"\nUrl : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Full scan \t\t (Recommended)","Advance scan","Scan with specific modules ","Aggressive scan ","Auth Scan","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Full scan is running...",colors.reset )
                os.system(f"cd output && wapiti -u {targets[0]} --auth-type basic --flush-attacks -t 5 -H1000 -A 1000 -o wapati") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/wapiti \n")
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Advance scan is running...",colors.reset )
                os.system(f"cd output && wapiti -u {targets[0]} --scop page -o wapati") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/wapiti \n")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Scan with specific modules is running...",colors.reset )
                os.system(f"cd output && wapiti -u {targets[0]} -m \"xss, sqli\" -l 2 -o wapati") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/wapiti \n")
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Aggressive scan is running...",colors.reset )
                os.system(f"cd output && wapiti -u {targets[0]}  -S aggressive -o wapati") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/wapiti \n")
                continue
            elif option == "5":
                template.load_banner(name)
                print(colors.options,f"Authorization Scan is running...",colors.reset )
                os.system(f"cd output && wapiti -u {targets[0]}  --auth-type basic -o wapati") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/wapiti \n")
                continue
            elif option== "6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option =="8":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def wfuzz(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url like https://example.com: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Full scan \t\t (Recommended)","Fuzzing with range","Basic Fuzzing","Aggressive scan ","Fuzzing with cookie","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Full scan is running...",colors.reset )
                os.system(f"wfuzz -c --hc 404 -z range,1-5 --sc 200  {targets[0]}/FUZZ") 
                
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Fuzzing with range is running...",colors.reset )
                os.system(f"wfuzz -c -z range,1-15 {targets[0]}/FUZZ") 
                continue
            elif option == "3":
                template.load_banner(name)
                wordlist = input("Enter path of wordlist : ")
                print(colors.options,f"Basic Fuzzing is running...",colors.reset )
                os.system(f"wfuzz -c -z file,{wordlist} --hc 404 {targets[0]}/FUZZ") 
                continue
            elif option == "4":
                template.load_banner(name)
                wordlist = input("Enter path of wordlist : ")
                print(colors.options,f"Aggressive scan is running...",colors.reset )
                os.system(f"wfuzz -c --hc 404 -z file,{wordlist} --hh 2 -z range,1-10 --hl 20 -t 20 {targets[0]}/FUZZ.php") 
                continue
            elif option == "5":
                template.load_banner(name)
                wordlist = input("Enter path of wordlist : ")
                cookie_value = input("Enter cookie value : ")
                print(colors.options,f"Fuzzing with cookie is running...",colors.reset )
                os.system(f"wfuzz -c --hc 404 -z file,{wordlist} --cookie \"{cookie_value}=FUZZ\" {targets[0]}") 
                continue
            elif option== "6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option =="8":
                break
            else:
                break
    except KeyboardInterrupt:
        return
####################################   Web Application ANAlysis Tools   ###############################

def nikto(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Scan with User-Agent Customization \t\t (Recommended)","Basic scan with SSL Forced","Scan with Extended Evasion Techniques","Scan with Disabling SSL","Scan with Ignoring Specific HTTP Codes","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                timeout=input("\n\nEnter time out(like20,30,50etc) : ")
                targets.append(timeout)
                maxtime=input("\n\nEnter maxtime:")
                targets.append(maxtime)
                print(colors.options,f"Scan is running...",colors.reset )
                os.system(f"""nikto -host {targets[0]} -useragent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" -timeout {targets[1]} -maxtime {targets[2]}""") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Scan is running...",colors.reset )
                os.system(f"nikto -host {targets[0]} -ssl")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Scan is running...",colors.reset )
                os.system(f"""nikto -host {targets[0]}  -evasion '1,3,6,8'""")
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Scan is running...",colors.reset )
                os.system(f"nikto -host {targets[0]} -nossl")
                continue
            elif option == "5":
                template.load_banner(name)
                print(colors.options,f"Scan is running...",colors.reset )
                os.system(f"""nikto -host {targets[0]} -404code '301,302'""")
                continue
            elif option== "6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option == "8":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def dirb(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    dirb(name)
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Specifying a custom output file \t\t (Recommended)","Limiting the scan depth with multiple threads","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                wordlist=input("\n\nEnter wordlist path : ")
                targets.append(wordlist)
                wordlist1=input("\n\nEnter which path you want to save: ")
                targets.append(wordlist1)
                print(colors.options,f"Dirb is running...",colors.reset )
                os.system(f"dirb {targets[0]} {targets[1]} -t -v -i -o {targets[2]}") 
                continue
            elif option == "2":
                template.load_banner(name)
                wordlist=input("\n\nEnter How much thread want to running : ")
                targets.append(wordlist)
                print(colors.options,f"Dirb is running...",colors.reset )
                os.system(f"dirb {targets[0]} -r 3 -t {targets[1]} -v -S")
                continue
            # elif option == "3":
            #     template.load_banner(name)
            #     wordlist=input("\n\nEnter wordlist path: ")
            #     targets.append(wordlist)
            #     print(colors.options,f"Dirb is running...",colors.reset )
            #     os.system(f"dirb {targets[0]} -r 3 -t {targets[1]} -v -S")
            #     continue
            elif option== "3":
                change_target(name)
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option=="5":
                break
            else:
                break
    except KeyboardInterrupt:
        return
        
def ffuf(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["explore deeper with recursion \t\t (Recommended)","Recommended for better output","filter out responses with 404/403 status codes","fuzzing with Threads and redirects","save output for reviewing and record-keeping","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                wordlist=input("\n\nEnter wordlist path : ")
                targets.append(wordlist)
                depth=input("""\n\nEnter how much depth you want to scan (like "1 to 4"): """)
                targets.append(depth)
                print(colors.options,f"fuzzing...",colors.reset )
                os.system(f"cd output && ffuf -u {targets[0]}/FUZZ -w {targets[1]} -recursion -recursion-depth {targets[2]} -o ffuf") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/ffuf \n")
                continue
            elif option == "2":
                template.load_banner(name)
                wordlist=input("\n\nEnter wordlist path : ")
                targets.append(wordlist)
                print(colors.options,f"fuzzing...",colors.reset )
                os.system(f"cd output && ffuf -u {targets[0]}/FUZZ -w {targets[1]} -of html -o ffuf") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/ffuf \n")
                continue
            elif option == "3":
                template.load_banner(name)
                wordlist=input("\n\nEnter wordlist path : ")
                targets.append(wordlist)
                print(colors.options,f"fuzzing...",colors.reset )
                os.system(f"cd output && ffuf -u {targets[0]}/FUZZ -w {targets[0]} -fc 404,403 -o ffuf") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/ffuf \n")
                continue
            elif option == "4":
                template.load_banner(name)
                wordlist=input("\n\nEnter wordlist path : ")
                targets.append(wordlist)
                threads=input("\n\nEnter How many threads you want to fuzzing: ")
                targets.append(threads)
                redirect=input("\n\nEnter How many redirects you want to fuzzing : ")
                targets.append(redirect)
                print(colors.options,f"fuzzing... ",colors.reset )
                os.system(f"cd output && ffuf -u {targets[0]}/FUZZ -w {targets[1]} -t {targets[3]} -fr {targets[4]} -o ffuf") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/ffuf \n")
                continue
            elif option == "5":
                template.load_banner(name)
                wordlist=input("\n\nEnter wordlist path : ")
                targets.append(wordlist)
                print(colors.options,f"fuzzing... ",colors.reset )
                os.system(f"cd output && ffuf -u {targets[0]}/FUZZ -w {targets[1]} |  -o ffuf") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/ffuf \n")
                continue
            elif option== "6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option == "8":
                break
            else:
                break
    except KeyboardInterrupt:
        return
        

def nuclei(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Advance scan \t\t (Recommended)","Scan With vesrion","Basic scan","Scan with new template","Ip version scan","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"nuclei is running... ",colors.reset )
                os.system(f"nuclei -u {targets[0]} -sa -iv 4,6 -nt -as -nss -td -tl -code -json-export output.json") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"nuclei is running... ",colors.reset )
                os.system(f"nuclei -u {targets[0]} -sa -iv 4,6 -nt -as – version") 
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"nuclei is running... ",colors.reset )
                os.system(f"nuclei -u {targets[0]} -sa") 
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"nuclei is running... ",colors.reset )
                os.system(f"nuclei -u {targets[0]} -sa -iv 4,6 -nt -as ") 
                continue
            elif option == "5":
                template.load_banner(name)
                print(colors.options,f"nuclei is running... ",colors.reset )
                os.system(f"nuclei -u {targets[0]} -sa -iv 4,6") 
                continue
            elif option== "6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option == "8":
                break
            else:
                break
    except KeyboardInterrupt:
        return
    
def dirsearch(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["scan with all the extensions with deep recursivnesss \t\t (Recommended)","Use random User-Agent to evade detection","Conduct Deep Bruteforce with Recursive Mode","Deep Recursive scan with Custom Timeout and Delay","Stealthy Reconnaissance with Random User-Agent and Proxy","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"dirsearch is running... ",colors.reset )
                os.system(f"cd output && dirsearch -e php,asp,aspx,jsp,py,txt,conf,config,bak,backup,swp,old,db,sql -u {targets[0]} --force-recursive --skip-on-status=502,500,404,400 -o dirsearch") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/dirsearch \n")
                continue
            elif option == "2":
                template.load_banner(name)
                wordlist=input("\n\nEnter wordlist path: ")
                targets.append(wordlist)
                extension=input("\n\nEnter extension path: ")
                targets.append(extension)
                threads=input("\n\nEnter How many threads you want to fuzzing: ")
                targets.append(threads)
                print(colors.options,f"dirsearch is running... ",colors.reset )
                os.system(f"cd output && dirsearch -u {targets[0]} -w {targets[1]} -e {targets[2]} -t {targets[3]} --random-agent -o dirsearch") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/dirsearch \n")
                continue
            elif option == "3":
                template.load_banner(name)
                wordlist=input("\n\nEnter wordlist path: ")
                threads=input("\n\nEnter How many threads you want to fuzzing: ")
                print(colors.options,f"dirsearch is running... ",colors.reset )
                os.system(f"cd output && dirsearch -u {targets[0]} -w {wordlist} -t {threads} -r -o dirsearch") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/dirsearch \n")
                continue
            elif option == "4":
                template.load_banner(name)
                timeout=input("\n\nEnter time out(like20,30,50etc) : ")
                delay=input("\n\nEnter delay time: ")
                print(colors.options,f"dirsearch is running... ",colors.reset )
                os.system(f"cd output && dirsearch -u {targets[0]} --deep-recursive --timeout {timeout} --delay {delay} -o dirsearch") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/dirsearch \n")
                continue
            elif option == "5":
                template.load_banner(name)
                proxy=input("\n\nEnter your proxy wih port number(like'http://proxy.example.com:8080'): ")
                threads=input("\n\nEnter How many threads you want to fuzzing: ")
                print(colors.options,f"dirsearch is running... ",colors.reset )
                os.system(f"cd output && dirsearch -u {targets[0]} --random-agent --proxy {proxy} --threads {threads} -o dirsearch") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/dirsearch \n")
                continue
            elif option== "6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option == "8":
                break
            else:
                break
    except KeyboardInterrupt:
        return
####################################  Password Hacking Tools  #######################################################################
def hydra(name):
    try:
        template.load_banner(name)
        user=""
        password=""
        while True:
            
            list_attacks=["FTP Brute Force \t\t (Recommended)","SSH Brute Force","SMTP Brute Force","HTTP Basic Authentication Brute Force","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                user = input("Enter the path of the userlist : ")
                password = input("Enter the path of the password file :")
                change_ip(name)
                print(colors.options,f"FTP Brute Force is running...",colors.reset )
                os.system(f"hydra -L {user} -P {password} {targets[0]} ftp") 
                continue
            if option == "2":
                template.load_banner(name)
                user = input("Enter the path of the userlist : ")
                password = input("Enter the path of the password file :")
                change_ip(name)
                print(colors.options,f"SSH Brute Force is running...",colors.reset )
                os.system(f"hydra -L {user} -P {password} {targets[0]} ssh") 
                continue
            if option == "3":
                template.load_banner(name)
                user = input("Enter the path of the userlist : ")
                password = input("Enter the path of the password file :")
                change_ip(name)
                print(colors.options,f"SMTP Brute Force is running...",colors.reset )
                os.system(f"hydra -L {user} -P {password} {targets[0]} smtp") 
                continue
            if option == "4":
                template.load_banner(name)
                user = input("Enter the path of the userlist : ")
                password = input("Enter the path of the password file :")
                change_ip(name)
                print(colors.options,f"HTTP Authentication Brute Force is running...",colors.reset )
                os.system(f"hydra -L {user} -P {password} {targets[0]} http-get") 
                continue
            elif option== "5":
                change_target(name)
                continue
            elif option == "6":
                command_line(name)
                continue
            elif option == "7":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def hashcat(name):
    try:
        template.load_banner(name)
        while True:
            
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Crack sam file password \t\t (Recommended)","NTLM hash crack","MD5 hask crack","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                hashfile = input(f"\n {colors.select} Enter the hashfile path :  {colors.reset}")
                wordlist = input(f"\n {colors.select}Enter the wordlist path : {colors.reset}")
                print(colors.options,f"Windows password cracking... ",colors.reset )
                os.system(f"sudo hashcat -m 1000 -a 0 {hashfile} {wordlist}") 
                continue
            elif option == "2":
                template.load_banner(name)
                hashfile = input(f"\n {colors.select} Enter the NTLM hashfile path :  {colors.reset}")
                wordlist = input(f"\n {colors.select}Enter the wordlist path : {colors.reset}")
                print(colors.options,f"NTLM hash crack... ",colors.reset )
                os.system(f"sudo hashcat -m 1000 -a 0 {hashfile} {wordlist}") 
                continue
            elif option == "3":
                template.load_banner(name)
                hashfile = input(f"\n {colors.select} Enter the MD5 hashfile path :  {colors.reset}")
                wordlist = input(f"\n {colors.select}Enter the wordlist path : {colors.reset}")
                print(colors.options,f"MD5 hask cracking... ",colors.reset )
                os.system(f"sudo hashcat -a 0 -m 1360 {hashfile} {wordlist}") 
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option == "5":
                break
            else:
                break
    except KeyboardInterrupt:
        return
    
def john(name):
    try:
        template.load_banner(name)
        while True:
            
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Password Crack \t\t (Recommended)","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                format = input(f"\n {colors.select} Enter the hash format  :  {colors.reset}")
                hashfile = input(f"\n {colors.select} Enter the hashfile path :  {colors.reset}")
                wordlist = input(f"\n {colors.select}Enter the wordlist path : {colors.reset}")
                print(colors.options,f"Password cracking... ",colors.reset )
                os.system(f"john --format={format} --wordlist={wordlist} {hashfile}") 
                continue
           
            elif option == "2":
                command_line(name)
                continue
            elif option == "3":
                break
            else:
                break
    except KeyboardInterrupt:
        return
    
def medusa(name):
    try:
        template.load_banner(name)
        while True: 
            if not targets:
                target = input(f"\n{colors.select}Enter a Target: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Basic Brute-force Attack \t\t (Recommended)","Brute-force attack against a VNC","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                change_ip(name)
                username = input(f"\n {colors.select} Enter the userlist file path :  {colors.reset}")
                wordlist = input(f"\n {colors.select}Enter the wordlist path : {colors.reset}")
                module = input(f"\n {colors.select}Enter service module like ssh,ftp : {colors.reset}")
                print(colors.options,f"Basic Brute-force Attack... ",colors.reset )
                os.system(f"medusa -h {targets[0]} -u {username} -p {wordlist} -M {module}") 
                continue
            elif option == "2":
                template.load_banner(name)
                change_ip(name)
                username = input(f"\n {colors.select} Enter the userlist file path :  {colors.reset}")
                wordlist = input(f"\n {colors.select}Enter the wordlist path : {colors.reset}")
                print(colors.options,f"Brute-force attack against a VNC... ",colors.reset )
                os.system(f"medusa -h {targets[0]} -u {username} -p {wordlist} -M vnc") 
                continue
            elif option == "3":
                command_line(name)
                continue
            elif option == "4":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def ncrack(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter a Target: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["SSH Password Brute-Force\t\t (Recommended)","FTP Brute-Force","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                change_ip(name)
                username = input(f"\n {colors.select} Enter the username :  {colors.reset}")
                wordlist = input(f"\n {colors.select}Enter the wordlist path : {colors.reset}")
                print(colors.options,f"SSH Password Brute-Force... ",colors.reset )
                os.system(f"ncrack -p 22 --user {username} -P {wordlist} {targets[0]}") 
                continue
            elif option == "2":
                template.load_banner(name)
                change_ip(name)
                username = input(f"\n {colors.select} Enter the username :  {colors.reset}")
                wordlist = input(f"\n {colors.select}Enter the wordlist path : {colors.reset}")
                print(colors.options,f"FTP Password Brute-Force... ",colors.reset )
                os.system(f"ncrack -p 21 --user {username} -P {wordlist} {targets[0]}") 
                continue
            elif option == "3":
                command_line(name)
                continue
            elif option == "4":
                break
            else:
                break
    except KeyboardInterrupt:
        return
def reaver(name):
    try:
        template.load_banner(name)
        while True:
            
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Wifi Attack \t\t (Recommended)","Avoid Detection in Attack","Set maximum Attemps","Advanced WPS attack","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                interface = input(f"\n {colors.select} Enter the interface :  {colors.reset}")
                bssid = input(f"\n {colors.select}Enter the BSSID : {colors.reset}")
                channel = input(f"\n {colors.select}Enter the channel : {colors.reset}")
                print(colors.options,f"Wifi Attak... ",colors.reset )
                os.system(f"reaver -i {interface} -b {bssid} -c {channel} -v") 
                continue
            elif option == "2":
                template.load_banner(name)
                interface = input(f"\n {colors.select} Enter the interface :  {colors.reset}")
                bssid = input(f"\n {colors.select}Enter the BSSID : {colors.reset}")
                time = input(f"\n {colors.select}Enter the time : {colors.reset}")
                print(colors.options,f"Attack without detection... ",colors.reset )
                os.system(f"reaver -i {interface} -b {bssid} -g {time} -v") 
                continue
            elif option == "3":
                template.load_banner(name)
                interface = input(f"\n {colors.select} Enter the interface :  {colors.reset}")
                bssid = input(f"\n {colors.select}Enter the BSSID : {colors.reset}")
                channel = input(f"\n {colors.select}Enter the channel : {colors.reset}")
                attempts = input(f"\n {colors.select}Enter the maximum attempts : {colors.reset}")
                print(colors.options,f"Attack with set maximum attemps... ",colors.reset )
                os.system(f"reaver -i {interface} -b {bssid} -x {attempts} -c {channel} -v") 
                continue
            elif option == "4":
                template.load_banner(name)
                interface = input(f"\n {colors.select} Enter the interface :  {colors.reset}")
                bssid = input(f"\n {colors.select}Enter the BSSID : {colors.reset}")
                channel = input(f"\n {colors.select}Enter the channel : {colors.reset}")
                print(colors.options,f"Advanced WPS attack... ",colors.reset )
                os.system(f"reaver -i {interface} -b {bssid} -a -c {channel} -v") 
                continue
            elif option == "5":
                command_line(name)
                continue
            elif option == "6":
                break
            else:
                break
    except KeyboardInterrupt:
        return
   
def rainbowcrack(name):
    try:
        template.load_banner(name)
        while True:
            
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["RainbowCrack table generation\t\t (Recommended)","RainbowCrack password crack","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                algorithm = input(f"\n {colors.select} Enter the hash algorithm (e.g., md5, sha1):  {colors.reset}")
                charset = input(f"\n {colors.select} Enter the character set for password generation (e.g., numeric, alphanumeric):  {colors.reset}")
                plaintext_length_min = input(f"\n {colors.select} Enter the minimum length of plaintext passwords:  {colors.reset}")
                plaintext_length_max = input(f"\n {colors.select} Enter the maximum length of plaintext passwords:  {colors.reset}")
                filename = input(f"\n {colors.select} Enter the filename to save the generated rainbow tables:  {colors.reset}")
                index_filename = input(f"\n {colors.select} Enter the filename to save the index file:  {colors.reset}")
                print(colors.options,f"RainbowCrack password cracking... ",colors.reset )
                os.system(f"rtgen {algorithm} {charset} {plaintext_length_min} {plaintext_length_max} {filename} {index_filename}") 
                continue
            elif option == "2":
                template.load_banner(name)
                algorithm = input(f"\n Enter the hash algorithm used (e.g., md5, sha1): ")
                hash_filename = input(f"\n Enter the filename path : ")
                rainbow_table_filename = input(f"\n Enter the filename of the rainbow table: ")
                print(colors.options,f"FTP Password Brute-Force... ",colors.reset )
                os.system(f"rcrack{algorithm} {hash_filename} {rainbow_table_filename}") 
                continue
            elif option == "3":
                command_line(name)
                continue
            elif option == "4":
                break
            else:
                break
    except KeyboardInterrupt:
        return
    
####################################  Wireless Attack Tools   #######################################################################

def aircrack_ng(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                os.system("aircrack-ng --help") 
            list_attacks=["Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}){list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                command_line(name)
                continue
            elif option == "2":
                break   
            else:
                break
    except KeyboardInterrupt:
        return


####################################  Exploiation Tools   #######################################################################
def crackmapexec(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter a Target: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Using Threads With SMB  \t\t (Recommended)","With FTP","With SSH","WINRM","MSSQL","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"When SMB Port is open Then Showing Target Details... ",colors.reset )
                os.system(f"crackmapexec --verbose smb {targets[0]} ") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"When FTP Port is open Then Showing Target Details... ",colors.reset )
                os.system(f"crackmapexec --verbose ftp {targets[0]} ") 
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"When SSH Port is open Then Showing Target Details... ",colors.reset )
                os.system(f"crackmapexec --verbose ssh {targets[0]} ") 
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"When WINRM Port is open Then Showing Target Details... ",colors.reset )
                os.system(f"crackmapexec --verbose winrm {targets[0]} ") 
                continue
            elif option == "5":
                template.load_banner(name)
                print(colors.options,f"When MSSQL Port is open Then Showing Target Details... ",colors.reset )
                os.system(f"crackmapexec --verbose mssql {targets[0]} ") 
                continue
            elif option== "6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option == "8":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def searchsploit(name):
    try:
        template.load_banner(name)
        while True:
            
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["All payloads with json format\t\t (Recommended)","All payload with normal format","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                payload=input("\n\nEnter which type of payload want to find: ")
                targets.append(payload)
                print(colors.options,f"Searching... ",colors.reset )
                os.system(f"searchsploit -c -e -s -t -j | grep {targets[0]}") 
                continue
            elif option == "2":
                template.load_banner(name)
                payload=input("\n\nEnter which type of payload want to find: ")
                targets.append(payload)
                print(colors.options,f"Searching... ",colors.reset )
                os.system(f"searchsploit -c -e -s -t | grep {targets[0]}") 
                continue
            elif option== "3":
                change_target(name)
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option == "5":
                break
            else:
                break
    except KeyboardInterrupt:
        return
def sqlmap(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url with id (like https://example.com?phpid=1) : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Google Dorks with random agent and Output save with advance  \t\t (Recommended)","Gaining a SQL Shell","Running Operating System Commands","Scanning for Vulnerabilities with userfriendly interface","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                savefile = input(f"\n {colors.select}Enter full path Where you want to save(like /home/user/Desktop/result.txt) : {colors.reset}")
                print(colors.options,f"Sqlmap is running...",colors.reset )
                os.system(f"sqlmap -u '{targets[0]}' --batch --level=5 --risk=3 --dbs -g -v 6 --random-agent -o {savefile}") 
                continue
            elif option == "2":
                template.load_banner(name)
                savefile = input(f"\n {colors.select}Enter full path Where you want to save(like /home/user/Desktop/result.txt) : {colors.reset}")
                print(colors.options,f"Sqlmap is running...",colors.reset )
                os.system(f"sqlmap -u '{targets[0]}'  --sql-shell --random-agent -o {savefile}") 
                continue
            elif option == "3":
                template.load_banner(name)
                cmd = input(f"\n {colors.select}Enter Operating System Command want to run(like ls , ls -la) : {colors.reset}")
                print(colors.options,f"Sqlmap is running...",colors.reset )
                os.system(f"sqlmap -u '{targets[0]}' --random-agent --os-shell '{cmd}'") 
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Sqlmap is running...",colors.reset )
                os.system(f"sqlmap -u '{targets[0]}' --random-agent --wizard") 
                continue
            elif option=="5":
                change_target(name)
                continue
            elif option == "6":
                command_line(name)
                continue
            elif option == "7":
                break
            else:
                break
    except KeyboardInterrupt:
        return
####################################  Post Exploitation Tools   #######################################################################
def linpeas(name):
    try:
        template.load_banner(name)
        while True:
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Common misconfigurations and vulnerabilities\t\t (Recommended)","Finding Specific aspect of the system","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Common misconfigurations and vulnerabilities is running... ",colors.reset )
                os.system(f"cd /usr/share/peass/linpeas && ./linpeas.sh –a") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Finding Specific aspect of the system... ",colors.reset )
                os.system(f"cd /usr/share/peass/linpeas && ./linpeas.sh -s suid") 
                continue
            elif option== "3":
                change_target(name)
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option == "5":
                break
            else:
                break
    except KeyboardInterrupt:
        return
    
def linenum(name):
    try:
        template.load_banner(name)
        while True:
            
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Full Scan \t\t (Recommended)","Check for common misconfigurations","Search for specific keywords","Search for SUID/SGID files and binaries","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Full Scans is running... ",colors.reset )
                os.system(f"cd Tools/LinEnum && ./LinEnum.sh -k password") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Check for common misconfigurations... ",colors.reset )
                os.system(f"cd Tools/LinEnum && ./LinEnum.sh -s suid") 
                continue
            elif option == "3":
                template.load_banner(name)
                keyword = input(f"\n {colors.select}Enter a keyword :  {colors.reset}")
                print(colors.options,f"Search for specific keywords... ",colors.reset )
                os.system(f"cd Tools/LinEnum && ./LinEnum.sh -k {keyword} -r report ") 
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Search for SUID/SGID files and binaries... ",colors.reset )
                os.system(f"cd Tools/LinEnum && ./LinEnum.sh -t -k password -r –s") 
                continue
            elif option== "5":
                change_target(name)
                continue
            elif option == "6":
                command_line(name)
                continue
            elif option == "7":
                break
            else:
                break
    except KeyboardInterrupt:
        return
    
def sudo_killer(name):
    try:
        template.load_banner(name)
        while True:
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Simple Scan \t\t (Recommended)","Potential vulnerabilities ","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Simple Scans is running... ",colors.reset )
                os.system(f"cd Tools/SUDO_KILLER && chmod u+x * && ./SUDO_KILLERv2.4.2.sh ") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Potential vulnerabilities... ",colors.reset )
                os.system(f"cd Tools/SUDO_KILLER && chmod u+x * && ./SUDO_KILLERv2.4.2.sh -p ") 
                continue
            
            elif option== "3":
                change_target(name)
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option == "5":
                break
            else:
                break
    except KeyboardInterrupt:
        return
    
def linux_exploit_suggester_2(name):
    try:
        template.load_banner(name)
        while True:
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Simple Scan \t\t (Recommended)","Specify the kernel version ","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Simple Scans is running... ",colors.reset )
                os.system(f"cd Tools/linux-exploit-suggester-2 && ./linux-exploit-suggester-2.pl ") 
                continue
            elif option == "2":
                template.load_banner(name)
                kernel = input(f"\n{colors.select}Enter a kernel version : {colors.reset}")
                print(colors.options,f"Specify the kernel versions... ",colors.reset )
                os.system(f"cd Tools/linux-exploit-suggester-2 && ./linux-exploit-suggester-2.pl -k {kernel}") 
                continue
            
            elif option== "3":
                change_target(name)
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option == "5":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def linux_smart_enumeration(name):
    try:
        template.load_banner(name)
        while True:
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Simple Scan \t\t (Recommended)","Check for dangerous SUID/SGID binaries","Check for writable configuration files","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Simple Scans is running... ",colors.reset )
                os.system(f"cd Tools/linux-smart-enumeration &&./lse.sh ") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Check for dangerous SUID/SGID binaries... ",colors.reset )
                os.system(f"cd Tools/linux-smart-enumeration &&./lse.sh -s") 
                continue
            
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Check for writable configuration files... ",colors.reset )
                os.system(f"cd Tools/linux-smart-enumeration &&./lse.sh -c") 
                continue
            elif option== "4":
                change_target(name)
                continue
            elif option == "5":
                command_line(name)
                continue
            elif option == "6":
                break
            else:
                break
    except KeyboardInterrupt:
        return
def pspy64(name):
    try:
        template.load_banner(name)
        while True:
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Start monitoring processes \t\t (Recommended)","Start monitoring SSH","Monitor specific process","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Start monitoring processes... ",colors.reset )
                os.system(f"cd Tools/PSPY && ./pspy64") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Start monitoring SSH... ",colors.reset )
                os.system(f"cd Tools/PSPY && ./pspy64  | grep -i ssh") 
                continue
            
            elif option == "3":
                template.load_banner(name)
                process = input(f"\n {colors.select}Enter process name for monitor :  {colors.reset}")
                print(colors.options,f"Monitor specific process... ",colors.reset )
                os.system(f"cd Tools/PSPY && ./pspy64  | grep {process}") 
                continue
            elif option== "4":
                change_target(name)
                continue
            elif option == "5":
                command_line(name)
                continue
            elif option == "6":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def upx(name):
    try:
        template.load_banner(name)
        while True:
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Compress an executable file\t\t (Recommended)","Decompress an executable file","Custom compression level","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                file = input(f"\n {colors.select} Enter path of file :  {colors.reset}")
                print(colors.options,f"Compress an executable file... ",colors.reset )
                os.system(f"cd Tools/upx-4.0.1-i386_linux && chmod u+x upx && ./upx -9 {file}") 
                continue
            elif option == "2":
                template.load_banner(name)
                file = input(f"\n {colors.select} Enter path of file :  {colors.reset}")
                print(colors.options,f"Decompress an executable file... ",colors.reset )
                os.system(f"cd Tools/upx-4.0.1-i386_linux && chmod u+x upx && ./upx -d {file}")
                continue
            elif option == "3":
                template.load_banner(name)
                file = input(f"\n {colors.select} Enter path of file :  {colors.reset}")
                print(colors.options,f"Custom compression level... ",colors.reset )
                os.system(f"cd Tools/upx-4.0.1-i386_linux && chmod u+x upx && ./upx -o2 {file}")
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option == "5":
                break
            else:
                break
    except KeyboardInterrupt:
        return


###################################  Anonimity Tools  #######################################################################
def tor(name):
    try:
        template.load_banner(name)
        while True:
            list_tools = ["Tor service Start", "Tor service Stop","Tor Service Status", "Writeups",  "go back"]
            for i in range(len(list_tools)):
                print(colors.options, f"{i+1}) {list_tools[i]}".title(), colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            # while not option:
            #     option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            if option == "1":
                template.load_banner(name)
                print(colors.options, f"Tor Service is Starting...", colors.reset)
                os.system(f"sudo service tor start && proxychains firefox")
                template.load_banner(name)
                print(colors.options, f"Tor Service Status...", colors.reset) 
                os.system(f"sudo service tor status | head -n 3")
                print("\n")
            elif option == "2":
                template.load_banner(name)
                print(colors.options, f"Tor Service is Stop...", colors.reset)
                os.system(f"sudo service tor stop")
                template.load_banner(name)
                print(colors.options, f"Tor Service Status...", colors.reset) 
                print(os.system(f"sudo service tor status | head -n 3\n"))
                print("\n")
            elif option == "3":
                template.load_banner(name)
                print(colors.options, f"Tor Service Status...", colors.reset) 
                os.system(f"sudo service tor status | head -n 3\n")
                print("\n")
            elif option == "4":
                template.load_banner(name)
                print("\n[+] Writeups")
                template.template("Writeups", "no-tools","Writeup to Configure TOR",
                                {
                                    "Configuring TOR with Python": "https://infosecwriteups.com/configuring-tor-with-python-1a90fc1c246f",
                                    
                                })
                                
            else:
                break
    except KeyboardInterrupt:
                return
def anonsurf(name):
    try:
        template.load_banner(name)
        while True:
            list_tools = ["anonsurf service start", "anonsurf service stop","anonsurf service status","anonsurf service myip",  "go back"]
            for i in range(len(list_tools)):
                print(colors.options, f"{i+1}) {list_tools[i]}".title(), colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            if option == "1":
                template.load_banner(name)
                print(colors.options, f"anonsurf Service is Starting...", colors.reset)
                os.system("cd Tools/kali-anonsurf && sudo anonsurf start")
                
                print(colors.options, f"anonsurf Service Status...", colors.reset) 
                os.system("cd Tools/kali-anonsurf &&  sudo anonsurf status")
                print("\n")
            elif option == "2":
                template.load_banner(name)
                print(colors.options, f"anonsurf Service is Stop...", colors.reset)
                os.system("cd Tools/kali-anonsurf && sudo anonsurf stop")
                
                print(colors.options, f"anonsurf Service Status...", colors.reset) 
                os.system("cd Tools/kali-anonsurf &&  sudo anonsurf status")
                print("\n")
            elif option == "3":
                template.load_banner(name)
                print(colors.options, f"anonsurf Service Status...", colors.reset) 
                os.system("cd Tools/kali-anonsurf &&  sudo anonsurf status")
                print("\n")
            elif option == "4":
                template.load_banner(name)
                print(colors.options, f"anonsurf Service Status...", colors.reset) 
                os.system("cd Tools/kali-anonsurf &&  sudo anonsurf myip")
                print("\n")    
                  
            else:
                break
    except KeyboardInterrupt:
                return                
def nipe(name):
    try:
        template.load_banner(name)
        while True:
            list_tools = ["Nipe service Start", "Nipe service Stop","Nipe Service Status",  "go back"]
            for i in range(len(list_tools)):
                print(colors.options, f"{i+1}) {list_tools[i]}".title(), colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            if option == "1":
                template.load_banner(name)
                print(colors.options, f"Nipe Service is Starting...", colors.reset)
                os.system("cd Tools/nipe && sudo perl nipe.pl start")
                
                print(colors.options, f"Nipe Service Status...", colors.reset) 
                os.system("cd Tools/nipe &&  sudo perl nipe.pl status")
                print("\n")
            elif option == "2":
                template.load_banner(name)
                print(colors.options, f"Nipe Service is Stop...", colors.reset)
                os.system("cd Tools/nipe && sudo perl nipe.pl stop")
                
                print(colors.options, f"Nipe Service Status...", colors.reset) 
                os.system("cd Tools/nipe &&  sudo perl nipe.pl status")
                print("\n")
            elif option == "3":
                template.load_banner(name)
                print(colors.options, f"Nipe Service Status...", colors.reset) 
                os.system("cd Tools/nipe &&  sudo perl nipe.pl status")
                print("\n")
                  
            else:
                break
    except KeyboardInterrupt:
                return
    
###################################  Pentesting And Bug Bounty #######################################################################
###################################  configuration management #######################################################################

def gobuster(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["DNS Enumeration with gobuster advance search \t\t (Recommended)","Basic scan","Advance slash + dir","Discover backup","set threat with advance result","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                threads=input("\n\nEnter How many threads you want to Run : ")
                wordlist=input("Enter Full Path of Wordlist: ")
                print(colors.options,f"Gobuster is running...",colors.reset )
                os.system(f"gobuster dns -d {targets[0]} -r -c -i -t {threads} --wildcard --debug -w {wordlist}")
                continue
            elif option == "2":
                template.load_banner(name)
                word=input("Enter Full Path of Wordlist: ")
                targets.append(word)
                print(colors.options,f"Gobuster is running...",colors.reset)
                os.system(f"gobuster dir -u {targets[0]} -w {targets[1]}")
                continue
            elif option == "3":
                template.load_banner(name)
                word=input("Enter Full Path of Wordlist: ")
                targets.append(word)
                print(colors.options,f"Gobuster is running...",colors.reset )
                os.system(f"gobuster dir -f -u {targets[0]} -w {targets[1]}")
                continue
            elif option == "4":
                template.load_banner(name)
                word=input("Enter Full Path of Wordlist: ")
                targets.append(word)
                print(colors.options,f"Gobuster is running...",colors.reset )
                os.system(f"gobuster dir -f -d -u {targets[0]} -w {targets[1]}")
                continue
            elif option == "5":
                template.load_banner(name)
                thread=input("Enter How many threads you want to run: ")
                targets.append(thread)
                word=input("Enter Full Path of Wordlist: ")
                targets.append(word)
                out=input("Enter where you want to save output: ")
                targets.append(out)
                print(colors.options,f"Gobuster is running...",colors.reset )
                os.system(f"gobuster dir -f -d -e -r -n -k -z -v -u {targets[0]} -t {targets[1]} -w {targets[2]} -o {targets[3]}")
                continue
            elif option=="6":
                change_target(name)
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option == "8":
                break
            else:
                break
    except KeyboardInterrupt:
        return
    
def httpie(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0]} {colors.reset}")
           # print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["json format scan \t\t (Recommended)","Debug Scan","Basic Scan","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Httpie is scanning...",colors.reset )
                os.system(f"http --follow  {targets[0]} 'Accept: application/json'") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Httpie is scanning...",colors.reset )
                os.system(f"http --debug --traceback '{targets[0]}'") 
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Httpie is scanning...",colors.reset )
                os.system(f"http --follow '{targets[0]}'") 
                continue
            elif option== "4":
                change_target(name)
                continue
            elif option == "5":
                command_line(name)
                continue
            elif option == "6":
                break
            else:
                break
    except KeyboardInterrupt:
        return


def feroxbuster(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    template.load_banner(name)
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0]} {colors.reset}")
           # print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Fast thread and Depth result with recursion \t\t (Recommended)","Random Agent scan","Enable Follow Redirects","Disable TLS Verification","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                wordlist = input("Enter Full path of wordlist : ")
                threads = input("Enter How many threads you want to run : ")
                print(colors.options,f"Feroxbuster is running...",colors.reset )
                os.system(f"feroxbuster -u {targets[0]} -w {wordlist} -t {threads} --force-recursion -v") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Feroxbuster is running...",colors.reset )
                os.system(f"feroxbuster -u {targets[0]} --random-agent -v") 
                continue
            elif option == "3":
                template.load_banner(name)
                word =  input("Enter Full path of wordlist : ")
                print(colors.options,f"Feroxbuster is running...",colors.reset )
                os.system(f"feroxbuster -u {targets[0]} -w {word} -r") 
                continue
            elif option == "4":
                template.load_banner(name)
                word =  input("Enter Full path of wordlist : ")
                print(colors.options,f"Feroxbuster is running...",colors.reset )
                os.system(f"feroxbuster -u {targets[0]} -w {word} --insecure") 
                continue
            elif option== "5":
                change_target(name)
                continue
            elif option == "6":
                command_line(name)
                continue
            elif option == "7":
                break
            else:
                break
    except KeyboardInterrupt:
        return
            

def secretfinder(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url like https://example.com: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Multiple Urls \t\t (Recommended)","Single url","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                file = input(f"\n {colors.select} Enter path of url file :  {colors.reset}")
                print(colors.options,f"Multiple Urls Scanning... ",colors.reset )
                os.system(f"cd Tools/SecretFinder && cat {file} | while read url; do python3 SecretFinder.py -i $url -o cli >> result.txt; done") 
                path = template.check_path("SecretFinder")
                print(f"\nOutput saved to {path}/result.txt")
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Single url is scanning... ",colors.reset )
                os.system(f"cd Tools/SecretFinder &&  python3 SecretFinder.py -i {targets[0]} -o cli >> result.txt")
                path = template.check_path("SecretFinder")
                print(f"\nOutput saved to {path}/result.txt")
                continue
            elif option== "3":
                change_target(name)
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option == "5":
                break
            else:
                break
    except KeyboardInterrupt:
        return

###################################  Data validation #######################################################################

def xsstrike(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Scan with All file log techniques \t\t (Recommended)","Scan with Url Fuzzing","Scan with All console log techniques","Basic Scan with crawling","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"xsstrike is running...",colors.reset )
                os.system(f"cd Tools/XSStrike && python3 xsstrike.py -u '{targets[0]}' --crawl --console-log-level DEBUG --console-log-level INFO --console-log-level RUN --console-log-level GOOD --console-log-level WARNING --console-log-level ERROR --console-log-level CRITICAL --console-log-level VULN --delay 2") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"xsstrike is running...",colors.reset )
                os.system(f"cd Tools/XSStrike && python3 xsstrike.py -u '{targets[0]}' --fuzzer --delay 5") 
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"xsstrike is running...",colors.reset )
                os.system(f"cd Tools/XSStrike && python3 xsstrike.py -u '{targets[0]}' --crawl --file-log-level DEBUG --file-log-level INFO --file-log-level RUN --file-log-level GOOD --file-log-level WARNING --file-log-level ERROR --file-log-level CRITICAL --file-log-level VULN --delay 2") 
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"xsstrike is running...",colors.reset )
                os.system(f"cd Tools/XSStrike && python3 xsstrike.py -u '{targets[0]}' --crawl --level 3") 
            elif option=="5":
                change_target(name)
                continue
            elif option == "6":
                command_line(name)
                continue
            elif option == "7":
                break
            else:
                break
    except KeyboardInterrupt:
        return


def dalfox(name):
    try:
        template.load_banner(name)
        s.system("dalfox -h") 
        while True:
            list_attacks=["Command Line","Open this for Best Commands(link to website)","Output handling(link to website)","Parameter Analysis and XSS Scanning(link to website)","Scanning single url's(link to website)","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}){list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                command_line(name)
                continue
            elif option == "2":
                run_on_browser.main("https://www.blackhatethicalhacking.com/tools/dalfox/")
                template.load_banner(name)
            elif option == "3":
                run_on_browser.main("https://dalfox.hahwul.com/docs/output-handling/")
                template.load_banner(name)
            elif option == "4":
                run_on_browser.main("https://geekscripts.guru/dalfox-parameter-analysis-xss-scanning/")
                template.load_banner(name)
            elif option == "5":
                run_on_browser.main("https://dalfox.hahwul.com/docs/scan-single-url/")
                template.load_banner(name)
            elif option == "3":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def oralyzer(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0]} {colors.reset}")
           # print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Advance Scan \t\t (Recommended)","Basic Scan","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Oralyzer is running...",colors.reset )
                os.system(f"python3 oralyzer.py -u {targets[0]} -crlf") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Oralyzer is running...",colors.reset )
                os.system(f"python3 oralyzer.py -u {targets[0]}") 
                continue
            elif option== "3":
                change_target(name)
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option == "5":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def openredirex(name):
    try:
        
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url like https://example.com: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Multiple Urls \t\t (Recommended)","Single url","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                file = input(f"\n {colors.select} Enter path of url file :  {colors.reset}")
                print(colors.options,f"Multiple Urls Scanning... ",colors.reset )
                os.system(f"cd Tools/OpenRedireX && cat {file} |  cat {file}=FUZZ | python3 openredirex.py  -p payloads.txt  --keyword FUZZ  --concurrency 100") 
                path = template.check_path("OpenRedireX")
                print(f"\nOutput saved to {path}/result.txt")
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Single url is scanning... ",colors.reset )
                os.system(f"cd Tools/OpenRedireX &&  echo {targets[0]}=FUZZ | python3 openredirex.py  -p payloads.txt  --keyword FUZZ  --concurrency 100")
                path = template.check_path("OpenRedireX")
                print(f"\nOutput saved to {path}/result.txt")
                continue
            elif option== "3":
                change_target(name)
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option == "5":
                break
            else:
                break
    except KeyboardInterrupt:
        return



def dalfox(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                os.system("dalfox -h") 
            list_attacks=["Command Line","Open this for Best Commands(link to website)","Output handling(link to website)","Parameter Analysis and XSS Scanning(link to website)","Scanning single url's(link to website)","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}){list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                command_line(name)
                continue
            elif option == "2":
                run_on_browser.main("https://www.blackhatethicalhacking.com/tools/dalfox/")
            elif option == "3":
                run_on_browser.main("https://dalfox.hahwul.com/docs/output-handling/")
            elif option == "4":
                run_on_browser.main("https://geekscripts.guru/dalfox-parameter-analysis-xss-scanning/")
            elif option == "5":
                run_on_browser.main("https://dalfox.hahwul.com/docs/scan-single-url/")
            elif option == "3":
                break
            else:
                break
    except KeyboardInterrupt:
        return
##################################  DOS ATTACK  #######################################################################

def slowloris(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target Host (like facebook.com , google.com {colors.red}'Not use http://'): {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0]} {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Attack with random user agent with custom sleeptime \t\t (Recommended)",
            	"Attack with proxy and sleeptime",
            	"Basic Attack",
            	"Using https Attacks",
            	"Change Target",
            	"Command Line",
            	"exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                sleeptime = input("\nEnter how much sleeptime between requests (like 60): ")
                port = input("\nEnter the port number: ")
                socket  = input("\nEnter how many socket you want to add  (like 600): ")
                print(colors.options,f"Slowloris is running...",colors.reset )
                os.system(f"cd Tools/slowloris && python3 slowloris.py {targets[0]} -s {socket} -p {port} -v -ua --sleeptime {sleeptime}") 
                continue
            elif option == "2":
                template.load_banner(name)
                sleeptime = input("\nEnter how much sleeptime between requests (like 60): ")
                port = input("\nEnter the port number: ")
                socket  = input("\nEnter how many socket you want to add  (like 600): ")
                proxyhost = input("\nEnter proxy IP: ")
                proxyport = input("\nEnter proxy port number: ")
                print(colors.options,f"Slowloris is running...",colors.reset )
                os.system(f"cd Tools/slowloris && python3 slowloris.py {targets[0]} -s {socket} -p {port} -v --proxy-host {proxyhost} --proxy-port {proxyport} --sleeptime {sleeptime}") 
                continue
            elif option == "3":
                template.load_banner(name)
                port = input("\nEnter the port number: ")
                socket  = input("\nEnter how many socket you want to add  (like 600): ")
                print(colors.options,f"Slowloris is running...",colors.reset )
                os.system(f"cd Tools/slowloris && python3 slowloris.py {targets[0]} -s {socket} -p {port} -ua") 
                continue
            elif option == "4":
                template.load_banner(name)
                port = input("\nEnter the port number: ")
                socket  = input("\nEnter how many socket you want to add  (like 600): ")
                print(colors.options,f"Slowloris is running...",colors.reset )
                os.system(f"cd Tools/slowloris && python3 slowloris.py {targets[0]} --https -s {socket} -p {port} -ua") 
                continue
            elif option== "5":
                change_target(name)
                continue
            elif option == "6":
                command_line(name)
                continue
            elif option == "7":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def goldeneye(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0]} {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["debug mode and no sslcheck with specific method \t\t (Recommended)","Basic scan"," disable SSL certificate verification","With any method","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                method = input("\nEnter the method(like get or post or random): ")
                worker = input("\nEnter how many worker you want to add (like 60): ")
                socket  = input("\nEnter how many socket you want to add  (like 600): ")
                print(colors.options,f"goldeneye is running...",colors.reset )
                os.system(f"goldeneye {targets[0]} -d -m {method} -w {worker} -s {socket} -n") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"goldeneye is running...",colors.reset )
                os.system(f"goldeneye {targets[0]} -d -m ") 
                continue
            elif option == "3":
                template.load_banner(name)
                worker = input("\nEnter how many worker you want to add (like 60): ")
                socket  = input("\nEnter how many socket you want to add  (like 600): ")
                print(colors.options,f"goldeneye is running...",colors.reset )
                os.system(f"goldeneye {targets[0]} -d -n -w {worker} -s {socket}") 
                continue
            elif option == "4":
                template.load_banner(name)
                method = input("\nEnter the method(like get or post or random): ")
                worker = input("\nEnter how many worker you want to add (like 60): ")
                socket  = input("\nEnter how many socket you want to add  (like 600): ")
                print(colors.options,f"goldeneye is running...",colors.reset )
                os.system(f"goldeneye {targets[0]} -d -m {method} -w {worker} -s {socket}") 
                continue
            elif option== "5":
                change_target(name)
                continue
            elif option == "6":
                command_line(name)
                continue
            elif option == "7":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def thcssldos(name):
    try:
        template.load_banner(name)
        while True:  # Infinite loop until explicitly broken 
            if not targets:
                target = input(f"\n{colors.select}Enter an IP : {colors.reset}")
                if not target:
                    continue  # If target is empty, restart the loop
                valid = ip_valid(target)
                if valid == 2:
                    template.load_banner(name)
                    print(f"\n{colors.red}Please enter a valid IP. {colors.reset}")  
                    continue  # If the IP is invalid, restart the loop
                targets.append(target)

            print(colors.options, f"\nDomain: {targets[0]}", colors.reset)
            print(f"\n{colors.select}Select an option:", colors.reset)
            list_attacks = [
                "Complete scan \t\t (Recommended)",
                "Change Target",
                "Command Line",
                "Exit"
            ]
            for i, attack in enumerate(list_attacks, 1):
                print(colors.options, f"{i}) {attack.title()}", colors.reset)

            option = input(f"\n{colors.select}Select an option: {colors.reset}")

              # If option is empty, restart the loop

            if option == "1":
                port = int(input("\nEnter the Port Number: "))
                print(colors.options, "Thc-ssl-dos is running...", colors.reset)
                os.system(f"thc-ssl-dos -–accept {targets[0]} {port}")
            elif option == "2":
                change_target(name)	
                continue  # Placeholder for change_target function
            elif option == "3":
                command_line(name)
                continue  # Placeholder for command_line function
            elif option == "4":
                break  # Exit the loop and function
            else:
                break

    except KeyboardInterrupt:
        return


def slowhttptest(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Advanced command with configuration on connection interval with debugging \t\t (Recommended)","Aggresive Post attack","Basic Scan with Random Slow Headers and Body","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                connections = input(f"\n {colors.select}Enter how much target number of connections(like 90) : {colors.reset}")
                interval = input(f"\n {colors.select}Enter how much interval between followup data in seconds(like 20) : {colors.reset}")
                rate = input(f"\n {colors.select}Enter how much Connections per seconds (like 60) : {colors.reset}")
                print(colors.options,f"Slowhttptest is running...",colors.reset )
                os.system(f"slowhttptest -c {connections} -B -g  -i {interval} -r {rate} -s 8192 -t GET -u {targets[0]} -v 4") 
                continue
            elif option == "2":
                template.load_banner(name)
                connections = input(f"\n {colors.select}Enter how much target number of connections(like 90) : {colors.reset}")
                interval = input(f"\n {colors.select}Enter how much interval between followup data in seconds(like 20) : {colors.reset}")
                rate = input(f"\n {colors.select}Enter how much Connections per seconds (like 60) : {colors.reset}")
                print(colors.options,f"Slowhttptest is running...",colors.reset )
                os.system(f"slowhttptest -c {connections} -B -i {interval} -r {rate} -s 8192 -t POST -x 10 -y 20 -u {targets[0]}") 
                continue
            elif option == "3":
                template.load_banner(name)
                connections = input(f"\n {colors.select}Enter how much target number of connections(like 90) : {colors.reset}")
                interval = input(f"\n {colors.select}Enter how much interval between followup data in seconds(like 20) : {colors.reset}")
                rate = input(f"\n {colors.select}Enter how much Connections per seconds (like 60) : {colors.reset}")
                print(colors.options,f"Slowhttptest is running...",colors.reset )
                os.system(f"slowhttptest -c {connections} -H -i {interval} -r {rate} -s 8192 -t GET -u {targets[0]} -v 4") 
                continue
            elif option=="4":
                change_target(name)
                continue
            elif option == "5":
                command_line(name)
                continue
            elif option == "6":
                break
            else:
                break
    except KeyboardInterrupt:
        return

###################################  Cryptography #######################################################################
def sslyze(name):
    try:
        template.load_banner(name)
        while True:
            
            if not targets:
                target = input(f"\n{colors.select}Enter Target url: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0]} {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Advance scanning with plugins \t\t (Recommended)","Basic Scan","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Sslyze is scanning...",colors.reset )
                os.system(f"sslyze {targets[0]} --fallback --tlsv1 --sslv2 --elliptic_curves --http_headers --tlsv1_2 --robot --sslv3 --heartbleed --tlsv1_3 --openssl_ccs --reneg --early_data --certinfo") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Sslyze is scanning...",colors.reset )
                os.system(f"sslyze {targets[0]}") 
                continue
            elif option== "3":
                change_target(name)
                continue
            elif option == "4":
                command_line(name)
                continue
            elif option == "5":
                break
            else:
                break
    except KeyboardInterrupt:
        return

def sslscan(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Detailed TLS Version and Cipher Suite Analysis \t\t (Recommended)","Basic SSL/TLS Scan with Certificate Information","Comprehensive TLS Version and Cipher Suite Analysis","Detection of SSL/TLS Implementation Bugs","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Detailed TLS Version and Cipher Suite Analysis... ",colors.reset )
                os.system(f"sslscan --show-ciphers --show-certificate --xml=output/scan_results.xml --verbose {targets[0]}") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/scan_results.xml \n")
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Basic SSL/TLS Scan with Certificate Information... ",colors.reset )
                os.system(f"sslscan --show-certificate --no-check-certificate {targets[0]}")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Comprehensive TLS Version and Cipher Suite Analysis...",colors.reset )
                os.system(f"sslscan --show-ciphers --tlsall {targets[0]}")
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Detection of SSL/TLS Implementation Bugs",colors.reset )
                os.system(f"sslscan --bugs {targets[0]}")
                continue
            elif option== "5":
                change_target(name)
                continue
            elif option == "6":
                command_line(name)
                continue
            elif option == "7":
                break
            else:
                break
    except KeyboardInterrupt:
        return   

def o_saft(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Supported (enabled) ciphers \t\t (Recommended)","HTTP response header","Certificate, Ciphers, and SSL connection","Check vulnerabilities","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Supported (enabled) ciphers ... ",colors.reset )
                os.system(f"o-saft +cipher --enabled {targets[0]}") 
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"HTTP response header... ",colors.reset )
                os.system(f"o-saft +info --v --header  {targets[0]}")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Certificate, Ciphers, and SSL connection...",colors.reset )
                os.system(f"o-saft +check --ignore-no-conn --ignore-no-cert {targets[0]}")
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Check vulnerabilities...",colors.reset )
                os.system(f"o-saft +vulns --trace --experimental {targets[0]}")
                continue
            elif option== "5":
                change_target(name)
                continue
            elif option == "6":
                command_line(name)
                continue
            elif option == "7":
                break
            else:
                break
    except KeyboardInterrupt:
        return      

###################################  File Upload  #######################################################################
def fuxploider(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url like http://example.com: {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Basic Scan \t\t (Recommended)","Comprehensive Scan","Advanced Scan with Proxy and Cookies","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Basic Scan is running... ",colors.reset )
                os.system(f"cd Tools/fuxploider && python3 fuxploider.py --not-regex \"error\" -v -u {targets[0]}") 
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Comprehensive Scan... ",colors.reset )
                os.system(f"cd Tools/fuxploider && python3 fuxploider.py -v -t nastygif -f 100 -u {targets[0]} --not-regex \"error\"")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Advanced Scan with Proxy and Cookies...",colors.reset )
                os.system(f"cd Tools/fuxploider && python3 fuxploider.py --cookies \"PHPSESSID=aef45aef45afeaef45aef45&JSESSID=AQSEJHQSQSG\" --not-regex \"error\" -u {targets[0]} -v ")
                continue
            elif option== "4":
                change_target(name)
                continue
            elif option == "5":
                command_line(name)
                continue
            elif option == "6":
                break
            else:
                break
    except KeyboardInterrupt:
        return
    

###################################  NEW Bug BOUNTY SECITON #######################################################################
###################################  Exploitation #######################################################################


def masscan(name):
    try:
        template.load_banner(name)
        while True:  # Infinite loop until explicitly broken 
            if not targets:
                target = input(f"\n{colors.select}Enter an IP : {colors.reset}")
                if not target:
                    continue  # If target is empty, restart the loop
                valid = ip_valid(target)
                if valid == 2:
                    template.load_banner(name)
                    print(f"\n{colors.red}Please enter a valid IP. {colors.reset}")  
                    continue  # If the IP is invalid, restart the loop
                targets.append(target)

            print(colors.options, f"\nDomain: {targets[0]}", colors.reset)
            print(f"\n{colors.select}Select an option:", colors.reset)
            list_attacks = [
                "Advanced scan \t\t (Recommended)",
                "Complete scanning ",
                "Basic Scan",
                "Change Target",
                "Command Line",
                "Exit"
            ]
            for i, attack in enumerate(list_attacks, 1):
                print(colors.options, f"{i}) {attack.title()}", colors.reset)

            option = input(f"\n{colors.select}Select an option: {colors.reset}")

              # If option is empty, restart the loop
            if option == "1":
                template.load_banner(name)
                port = int(input("\nEnter the Port Number: "))
                Range = input("\nEnter the range(like 8000-8100) : ")
                print(colors.options, "Masscan is running...", colors.reset)
                os.system(f"masscan -p {port},{Range} {targets[0]} --rate=10000")
            elif option == "2":
                template.load_banner(name)
                port = int(input("\nEnter the Port Number: "))
                Range = input("\nEnter the range(like 8000-8100) : ")
                print(colors.options, "Masscan is running...", colors.reset)
                os.system(f"masscan -p {port},{Range} {targets[0]} --rate=10000 --banners --open")
            elif option == "3":
                template.load_banner(name)
                port = int(input("\nEnter the Port Number: "))
                Range = input("\nEnter the range(like 8000-8100) : ")
                print(colors.options, "Masscan is running...", colors.reset)
                os.system(f"masscan -p {port},{Range} {targets[0]}")            
            elif option == "4":
                template.load_banner(name)
                change_target(name)
                continue  # Placeholder for change_target function
            elif option == "5":
                command_line(name)
                continue  # Placeholder for command_line function
            elif option == "6":
                break  # Exit the loop and function
            else:
                break

    except KeyboardInterrupt:
        return
            

def unicornscan(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Basic TCP SYN Scan \t\t (Recommended)","UDP Scan","TCP Scan all ports","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Basic TCP SYN Scanning... \n",colors.reset )
                os.system(f"unicornscan -msf -v -r 1000 {targets[0]}:a ") 
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"UDP Scanning... \n",colors.reset )
                os.system(f" unicornscan -mU -v -I -r 500 {targets[0]}:53  ")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"TCP Scanning all ports...\n",colors.reset )
                os.system(f"unicornscan -mT -v -r 1000 -mTsFpU -W 6 {targets[0]}.com:a ")
                continue
            elif option== "4":
                change_target(name)
                continue
            elif option == "5":
                command_line(name)
                continue
            elif option == "6":
                break
            else:
                break
    except KeyboardInterrupt:
        return      
def dnsrecon(name):
    try:
        template.load_banner(name)
        while True:
            if not targets:
                target = input(f"\n{colors.select}Enter Target url : {colors.reset}")
                if not target:
                    continue
                targets.append(target)
            print (colors.options,f"\nDomain : {targets[0] } {colors.reset}")
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Bruteforce subdomains \t\t (Recommended)","Enumeration Subdomain","Domain bruteforce enumeration","Reverse Lookup","Change Target","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                file = input(f"{colors.select}Enter Bruteforce list file path : ")
                print(colors.options,f"Bruteforcing subdomains... \n",colors.reset )
                os.system(f"dnsrecon -d {targets[0]} -D {file}") 
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Enumeration Subdomain... \n",colors.reset )
                os.system(f"dnsrecon -d {targets[0]} -b -k -y --type bing,yand,crt ")
                continue
            elif option == "3":
                template.load_banner(name)
                file = input(f"{colors.select}Enter Bruteforce list file path : ")
                print(colors.options,f"Domain bruteforce enumeration...\n",colors.reset )
                os.system(f"dnsrecon -d {targets[0]} -D {file}")
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Reverse Lookup...\n",colors.reset )
                os.system(f"dnsrecon -d {targets[0]} -s")
                continue
            elif option== "5":
                change_target(name)
                continue
            elif option == "6":
                command_line(name)
                continue
            elif option == "7":
                break
            else:
                break
    except KeyboardInterrupt:
        return 
###################################  Reporting Tools #######################################################################    
    
def recordmydesktop(name):
    try:
        template.load_banner(name)
        while True:
            list_attacks=["Normal Recording \t\t (Recommended)","Quick recording","Advance recording","Full shot","Set buffer size","Full Advanced frame recording","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                print(colors.options,f"Normal Recording ... \n",colors.reset )
                os.system(f"cd output && recordmydesktop -o record.ogv") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/record.ogv \n")
                continue
            elif option == "2":
                template.load_banner(name)
                print(colors.options,f"Quick recording... \n",colors.reset )
                os.system(f"cd output && recordmydesktop --quick-subsampling -o record.ogv")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/record.ogv \n")
                continue
            elif option == "3":
                template.load_banner(name)
                print(colors.options,f"Advance recording...\n",colors.reset )
                os.system(f"cd output && recordmydesktop --quick-subsampling --no-cursor --full-shots --follow-mouse -o record.ogv")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/record.ogv \n")
                continue
            elif option == "4":
                template.load_banner(name)
                print(colors.options,f"Full shot...\n",colors.reset )
                os.system(f"cd output && recordmydesktop --full-shots -o record.ogv")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/record.ogv \n")
                continue
            elif option == "5":
                template.load_banner(name)
                buffer = input(f"{colors.select}Enter the buffer size : {colors.reset}")
                print(colors.options,f"Recording with Set buffer size...\n",colors.reset )
                os.system(f"cd output && recordmydesktop --buffer-size={buffer} -o record.ogv")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/record.ogv \n")
                continue
            elif option == "6":
                template.load_banner(name)
                print(colors.options,f"Full Advanced frame recording...\n",colors.reset )
                os.system(f"cd output && recordmydesktop --ring-buffer-size=10000 --buffer-size=100 --freq=1000 --v_quality=63 --v_bitrate=200000000 --s_quality=1 -o record.ogv")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/record.ogv \n")
                continue
            elif option == "7":
                command_line(name)
                continue
            elif option == "8":
                break
            else:
                break
    except KeyboardInterrupt:
        return  
def pipal(name):
    try:
        template.load_banner(name)
        while True:
            list_attacks=["Analyze wordlist\t\t (Recommended)","Command Line","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                wordlist = input(f"{colors.select}Enter your wordlist file path : {colors.reset}")
                print(colors.options,f"Analyzing wordlist ... \n",colors.reset )
                os.system(f"pipal {wordlist}") 
                continue
            elif option == "2":
                command_line(name)
                continue
            elif option == "3":
                break
            else:
                break
    except KeyboardInterrupt:
        return 

###################################  Digital Forensic Tools #######################################################################    
def autopsy():
    import subprocess
    autopsy_process = subprocess.Popen(["autopsy"])
    print("Autopsy is started at address:http://localhost:9999/autopsy")
    run_on_browser.main("http://localhost:9999/autopsy")

def hashdeep(name):
    try:
        template.load_banner(name)
        while True:
            print (f"\n{colors.select} Select a option -> {colors.reset}")
            list_attacks=["Verify Hashes from a Hash File Against Files in a Directory",
                          "Generate Hashes for Files in a Directory",
                          "Create a Manifest File with Hashes and Filenames",
                          "Compute Hash Values for Files in a Directory Recursively",
                          "Compute and Compare Hashes for Multiple Algorithms",
                          "Command Line",
                          "exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                template.load_banner(name)
                hashfile = input(f"\n {colors.select} Enter the hashfile path :  {colors.reset}")
                directory = input(f"\n {colors.select}Enter the path of directory's file location (like /home/user/Desktop/target.txt) : {colors.reset}")
                template.load_banner(name)
                print(colors.options,f"Hashdeep is running... ",colors.reset )
                os.system(f"cd output && hashdeep -k {hashfile} -r -vv -v -e {directory} > hashdeep")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/hashdeep \n")
                continue 
            elif option == "2":
                template.load_banner(name)
                directory = input(f"\n {colors.select}Enter the path of directory's file location (like /home/user/Desktop/target.txt) : {colors.reset}")
                template.load_banner(name)
                print(colors.options,f"Hashdeep is running... ",colors.reset )
                os.system(f"hashdeep -r -l -c md5,sha256 -o e -j 8 {directory} > hashdeep") 
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/hashdeep \n")
                continue 
            elif option == "3":
                template.load_banner(name)
                directory = input(f"\n {colors.select}Enter the path of directory's file location (like /home/user/Desktop/target.txt) : {colors.reset}")
                template.load_banner(name)
                print(colors.options,f"Hashdeep is running... ",colors.reset )
                os.system(f"hashdeep -r -l -c sha256 -o f -j 8 {directory} > hashdeep")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/hashdeep \n")
                continue 
            elif option == "4":
                template.load_banner(name)
                directory = input(f"\n {colors.select}Enter the path of directory's file location (like /home/user/Desktop/target.txt) : {colors.reset}")
                template.load_banner(name)
                print(colors.options,f"Hashdeep is running... ",colors.reset )
                os.system(f"hashdeep -r -c md5,sha256,sha512 -o f -l -j 8 {directory} > hashdeep")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/hashdeep \n")
                continue 
            elif option == "5":
                template.load_banner(name)
                directory = input(f"\n {colors.select}Enter the path of directory's file location (like /home/user/Desktop/target.txt) : {colors.reset}")
                template.load_banner(name)
                print(colors.options,f"Hashdeep is running... ",colors.reset )
                os.system(f"hashdeep -r -c sha256,md5,sha1 -l -o f {directory} > hashdeep")
                path = template.check_path("Cyberonix")
                print(f"\nOutput saved to {path}/output/hashdeep \n")
                continue 
            elif option == "6":
                command_line(name)
                continue
            elif option == "7":
                break
            else:
                break
    except KeyboardInterrupt:
        return


def bulk_extractor(name):
    try:
        template.load_banner(name)
        os.system("bulk_extractor -h")
        while True:
                 
            list_attacks=["Command Line","Bulk-Extractor -- Extract Everything From Drives(link to website)","Open this for Best Commands(link to website)","Digital Forensics with Bulk Extractor(link to website)","Bulk Extractor with Record Carving(link to website)","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                command_line(name)
                continue
            elif option == "2":
                run_on_browser.main("https://www.kalilinux.in/2020/01/bulk-extractor-kali-linux-forensics.html")
                template.load_banner(name)
            elif option == "3":
                run_on_browser.main("https://www.oreilly.com/library/view/digital-forensics-with/9781788625005/576053c4-24b9-42d5-a822-d44dbe05647c.xhtml")
                template.load_banner(name)
            elif option == "4":
                run_on_browser.main("https://youtu.be/-rf6-AOz-W8?si=4BC3wIx3IPYN3aZ9")
                template.load_banner(name)
            elif option == "5":
                run_on_browser.main("https://www.kazamiya.net/en/bulk_extractor-rec")
                template.load_banner(name)
            elif option == "6":
                break
            else:
                break
    except KeyboardInterrupt:
        return


def binwalk(name):
    try:
        template.load_banner(name)
        os.system("binwalk -h")
        while True:   
            list_attacks=["Command Line","Binwalk Tips & Commands(link to website)","binwalk Command Examples(link to website)","Firmware Analysis Tool Binwalk(link to website)","Open this for Best Commands(link to website)","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}){list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select a option -> {colors.reset}")
            
            if option == "1":
                command_line(name)
                continue
            elif option == "2":
                run_on_browser.main("https://linuxcommandlibrary.com/man/binwalk")
                template.load_banner(name)
            elif option == "3":
                run_on_browser.main("https://www.thegeekdiary.com/binwalk-command-examples-in-linux/")
                template.load_banner(name)
            elif option == "4":
                run_on_browser.main("https://allabouttesting.org/short-tutorial-firmware-analysis-tool-binwalk/#1-scan-to-identify-code-files-and-other-information")
                template.load_banner(name)
            elif option == "5":
                run_on_browser.main("https://github.com/ReFirmLabs/binwalk/wiki/Usage")
                template.load_banner(name)
            elif option == "6":
                break   
            else:
                break
    except KeyboardInterrupt:
        return
