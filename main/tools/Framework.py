from main.tools import template
import os
def main():
    print("\n[+] FrameWork")
    os.system("clear")
    template.template("Framework","no-tools","Writeups",
                    {
                            "OSINT Framework":"https://osintframework.com/",
                            "MITRE Framework":"https://attack.mitre.org/",
                    })



if __name__=='__main__':
    main()

