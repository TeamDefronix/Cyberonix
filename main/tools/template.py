from main.tools import banner, waiting, writeup, colors, run_on_browser, Recommended_Tool
import os
import subprocess
import threading


class template:
    def __init__(
        self,
        name,
        command,
        discription,
        writeups,
        link="",
        method="kali",
        github_install="",
        github_check="",
    ):
        self.name = name
        self.command = command
        self.method = method
        self.discription = discription
        self.writeup = writeups
        self.link = link
        self.github_install = github_install
        self.github_check = github_check
        
        while True:
            os.system("clear")
            banner.main()
            banner.attack(self.name)
            if command!="no-tools":
                banner.description(self.discription)
            else:
                writeup.writeup(self.writeup,self.name)
                break
            ask = tool_writeups(self.name,self.writeup, self.command)
            if ask == "1":
                if self.command == "no-tools":
                    break
                else:
                    if method == "kali":
                        check_installed(self.name, self.command)
                        waiting.waiting()
                    elif method == "go":
                        which_check(self.name, self.link, self.command)
                        waiting.waiting()
                    elif method == "pip":
                        pip_install(self.name, self.command)
                        waiting.waiting()

                    elif method == "deb":
                        deb_install(self.name, self.command, self.link)
                    elif method == "browser":
                        threading.Thread(
                            target=run_on_browser.main,
                            args=(self.command,)
                        ).start()
                    elif method == "github":
                        if not os.path.isdir("Tools"):
                            os.system("mkdir Tools")
                        if os.path.exists(f"Tools/{self.github_check}"):
                            print(f"{colors.green}[+] Installed")
                            run = input(
                                f"{colors.blue}[+] Do You Want To Run?(y/n):{colors.reset}"
                            )
                            if run.lower() == "yes" or run.lower() == "y":
                               
                                #os.system(f"cd Tools/{self.github_check} && {self.command}")
                                Recommended_Tool.recommended(name=name)
                                
                        else:
                            print(f"{colors.red}[-] Not Installed{colors.reset}")
                            installed = input(
                                f"{colors.blue}Do You Want To Install The Tool?(y/n):{colors.reset}"
                            )
                            if installed.lower() == "y" or installed.lower() == "yes":
                                os.system(f"cd Tools && {self.github_install}")
                                path = check_path(self.github_check)
                                print(f"\nInstalled folder path : {path}")
                                run = input(
                                    f"{colors.blue}[+] Do You Want To Run?(y/n):{colors.reset}"
                                )
                                if run.lower() == "yes" or run.lower() == "y":
                                    #os.system(f"cd Tools/{self.github_check} && {self.command}")
                                    Recommended_Tool.recommended(name=name)
                                   
                        waiting.waiting()
            elif ask == "2":
                if self.writeup == "no-writeups":
                    pass
                else:
                    writeup.writeup(self.writeup, self.name)
            elif ask == "3":
                if method == "github":
                    uninstall_tool(method, self.github_check)
                else:
                    uninstall_tool(method,name)
            else:
                break
          

def check_path(name):   
    def find_folder(folder_name, root_folder="/"):
        for folder, subfolders, files in os.walk(root_folder):
            if folder_name in subfolders:
                return os.path.join(folder, folder_name)
        return "Folder not found"
    #folder_name = input("Enter the name of the folder you want to find: ")
    folder_name = name
    folder_path = find_folder(folder_name)
    #print("Folder Path:", folder_path)
    return folder_path

def uninstall_tool(method,name):
    if method == "kali":
            run = input(f"\033[1m{colors.red}[+] Do You Want To Uninstall the Tool?(y/n):{colors.reset}")
            if run.lower() == "y" or run.lower() == "yes":
	    	        os.system(f"sudo apt remove {name}")
    elif method == "go" :
            run = input(f"\033[1m{colors.red}[+] Do You Want To Uninstall the Tool?(y/n):{colors.reset}")
            if run.lower() == "y" or run.lower() == "yes":
	    	        os.system(f"rm -rf ~/go/bin/{name}")
    elif method == "pip":
            run = input(f"\033[1m{colors.red}[+] Do You Want To Uninstall the Tool?(y/n):{colors.reset}")
            if run.lower() == "y" or run.lower() == "yes":
	    	        os.system(f"pip uninstall {name}")
    elif method == "deb":
            run = input(f"\033[1m{colors.red}[+] Do You Want To Uninstall the Tool?(y/n):{colors.reset}")
            if run.lower() == "y" or run.lower() == "yes":
	    	        os.system(f"sudo dpkg --purge {name}")	 
    elif method == "github":
            run = input(f"\033[1m{colors.red}[+] Do You Want To Github Uninstall the Tool?(y/n):{colors.reset}")
            if run.lower() == "y" or run.lower() == "yes":

                print("Uninstallation...")
                folder_path = check_path(name)
                os.system(f'rm -rf {folder_path}')
                waiting.waiting()
    elif name == "burp":  
            print(f"{colors.blue}[+]1. Do You Want Uninstall Professional Version?{colors.reset}")
            print(f"{colors.blue}[+]2. Do You Want Uninstall COMMUNITY VERSION?{colors.reset}")
            run = input(f"\033[1m{colors.red}[+] press 1 for Professional Version and 2 for COMMUNITY VERSION : {colors.reset}")
            if run == "1":
                print("Uninstallation...")
                folder_path = check_path("Burp-Suite")
                os.system(f'rm -rf {folder_path}')
                waiting.waiting()
            if run == "2":
                print("Uninstallation...")
                os.system("sudo  apt remove burpsuite")
                waiting.waiting()

