#!/usr/bin/python3
import os
import subprocess
from main.tools import banner

def main():
    os.system("clear")
    banner.main()
    banner.attack("Setup")
    os.system("sudo apt install python3-pip")
    os.system("pip install -r requirements.txt")
    os.system("sudo apt install golang -y")
    os.system("go env -w GO111MODULE=on")
    create_symlink()
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

