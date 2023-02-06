#!/usr/bin/python3
import os
import subprocess
from main.tools import banner

def main():
    os.system("clear")
    banner.main()
    banner.attack("Setup")
    update()
    os.system("pip install -r requirements.txt")
    os.system("sudo apt install golang -y")
    os.system("go env -w GO111MODULE=on")
    create_symlink()
def update():
        os.system("clear")
        banner.main()
        banner.attack("Update")
        print("[+] Checking for updates....".title())
        process = subprocess.Popen("git checkout . && git pull ",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (use,nouse)=process.communicate()
        if not nouse:
            if "Already up to date" in use.decode():
                print("[+] it is updated".title())
            elif "not a git repository" in use.decode():
                print("[-] IT is not a github repository".title())
            elif "Updating" in use.decode():
                print("[+] updating.....".title())
                print(use.decode())
                print("\u001b[32m[+] Cyberonix is UPDATED To Latest Version")
            else:
                print("[-] Something went wrong....".title())
                print(use.decode())
        else:
            print("[-] something went wrong".title())
            print(nouse)
        for i in range(3):
            print(f"[!] Redirecting in ...{3-i}sec\r".title(),end="")
            time.sleep(i)
def create_symlink():
    proc = subprocess.Popen([f"pwd"], stdout=subprocess.PIPE, shell=True)
    #there keyfor success output and noththere for error output
    (there, notthere) = proc.communicate()
    there=there.decode()
    there=there.split()
    f = open("run.sh", "w")
    f.write("#!/bin/bash")
    f.write("\n")
    f.write(f'cd {there[0]} && python3 cyberonix.py "$@"')
    f.close()
    os.system("chmod +x *")
    os.system("sudo mv run.sh /usr/bin/cyberonix")
    finish()
def finish():
    os.system("clear")
    banner.main()
    banner.attack("Setup Completed")
    os.system("cyberonix")

if __name__ == "__main__":
    main()

