#!/usr/bin/python3
import os
import subprocess
from main.tools import banner,colors,template,Recommended_Tool,run_on_browser
from main import * 
import time,argparse

def exit_program():
    os.system("clear")
    banner.main()
    print("\033[38;5;105m","[+] Thanks visit again".title())
    exit()

try:
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
                try:
                    subprocess.run('cyberonix',shell=True, check = True)
                except Exception as err:
                    os.system("python3 cyberonix.py")
                exit()
            else:
                print("[-] Something went wrong....".title())
                print(use.decode())
        else:
            print("[-] something went wrong".title())
            print(nouse)
        for i in range(3):
            print(f"[!] Redirecting in ...{3-i}sec\r".title(),end="")
            time.sleep(i)
    def starting():
        parser = argparse.ArgumentParser(
            description="Cyberonix is a complete resource hub for Cyber Security Community. Our aim is to make this tool an 1 stop solution for all the Hackers out there to get resources of various topics in Cyber Security. We will keep updating this tool & adding new & updated resources on the go.",
        )
        main_args = parser.add_argument_group('Main Arguments')
            
        main_args.add_argument(
            "--tools", "-t",type=str,help=": Access various cybersecurity tools."
        )
        main_args.add_argument(

            "--cheatsheet", "-c", action="store_true", help=": Get a cybersecurity reference guide."

        )
        ip_args = parser.add_argument_group('IP')
        ip_args.add_argument(
            "--getip", "-gip", action="store_true",help=": Get Ip Of A Domain. \nCan use with: --domain, --file, --output",
        )
                              
        dns_Args = parser.add_argument_group('DNS Records')
        parser.add_argument("--domain", "-D", dest='domain', nargs="?" , const="" ,help=': Specify the domain', option_strings=['--domain'])
        dns_Args.add_argument(
            "--dnsrecord", "-dns", action="store_true", help=": To Get DNS Records of a domain. Can use with: --domain, --file, --output "
        )
        dns_Args.add_argument(
            "--record", "-r", help=": Specify the type of DNS record (e.g., A, TXT, MX). \nusage: --record <type>"
        )
        screenshot_Args = parser.add_argument_group('Screenshoting')
        screenshot_Args.add_argument(
            "--screenshot",
            "-s",
            action="store_true",
            help=": To take a Screenshot Of Website/Websites. \nCan use with: --domain,--file,--output",
        )
        parser.add_argument("--output", "-o", help=": Save the results to the file Specify File location -o path/to/location")
        parser.add_argument("--file", "-f", help=": Read input from a file Specify An Input File -f path/to/file.txt")
        
        asn_Args = parser.add_argument_group('ASN Record')
        parser.add_argument("--ip", "-ip", help="Specify IP Address")
        asn_Args.add_argument(
                "--asnrecord", "-asn", action="store_true", help=": Get ASN (network) information. \n Can use with:  --ip,--file,--output"
        )
        password_Args = parser.add_argument_group("Password Generation")
        password_Args.add_argument(
            "--passwordgen", "-P", action="store_true", help=": To Generate a Password"
        )
        password_Args.add_argument(
            "--default-password-gen",
            "-pass",
            action="store_true",
            help=": To Generate Random Password (Recommended)(only use --length, --checkpassword for customization).",
        )
        
        password_Args.add_argument(
            "--upper", "-u", action="store_true", help=": For Uppercase"
        )
        password_Args.add_argument(
            "--lower", "-l", action="store_true", help=": For Lowercase"
        )
        password_Args.add_argument(
            "--digits", "-d", action="store_true", help=": For Digits"
        )
        password_Args.add_argument(
            "--punctuation", "-p", action="store_true", help=": For Punctuation"
        )
        password_Args.add_argument(
            "--length", "-L", help=": To Specify Length Of Password (Default=8)"
        )
        password_Args.add_argument(
            "--checkpassword",
            "-C",
            action="store_true",
            help=": To Check Your Generated Password",
        )
        wordlist_Args = parser.add_argument_group("Wordlist Generation")
        wordlist_Args.add_argument(
            "--wordlist", "-w", action="store_true", help=": To Generate a Wordlist"
        )
        wordlist_Args.add_argument("-ch", "--characters", type=str, default="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                   help=": Set of characters to include in the wordlist")
        wordlist_Args.add_argument("-min", "--min_length", type=int, default=4, help=": Minimum length of the words ( Default = 4 )")
        wordlist_Args.add_argument("-max", "--max_length", type=int, default=6, help=": Maximum length of the words ( Default = 6 )")
        wordlist_Args.add_argument("-ot", "--output_file", type=str, default="custom_wordlist.txt", help=": Output file name ( Default = custom_wordlist.txt )")

        hstatus_Args = parser.add_argument_group('HTTP Status')
        hstatus_Args.add_argument(
            "--http-status",
            "-S",
            action="store_true",
            help=": Check a website's HTTP status code." "\nCan use with: --domain, --file, --output" ,
        )
        remove_dub_Args = parser.add_argument_group('remove duplicate')
        remove_dub_Args.add_argument(
            "--remove-duplicate",
            "-rd",
            action="store_true",
            help=": To Remove Duplicates From a File. Can use with: --file,--output",
        )
        args = parser.parse_args()
        if args.tools:
            arguments.tools(args.tools) 
        elif args.getip:
            
            if args.file:
                if args.output:
                    arguments.getip(path=args.file, output=args.output)
                else:
                    arguments.getip(path=args.file)
            elif args.domain:
                if args.output:
                    arguments.getip(url=args.domain,output=args.output)                    
                else:
                    arguments.getip(url=args.domain)
            else:
                if args.output:
                    arguments.getip(url=args.getip, output=args.output)
                else:
                    arguments.getip(url=args.getip)
                #print(
                    #f"{colors.red}[!] Please enter file with --file path/to/file or pass a single domain with --domain https://example.com{colors.reset}"
                #)

        elif args.cheatsheet:
            run_on_browser.main("https://github.com/defronixpro/Defronix-Cybersecurity-Roadmap/blob/main/cheatsheet.md")
       
        elif args.screenshot:
            if args.file:
                if args.output:
                    arguments.screenshot(path=args.file,output=args.output)
                else:
                    arguments.screenshot(path=args.file)
            elif args.domain:
                if args.output:
                    arguments.screenshot(url=args.domain,output=args.output)
                else:
                    arguments.screenshot(url=args.domain)

            else:
                print(
                    f"{colors.red}[!] Please enter file with --file path/to/file or pass a single domain with --domain https://example.com{colors.reset}"
                )
        elif args.remove_duplicate:
            if args.file:
                if args.output:
                    arguments.remove_dublicates(location=args.file, output=args.output)
                else:
                    arguments.remove_dublicates(location=args.file)

            else:
                print(
                    f"{colors.red}[!] Please enter file with --file path/to/file or pass a single domain with --domain https://example.com{colors.reset}"
                )

        elif args.asnrecord:
            if args.file:
                if args.output:
                    arguments.asnrecord(path=args.file, output=args.output)
                else:
                    arguments.asnrecord(path=args.file)
            elif args.ip:
                if args.output:
                    arguments.asnrecord(url=args.ip, output=args.output)
                else:
                    arguments.asnrecord(url=args.ip)

            else:
                print(
                    f"{colors.red}[!] Please enter file with --file path/to/file or pass a single ip with --ip 8.8.8.8{colors.reset}"
                )

        elif args.http_status:
            if args.file:
                if args.output:
                    arguments.http_status_code(path=args.file, output=args.output)
                else:
                    arguments.http_status_code(path=args.file)
            elif args.domain:
                if args.output:
                    arguments.http_status_code(url=args.domain, output=args.output)
                else:
                    arguments.http_status_code(url=args.domain)
            else:
                print(
                    f"{colors.red}[!] Please enter file with --file path/to/file or pass a single domain with --domain https://example.com{colors.reset}"
                )

        elif args.passwordgen:
            if args.length:
                arguments.password_gen(
                    args.upper,
                    args.lower,
                    args.digits,
                    args.punctuation,
                    args.length,
                    args.checkpassword,
                )
            else:
                arguments.password_gen(
                    args.upper,
                    args.lower,
                    args.digits,
                    args.punctuation,
                    check=args.checkpassword,
                )
        elif args.default_password_gen:
            if args.length:
                arguments.password_gen(length=args.length, check=args.checkpassword)
            else:
                arguments.password_gen(check=args.checkpassword)

        elif args.wordlist:
            arguments.generate_wordlist(
                args.characters,
                args.min_length,
                args.max_length,
                args.output_file
            )
                
        elif args.dnsrecord:
            if args.record:
                if args.file:
                    if args.output:
                        arguments.dnsrecords(path=args.file, names=args.record,output=args.output)
                    else:
                        arguments.dnsrecords(path=args.file, names=args.record)
                elif args.domain:
                    if args.output:
                        arguments.dnsrecords(url=args.domain, names=args.record,output=args.output)
                    else:
                        arguments.dnsrecords(url=args.domain, names=args.record)
                else:
                    print("please give --domain/--file also")
            elif args.domain:
                if args.record:
                    if args.output:
                        arguments.dnsrecords(url=args.domain, names=args.record,output=args.output)
                    else:
                        arguments.dnsrecords(url=args.domain, names=args.record)
                else:
                    print("please give --record also")
        else:
            main()

    def main():
        #update()
        os.system("chmod +x *")
        proc = subprocess.Popen([f"id"], stdout=subprocess.PIPE, shell=True)
        #there keyfor success output and noththere for error output
        (there, notthere) = proc.communicate()
        there=there.decode()
        if "root" not in there:
            try:
                subprocess.run('sudo cyberonix',shell=True, check = True)
            except Exception as err:
                os.system("sudo python3 cyberonix.py")
            # os.system("sudo cyberonix")
            exit()
        while True:
            os.system("clear")
            banner.main()
            list_attacks=["TOOLS","CHEATSHEET","Bug Bounty","Certifications & Roadmap","Write Ups","Man Page","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i+1}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
            if option=="1":
                os.system("clear")
                tool.main()
            elif option=="2":
                run_on_browser.main("https://github.com/defronixpro/Defronix-Cybersecurity-Roadmap/blob/main/cheatsheet.md")
            elif option == "3":
                os.system("clear")
                Bug_Bounty.main()
            elif option =="4":
                run_on_browser.main("https://github.com/defronixpro/Defronix-Cybersecurity-Roadmap/blob/main/README.md")
            elif option == "5":
                run_on_browser.main("https://github.com/defronixpro/Defronix-Cybersecurity-Roadmap/blob/main/Writeups.md")
            elif option=="6":
                os.system("clear")
                os.system("man cyberonix")
            else:
                exit_program()
    #to run file separately
    if __name__ == "__main__": 
        starting()
except KeyboardInterrupt:
    exit_program()
#except Exception as err:
    #os.system("clear")
#    banner.main()
#    banner.attack(f"{colors.red}ERROR{colors.reset}")
#    banner.description(f"{colors.red}{err}{colors.reset}")

