import subprocess
import os
def main(URL):
        # print("[+] Opening url")
        print("[+] Opening Article")
        proc = subprocess.Popen([f"pwd"], stdout=subprocess.PIPE, shell=True)
        #there keyfor success output and noththere for error output
        (there, notthere) = proc.communicate()
        there=there.decode()
        there=there.split("/")
        if "root" in there:
            os.system(f"firefox {URL} 2>/dev/null" )
        else:
            #this is to get desktop enviroment
            proc = subprocess.Popen([f"echo $DESKTOP_SESSION"], stdout=subprocess.PIPE, shell=True)
            (envo, noenvo) = proc.communicate()
            #this is to get username
            proc = subprocess.Popen([f"cat /etc/passwd | grep {there[2]}"], stdout=subprocess.PIPE, shell=True)
            (uid, notuid) = proc.communicate()
            uid=uid.decode()
            uid=uid.split(":")
            os.system(f"sudo chown root:root /run/user/{uid[2]}/gdm/Xauthority > /dev/null 2>&1")
            # os.system(f"firefox {URL} 2>/dev/null")
            os.system(f"sudo chown root:root /home/{there[2]}/.Xauthority > /dev/null 2>&1")
            os.system(f"firefox {URL} 2>/dev/null")
