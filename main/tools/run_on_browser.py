import subprocess
import os
def main(URL):
        # print("[+] Opening url")
        print("[+] Opening Article")
        user=os.getlogin()
        if "root" in user:
            os.system(f"firefox {URL} /dev/null 2>&1" )
        else:
            os.system(f"sudo chown root:root /run/user/{user}/gdm/Xauthority > /dev/null 2>&1")
            # os.system(f"firefox {URL} 2>/dev/null")
            os.system(f"sudo chown root:root /home/{user}/.Xauthority > /dev/null 2>&1")
            os.system(f"firefox {URL} /dev/null 2>&1")
