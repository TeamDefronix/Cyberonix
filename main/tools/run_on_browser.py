import os
def main(URL):
        # print("[+] Opening url")
        print("[+] Opening.....")
        user=os.getlogin()
        if "root" in user:
            os.system(f"firefox {URL} > /dev/null 2>&1" )
        else:
            os.system(f"sudo chown root:root /run/user/{user}/gdm/Xauthority > /dev/null 2>&1")
            os.system(f"sudo chown root:root /home/{user}/.Xauthority > /dev/null 2>&1")
            os.system(f"firefox {URL} > /dev/null 2>&1")
            os.system(f"sudo chown {user}:{user} /run/user/{user}/gdm/Xauthority > /dev/null 2>&1")
            os.system(f"sudo chown {user}:{user} /home/{user}/.Xauthority > /dev/null 2>&1")

