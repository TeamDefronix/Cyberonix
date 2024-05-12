from main.tools import banner, colors, template
import os
import requests
from bs4 import BeautifulSoup


def main():
    while True:
        os.system("clear")
        banner.main()
        banner.attack("Digital Forensic Tools")
        list_attacks=["Autopsy","Binwalk","Hashdeep","Bulk Extractor","Go Back"]
        for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
        try:
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
        except KeyboardInterrupt:
            template.exit_program()
        if option == "1":
            print("\n[+] Autopsy")
            autopsy()        
        elif option == "2":
            print("\n[+] Binwalk")
            binwalk()            
        elif option == "3":
            print("\n[+] Hashdeep")
            hashdeep()        
        elif option == "4":
            print("\n[+] Bulk Extractor")
            bulk_extractor()        
        else:
            return

def autopsy():
    os.system("clear")
    github = "The Autopsy Forensic Browser is a graphical interface to the command line digital forensic analysis tools in The Sleuth Kit. Together, The Sleuth Kit and Autopsy provide many of the same features as commercial digital forensics tools for the analysis of Windows and UNIX file systems (NTFS, FAT, FFS, EXT2FS, and EXT3FS)."
    template.template(
                "autopsy",
                "autopsy",
                github.strip(),
                {"Forensic Autopsy":"https://www.ncbi.nlm.nih.gov/books/NBK539901/",
                "Autopsy – Cyber Forensic Browser in Kali Linux": "https://www.geeksforgeeks.org/autopsy-cyber-forensic-browser-in-kali-linux/",
                 "TryHackMe Autopsy Write-Up":"https://medium.com/@laupeiip/tryhackme-autopsy-write-up-98fad3e98e8b",
                },
            )
def bulk_extractor():
    os.system("clear")
    github = """bulk_extractor is a C++ program that scans a disk image, a file, or a directory of files and extracts useful information without parsing the file system or file system structures. The results are stored in feature files that can be easily inspected, parsed, or processed with automated tools. bulk_extractor also creates histograms of features that it finds, as features that are more common tend to be more important."""
    template.template(
                "bulk-extractor",
                "bulk_extractor",
                github.strip(),
                {"cheat sheet": "https://www.kalilinux.in/2020/01/bulk-extractor-kali-linux-forensics.html",
                 "Extracting Forensic Data from a Device Using Bulk Extractor":"https://www.researchgate.net/publication/350502325_Extracting_Forensic_Data_from_a_Device_Using_Bulk_Extractor",
                 "USER MANUAL":"https://digitalcorpora.s3.amazonaws.com/downloads/bulk_extractor/BEUsersManual.pdf",
                 "Using Bulk_extractor":"https://www.oreilly.com/library/view/digital-forensics-with/9781788625005/576053c4-24b9-42d5-a822-d44dbe05647c.xhtml",
                 },
            )
    

def binwalk():
    os.system("clear")
    github = "Binwalk is a popular open-source tool used in digital forensics and cybersecurity for analyzing, extracting, and identifying various file types embedded within firmware images and binary files. It is particularly useful for examining firmware images such as those found in embedded devices like routers, IoT devices, and other hardware."
    template.template(
                "binwalk",
                "binwalk",
                github.strip(),
                {"cheat sheet": "https://gbhackers.com/analyzing-embedded-files-and-executable-code-with-frimware-images-binwalk/",
                 "Analysing and extracting firmware using Binwalk":"https://fr3ak-hacks.medium.com/analysing-and-extracting-firmware-using-binwalk-982012281ff6",
                 "Reverse engineering my router's firmware with binwalk":"https://sergioprado.blog/reverse-engineering-router-firmware-with-binwalk/",
                 
                 },
            )
        
def hashdeep():
    os.system("clear")
    github = "hashdeep is a set of tools to compute MD5, SHA1, SHA256, tiger and whirlpool hashsums of arbitrary number of files recursively."
    template.template(
                "hashdeep",
                "hashdeep -h",
                github.strip(),
                {"cheat sheet":"https://www.codecnetworks.com/blog/hashdeep-chfi-forensics-tool/",
                 "Hashdeep -File Integrity Checker ( CHFI Forensics tool )":"https://www.codecnetworks.com/blog/hashdeep-chfi-forensics-tool/",
                 "Verify File Integrity with Hashdeep":"https://geekthis.net/post/file-integrity-with-hashdeep/",
                 },
            )
if __name__=='__main__':
    main()
