from main.tools import banner, template, colors, writeup
import os
import requests
from bs4 import BeautifulSoup



def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack(f"File Upload")
        list_attacks = ["Tools", "Writeups", "Go Back"]
        for i in range(len(list_attacks)):
            print(colors.options, f"{i+1}) {list_attacks[i]}".title(), colors.reset)
        try:
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            return
        if option == "1":
            while True:
                os.system("clear")
                banner.main()
                banner.attack(f"Tools")
                list_tools = ["fuxploider","go back"]
                for i in range(len(list_tools)):
                    print(
                        colors.options, f"{i+1}) {list_tools[i]}".title(), colors.reset
                    )
                try:
                    option = input(f"\n {colors.select}Select an Option ->{colors.reset} ")
                except KeyboardInterrupt:
                    return
                if option == "1":
                    print("\n[+] Fuxploider")
                    fuxploider()
                else:
                    break
        elif option == "2":
            # writeup.writeup({"Test Upload of Unexpected File Types":"https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types","What is Unrestricted File Upload?":"https://www.aptive.co.uk/blog/unrestricted-file-upload-testing/","File Upload General Methodology":"https://book.hacktricks.xyz/pentesting-web/file-upload","File upload vulnerabilities":"https://portswigger.net/web-security/file-upload","File Upload Attacks (Part 2)":"https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/","Hunting for Bugs in File Upload Feature:":"https://sm4rty.medium.com/hunting-for-bugs-in-file-upload-feature-c3b364fb01ba","How I abused the file upload function to get a high severity vulnerability in Bug Bounty":"https://infosecwriteups.com/how-i-abused-the-file-upload-function-to-get-a-high-severity-vulnerability-in-bug-bounty-7cdcf349080b","Directory Traversal via PHP Multi-File Uploads":"https://nealpoole.com/blog/tag/file-upload/"},"Writups")
            writeup.writeup(
                {
                    "Upload Scanner Website":"https://github.com/portswigger/upload-scanner",
                    "Test Upload of Unexpected File Types": "https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types",
                    "What is Unrestricted File Upload?": "https://www.aptive.co.uk/blog/unrestricted-file-upload-testing/",
                    "File Upload General Methodology": "https://book.hacktricks.xyz/pentesting-web/file-upload",
                    "File upload vulnerabilities": "https://portswigger.net/web-security/file-upload",
                    "File Upload Attacks (Part 2)": "https://blog.yeswehack.com/yeswerhackers/file-upload-attacks-part-2/",
                    "Hunting for Bugs in File Upload Feature:": "https://sm4rty.medium.com/hunting-for-bugs-in-file-upload-feature-c3b364fb01ba",
                    "How I abused the file upload function to get a high severity vulnerability in Bug Bounty": "https://infosecwriteups.com/how-i-abused-the-file-upload-function-to-get-a-high-severity-vulnerability-in-bug-bounty-7cdcf349080b",
                    "Directory Traversal via PHP Multi-File Uploads": "https://nealpoole.com/blog/tag/file-upload/",
                },
                "File Upload writups",
            )

        else:
            return


def github_getting_text(link, selector, indexvalue):
    print(f"Please Wait....\r", end="")
    URL = link
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, "html.parser")
        paras = soup.select(selector)
        # check index value from test file
        return paras[indexvalue].text
    except:
        return f"{colors.red}NotLloaded Because No Internet Connection{colors.reset}"

def fuxploider():
    os.system("clear")
    github = "Fuxploider is an open source penetration testing tool that automates the process of detecting and exploiting file upload forms flaws. This tool is able to detect the file types allowed to be uploaded and is able to detect which technique will work best to upload web shells or any malicious file on the desired web server."
    template.template(
                        "fuxploider",
                        "python3 fuxploider.py -h",
                        github,
                        "no-writeups",
                        link="https://github.com/almandin/fuxploider.git",
                        method="github",
                        github_install="git clone https://github.com/almandin/fuxploider.git && python3 -m pip install -r fuxploider/requirements.txt ",
                        github_check="fuxploider"
                    )
                
if __name__ == "__main__":
    main()

