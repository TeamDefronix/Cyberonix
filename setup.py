#!/usr/bin/python3
import os
import subprocess
from main.tools import banner,colors
#import cyberonix

def is_module_installed(module_name):
    try:
        pip_result = subprocess.run(['pip', 'show', module_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if pip_result.returncode == 0 and pip_result.stdout:
            return True
        
        apt_result = subprocess.run(['apt', 'list',  module_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if apt_result.returncode == 0 and module_name in apt_result.stdout:
            return True
        else:
            os.system("pip install dnspython==2.3.0")
    except Exception as e:
        print(f"An error occurred: {e}")
        return False



def exit_program():
    os.system("clear")
    banner.main()
    print("\033[38;5;105m","[+] Thanks visit again".title())
    exit()
try:
    def main():
        os.system("clear")
        banner.main()
        banner.attack("Setup")
        is_module_installed('dnspython')
        os.system("pip install -r requirements.txt")
        os.system("pip install selenium")
        os.system("sudo apt install golang -y")
        os.system("go env -w GO111MODULE=on")
        os.system("apt install php")
        os.system("mkdir output")
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
        os.system("sudo mv cyberonix.1 /usr/local/man/man1/")
        finish()
    def finish():
        os.system("clear")
        banner.main()
        banner.attack("Setup Completed")
        os.system("python3 cyberonix.py")
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    exit_program()
except Exception as err:
    os.system("clear")
    banner.main()
    banner.attack(f"{colors.red}ERROR{colors.reset}")
    banner.description(f"{colors.red}{err}{colors.reset}")



