import os
def main(URL):
        print("[+] Opening Article")
        os.system(f"sudo -u {os.getlogin()} -H firefox {URL} > /dev/null 2>&1")