def load_banner(name):
    os.system("clear")
    banner.main()
    banner.attack(name)
def tool_writeups(name,check="no-writeups", tool_check="no-tools"):
    if tool_check != "no-tools":
        print(f"{colors.options}1) Launch")
    if check != "no-writeups":
        print(f"2) Write Ups")
    if check != "uninstall-tool":
        print(f"3) Uninstall ") 	
    print(f"4) Go Back..")
    try:
        ask = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
    except KeyboardInterrupt:
        return
    return ask
def exit_program():
    os.system("clear")
    banner.main()
    print("\033[38;5;105m", "[+] Thanks visit again".title())
    exit() 
    
def check_installed(name, run_arg):
    proc = subprocess.Popen(
        [f"dpkg -s {name} 2>> {os.path.dirname(__file__)}\\logs.txt "], stdout=subprocess.PIPE, shell=True
    )
    (there, notthere) = proc.communicate()
    if "install ok installed" not in there.decode():
        print(f"\n{colors.red}[+] Not Installed")
        try:
            install = input(
            f"{colors.blue}Do You Want To Install The Tool?(y/n):{colors.reset}"
        )
        except KeyboardInterrupt:
            return
        if install.lower() == "yes" or install.lower() == "y":
            os.system(f"apt install {name} -y")
            path = check_path(name)
            print(f"\nInstalled folder path : {path}")
            try:
                download = input(
                f"{colors.blue}Do You Want To Run The Tool?(y/n):{colors.reset}"
            )
            except KeyboardInterrupt:
                return
            if (
                download == "y"
                or download == "Y"
                or download == "Yes"
                or download == "yes"
            ):
                if run_arg == "kismet":
                    threading.Thread(target=thread_run, args=(run_arg,)).start()
                    print(
                        f"[+] {run_arg} is started at address: http://localhost:2501 (or the address of this system) for the Kismet UI"
                    )
                    KURL = "http://localhost:2501"
                    threading.Thread(target=run_on_browser.main, args=(KURL,)).start()
                elif run_arg == "fern-wifi-cracker":
                    threading.Thread(target=thread_run, args=(run_arg,)).start()
                    print("Fern-wifi-cracker Starting...")
                else:
                    os.system(f"{run_arg}")
                    Recommended_Tool.recommended(name=name)
    else:
        print(f"{colors.green}[+] Installed")
        try:
            download = input(
            f"{colors.blue}Do You Want To Run The Tool?(y/n):{colors.reset}"
        )
        except KeyboardInterrupt:
            return
        if download == "y" or download == "Y" or download == "Yes" or download == "yes":
            # os.system(f"{run_arg}")
            if run_arg == "kismet":
                threading.Thread(target=thread_run, args=(run_arg,)).start()
                print(
                    f"[+] {run_arg} is started at address: http://localhost:2501 (or the address of this system) for the Kismet UI"
                )
                KURL = "http://localhost:2501"
                threading.Thread(target=run_on_browser.main, args=(KURL,)).start()
            elif run_arg == "fern-wifi-cracker":
                threading.Thread(target=thread_run, args=(run_arg,)).start()
                print("Fern-wifi-cracker Starting...")
            else:
                #os.system(f"{run_arg}")
                load_banner(name=name)
                Recommended_Tool.recommended(name=name)


def thread_run(command):
    os.system(f"{command} >> {os.path.dirname(__file__)}\\logs.txt  2>&1")


def pip_install(name, run_arg):
    proc = subprocess.Popen([f"which {name}"], stdout=subprocess.PIPE, shell=True)
    (there, nothere) = proc.communicate()
    if there:
        print(f"{colors.green}[+] Installed")
        try:
            download = input(
            f"{colors.blue}Do You Want To Run The Tool?(y/n): {colors.reset} "
        )
        except KeyboardInterrupt:
            return
        if download.lower() == "y" or download.lower() == "yes":
            os.system(f"{run_arg}")
            Recommended_Tool.recommended(name=name)
    else:
        print(f"{colors.red}[+] Not Installed")
        try:
            download = input(
            f"{colors.blue}[+] Do You Want To Install It?(y/n):{colors.reset} "
        )
        except KeyboardInterrupt:
            return
        if download.lower() == "y" or download.lower() == "yes":
            os.system(f"pip install {name}")
            path = check_path(name)
            print(f"\nInstalled folder path : {path}")
            # os.system("go install github.com/projectdiscovery/katana/cmd/katana@latest")
            # os.system(f'sudo cp ~/go/bin/{name} /usr/bin')
            try:
                download = input(
                f"{colors.blue}\nDo You Want To Run The Tool?(y/n): {colors.reset}"
            )
            except KeyboardInterrupt:
                return
            if download.lower() == "y" or download.lower() == "yes":
                os.system(f"{run_arg}")
                Recommended_Tool.recommended(name=name)


