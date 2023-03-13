#!/usr/bin/python3
import os
import subprocess
from main import *
from main.tools import banner,colors
import time

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
            "--tools", "-t", action="store_true", help="Run Tools Function"
        )
        main_args.add_argument(
            "--cheatsheet", "-c", action="store_true", help="Run Cheatsheet Function"
        )
        main_args.add_argument(
            "--news",
            "-n",
            nargs="?",
            metavar="Date",
            const="latest",
            type=str,
            help="Date In The Format yyyy-mm-dd",
        )
        ip_args = parser.add_argument_group('IP')
        ip_args.add_argument(
            "--getip", "-gip", help="Get Ip Of A Domain(options: --file,--domain,--output)", action="store_true",
        )
        ip_args.add_argument("--ipinfo", "-ipi", action="store_true", help="Get IP Infomation(Options: --ip,--file,--output)")
                      
        dns_Args = parser.add_argument_group('DNS Records')
        parser.add_argument("--domain", "-D", dest='domain',
                    help='Specify the domain', option_strings=['--domain'])
        dns_Args.add_argument(
            "--dnsrecord", "-dns", action="store_true", help="To Get DNS Records(options: --domain,--file,--output) and use --record to specify record name"
        )
        dns_Args.add_argument(
            "--record", "-r", help="To Give Record For DNSrecord(Like: A,TXT,MX)"
        )
        screenshot_Args = parser.add_argument_group('Screenshoting')
        screenshot_Args.add_argument(
            "--screenshot",
            "-s",
            action="store_true",
            help="To Get Screenshot Of Websites(options: --file,--domain,--output)",
        )
        parser.add_argument("--output", "-o", help="Specify An Output File (-o path/to/location)")
        parser.add_argument("--file", "-f", help="Specify An Input File (-f path/to/file.txt)")
        
        asn_Args = parser.add_argument_group('ASN Record')
        parser.add_argument("--ip", "-ip", help="Specify IP Address")
        asn_Args.add_argument(
                "--asnrecord", "-asn", action="store_true", help="To Get ASN Record(Options: --ip,--file,--output)"
        )
        password_Args = parser.add_argument_group("Password Generation")
        password_Args.add_argument(
            "--passwordgen", "-P", action="store_true", help="To Generate Password"
        )
        password_Args.add_argument(
            "--default-password-gen",
            "-pass",
            action="store_true",
            help="To Generate Random Password (Recommended)(You can only use --length,--checkpassword)",
        )

        password_Args.add_argument(
            "--upper", "-u", action="store_true", help="For Uppercase"
        )
        password_Args.add_argument(
            "--lower", "-l", action="store_true", help="For Lowercase"
        )
        password_Args.add_argument(
            "--digits", "-d", action="store_true", help="For Digits"
        )
        password_Args.add_argument(
            "--punctuation", "-p", action="store_true", help="For Punctuation"
        )
        password_Args.add_argument(
            "--length", "-L", help="To Specify Length Of Password (Default=8)"
        )
        password_Args.add_argument(
            "--checkpassword",
            "-C",
            action="store_true",
            help="To Check Your Generated Password",
        )
        
        hstatus_Args = parser.add_argument_group('HTTP Status')
        hstatus_Args.add_argument(
            "--http-status",
            "-S",
            action="store_true",
            help="To Get Http Status Code Of A Domain(Options: --domain,--file,--output)",
        )
        remove_dub_Args = parser.add_argument_group('remove duplicate')
        remove_dub_Args.add_argument(
            "--remove-duplicate",
            "-rd",
            action="store_true",
            help="To Remove Dublicates From a File(Options: --file,--output)",
        )
        args = parser.parse_args()

        if args.tools:
            tool.main()
        elif args.getip:
            if args.file:
                if args.output:
                    arguments.getip(path=args.file, output=args.output)
                else:
                    arguments.getip(path=args.file)
            elif args.domain:
                if args.output:
                    arguments.getip(url=args.domain, output=args.output)
                else:
                    arguments.getip(url=args.domain)
            else:
                print(
                    f"{colors.red}[!] Please file with --file path/to/file or pass a single domain with --domain https://example.com{colors.reset}"
                )

        elif args.cheatsheet:
            Cheat_sheet.main()
        elif args.news:
            if args.news == "latest" or args.news is None:
                news.main(args.news)
            else:
                news.main(args.news)
        elif args.cheatsheet:
            Cheat_sheet.main()
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
                    f"{colors.red}[!] Please file with --file path/to/file or pass a single domain with --domain https://example.com{colors.reset}"
                )
        elif args.remove_duplicate:
            if args.file:
                if args.output:
                    arguments.remove_dublicates(location=args.file, output=args.output)
                else:
                    arguments.remove_dublicates(location=args.file)

            else:
                print(
                    f"{colors.red}[!] Please file with --file path/to/file or pass a single domain with --domain https://example.com{colors.reset}"
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
                    f"{colors.red}[!] Please file with --file path/to/file or pass a single ip with --ip 8.8.8.8{colors.reset}"
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
                    f"{colors.red}[!] Please file with --file path/to/file or pass a single domain with --domain https://example.com{colors.reset}"
                )
        elif args.ipinfo:
            arguments.ipinformation(args.ipinfo)
            if args.file:
                if args.output:
                    arguments.ipinformation(path=args.file, output=args.output)
                else:
                    arguments.ipinformation(path=args.file)
            elif args.domain:
                if args.output:
                    arguments.ipinformation(url=args.ip, output=args.output)
                else:
                    arguments.ipinformation(url=args.ip)
            else:
                print(
                    f"{colors.red}[!] Please file with --file path/to/file or pass a single ip with --ip 8.8.8.8{colors.reset}"
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
        update()
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
            list_attacks=["TOOLS","CHEATSHEET","NEWS","exit"]
            for i in range(len(list_attacks)):
                print(colors.options,f"{i}) {list_attacks[i]}".title(),colors.reset)
            option = input(f"\n {colors.select}Select An Option ->{colors.reset}  ")
            if option=="0":
                os.system("clear")
                tool.main()
            elif option=="1":
                os.system("clear")
                Cheat_sheet.main()
            elif option=="2":
                os.system("clear")
                news.main()
            else:
                exit_program()
    #to run file separately
    if __name__ == "__main__": 
        main()
except KeyboardInterrupt:
    exit_program()
except Exception as err:
    os.system("clear")
    banner.main()
    banner.attack(f"{colors.red}ERROR{colors.reset}")
    banner.description(f"{colors.red}{err}{colors.reset}")