def which_check(name, link, run_arg):
    proc = subprocess.Popen([f"which {name}"], stdout=subprocess.PIPE, shell=True)
    (there, nothere) = proc.communicate()
    if there:
        print(f"{colors.green}[+] Installed")
        try:
            download = input(
            f"{colors.blue}Do You Want To Run The Tool?(y/n): {colors.reset} "
        )
        except KeyboardInterrupt:
            return
        if download.lower() == "y" or download.lower() == "yes":
            os.system(f"{run_arg}")
            Recommended_Tool.recommended(name=name)
    else:
        print(f"{colors.red}[+] Not Installed")
        try:
            download = input(
            f"{colors.blue}[+] Do You Want To Install It?(y/n):{colors.reset} "
        )
        except KeyboardInterrupt:
            return
        if download.lower() == "y" or download.lower() == "yes":
            os.system(f"go install {link}")
            path = check_path(name)
            print(f"\nInstalled folder path : {path}")
            # os.system("go install github.com/projectdiscovery/katana/cmd/katana@latest")
            os.system(f"sudo cp ~/go/bin/{name} /usr/bin")
            try:
                download = input(
                f"{colors.blue}\nDo You Want To Run The Tool?(y/n): {colors.reset}"
            )
            except KeyboardInterrupt:
                return
            if download.lower() == "y" or download.lower() == "yes":
                os.system(f"{run_arg}")
                Recommended_Tool.recommended(name=name)


def deb_install(name, command, link):
    proc = subprocess.Popen(
        [f"dpkg -s {command} 2>> {os.path.dirname(__file__)}\\logs.txt "], stdout=subprocess.PIPE, shell=True
    )
    (there, notthere) = proc.communicate()
    if "install ok installed" not in there.decode():
        print(f"{colors.red}[+] Not Installed")
        try:
            install = input(
            f"{colors.blue}Do You Want To Install The Tool?(y/n):{colors.reset}"
        )
        except KeyboardInterrupt:
            return
        if install.lower() == "yes" or install.lower() == "y":
            if not os.path.exists(f"Tools/{link.split('/')[-1]}"):
                os.system(f"wget {link} -O Tools/{link.split('/')[-1]} ")
            os.system(f"dpkg -i Tools/{link.split('/')[-1]} ")
            path = check_path(name)
            print(f"\nInstalled folder path : {path}")
            try:
                install = input(
                f"{colors.blue}Do you want to run the tool?(y/n):{colors.reset}"	
            )
            except KeyboardInterrupt:
                return
            if install.lower() == "y" or install.lower == "yes":
                if command == "nessus":
                    os.system("systemctl start nessusd.service")
                    print(f"{colors.green}[+] Service Started....")
                    print(
                        f"{colors.blue}[+] YOU CAN CHECK IT'S WRITE UPS FOR MORE INFO{colors.reset}"
                    )
                    try:
                        use = input(
                        f"{colors.blue}[+] Do You Want To Configure Nessus?(y/n):{colors.reset}"
                    )
                    except KeyboardInterrupt:
                        return
                    if use == "y" or use == "Y" or use == "Yes" or use == "yes":
                        run_on_browser.main("https://localhost:8834/")
                else:
                    os.system(f"{command} 2>> {os.path.dirname(__file__)}\\logs.txt")
                    Recommended_Tool.recommended(name=name)
    else:
        print(f"{colors.green}[+] Installed")
        try:
            download = input(
            f"{colors.blue}Do You Want To Run The Tool?(y/n):{colors.reset}"
        )
        except KeyboardInterrupt:
            return
        if download.lower() == "y" or download.lower() == "yes":
            if command == "nessus":
                os.system("systemctl start nessusd.service")
                print(f"{colors.green}[+] Service Started....")
                print(
                    f"{colors.blue}[+] YOU CAN CHECK IT'S WRITE UPS FOR MORE INFO{colors.reset}"
                )
                try:
                    use = input(
                    f"{colors.blue}[+] Do You Want To Configure Nessus?(y/n):{colors.reset}"
                )
                except KeyboardInterrupt:
                    return
                if use == "y" or use == "Y" or use == "Yes" or use == "yes":
                    run_on_browser.main("https://localhost:8834/")
            else:
                os.system(f"{command} 2>> {os.path.dirname(__file__)}\\logs.txt")
                Recommended_Tool.recommended(name=name)
