import dns.resolver, requests, socket, os, time
import random
from main import tool
from main.tools import *
from selenium import webdriver
from ipwhois import IPWhois
from main.tools import colors, banner,template,Recommended_Tool
import argparse, itertools

def tools(name):
    try:
        getattr(information_gathering, name)()
        getattr(Vulnerability_Analysis, name)()
        getattr(WEB_Application_Analysis, name)()
        getattr(Password_Hacking, name)()
        getattr(Wireless_Hacking, name)()
        getattr(Exploitation_Tools, name)()
        getattr(Sniffing_and_Spoofing, name)()
        getattr(PostExploitationAttacks, name)()
        getattr(Anonymity, name)()
        getattr(Framework, name)()
        getattr(Pentesting_Bug_Bounty, name)()
        getattr(forensic, name)()
    except KeyboardInterrupt:
        return
    except Exception as err:
        return
    
def getip(url='',path='',output=''):
        banner.main()
        banner.attack("Get Ip")
        url=domain()['no_http'](url)
        if url!="ip":
            if path != "":
                try:
                    f = open(path, "r")
                    urls = f.read()
                    urls = urls.split("\n")
                    for url in urls:
                        if url != "":
                            url=domain()['no_http'](url)
                            if url!='ip':
                                    try:
                                        ip_address = socket.gethostbyname(url)
                                        if output != "":
                                            outputfunc(output, f"{url}\t --> \t{ip_address}")

                                        print(
                                            f"{colors.green}[+]{url}\t --> \t{ip_address}{colors.reset}"
                                        )
                                    except Exception as err:
                                        if output != "":
                                            outputfunc(output, f"{url}\t --> Something Went Wrong --> [!] {err}")
                                        print(f"{colors.red}[-]{url}\t --> Something Went Wrong --> [!] {err}{colors.reset}")
                            else:
                                print(f"{colors.red}[-]{url}\t -->\tYou Have Entered IP{colors.reset}")
                                if output != "":
                                            outputfunc(output, f"{url}\t -->\tYou Have Entered IP")

                except KeyboardInterrupt:
                    exit_program()
                except Exception as err:
                    print(
                        f"{colors.red}[-] Something Went Wrong\n[!] {err}\n[!] Check Your File location"
                    )
            else:
                url=domain()['no_http'](url)
                if url!='ip':
                        try:
                            ip_address = socket.gethostbyname(url)
                            if output != "":
                                outputfunc(output, f"{url}\t --> \t{ip_address}")

                            print(
                                f"{colors.green}[+]{url}\t --> \t{ip_address}{colors.reset}"
                            )
                        except Exception as err:
                            if output != "":
                                outputfunc(output, f"{url}\t --> Something Went Wrong --> [!] {err}")
                            print(f"{colors.red}[-]{url}\t --> Something Went Wrong --> [!] {err}{colors.reset}")
                else:
                    print(f"{colors.red}[-]{url}\t -->\tYou Have Entered IP{colors.reset}")
                    if output != "":
                                outputfunc(output, f"{url}\t -->\tYou Have Entered IP")
        else:
            print(f"{colors.red}[-] Something Went Wrong\n[!] Maybe You have Entered Ip")


def dnsrecords(url="", names='',path='',output=''):
        banner.main()
        banner.attack("DNS Records")
        names = names.upper()
        names = names.split(",")
        url=domain()['no_http'](url)
        if url!="ip":
            if path != "":
                try:
                    f = open(path, "r")
                    urls = f.read()
                    urls = urls.split("\n")
                    for url in urls:
                        if url != "":
                            url=domain()['no_http'](url)
                            if url!='ip':
                                for name in names:
                                    try:
                                        answers = dns.resolver.resolve(url, name)
                                        for answer in answers:
                                            if output != "":
                                                outputfunc(output, f"{url}\t -->\t{name}\t -->\t{answer}")
                                            print(
                                                f"{colors.blue}[+]{url}\t -->\t{name}\t -->\t{colors.green}{answer}{colors.reset}"
                                            )
                                    except dns.rdatatype.UnknownRdatatype:
                                        if output != "":
                                            outputfunc(output, f"{url}\t -->\t{name}\t -->\tWrong Record Input")
                                        print(f"{colors.red}[-]{url}\t -->\t{name}\t -->\tWrong Record Input{colors.reset}")
                                    except dns.resolver.NoAnswer:
                                        if output != "":
                                            outputfunc(output, f"{url}\t -->\t{name}\t -->\tRecord Found")
                                        print(f"{colors.red}[-]{url}\t -->\t{name}\t -->\tNo {name} Record Found{colors.reset}")
                                    except dns.resolver.NXDOMAIN:
                                        print(f"{colors.red}[-]{url}\t -->\t{name}\t -->\tHost {domain} Not Found{colors.reset}")
                                        if output != "":
                                            outputfunc(output, f"{url}\t -->\t{name}\t -->\tHost {domain} Not Found")
                                    except Exception as err:
                                        print(f"{colors.red}[-]{url}\t -->\t{name}\t -->\terr:{err}{colors.reset}")
                                        if output != "":
                                            outputfunc(output, f"{url}\t -->\t{name}\t -->\terr:{err}")

                            else:
                                print(f"{colors.red}[-]{url}\t -->\tYou Have Entered IP{colors.reset}")
                                if output != "":
                                            outputfunc(output, f"{url}\t -->\tYou Have Entered IP")

                except KeyboardInterrupt:
                    exit_program()
                except Exception as err:
                    print(
                        f"{colors.red}[-] Something Went Wrong\n[!] {err}\n[!] Check Your File location"
                    )
            else:
                for name in names:
                    try:
                        answers = dns.resolver.resolve(url, name)
                        for answer in answers:
                            if output != "":
                                outputfunc(output, f"{url}\t -->\t{name}\t -->\t{answer}")
                            print(
                                f"{colors.blue}[+]{url}\t -->\t{name}\t -->\t{colors.green}{answer}{colors.reset}"
                            )
                    except dns.rdatatype.UnknownRdatatype:
                        if output != "":
                            outputfunc(output, f"{url}\t -->\t{name}\t -->\tWrong Record Input")
                        print(f"{colors.red}[-]{url}\t -->\t{name}\t -->\tWrong Record Input{colors.reset}")
                    except dns.resolver.NoAnswer:
                        if output != "":
                            outputfunc(output, f"{url}\t -->\t{name}\t -->\tRecord Found")
                        print(f"{colors.red}[-]{url}\t -->\t{name}\t -->\tNo {name} Record Found{colors.reset}")
                    except dns.resolver.NXDOMAIN:
                        print(f"{colors.red}[-]{url}\t -->\t{name}\t -->\tHost {domain} Not Found{colors.reset}")
                        if output != "":
                            outputfunc(output, f"{url}\t -->\t{name}\t -->\tHost {domain} Not Found")
                    except Exception as err:
                        print(f"{colors.red}[-]{url}\t -->\t{name}\t -->\terr:{err}{colors.reset}")
                        if output != "":
                            outputfunc(output, f"{url}\t -->\t{name}\t -->\terr:{err}")

        else:
            print(f"{colors.red}[-] Something Went Wrong\n[!] Maybe You have Entered Ip")



def checking(result_str):

        print(f"{colors.green}Checking for password{colors.reset}")
        passwords = [
            "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords.txt",
            "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt",
            "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt",
            "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-1000000.txt",
        ]
        for link in range(len(passwords)):
            pass_check(passwords[link], result_str, link)


def pass_check(url, password, number):
        print(f"{colors.blue}Test {number}{colors.reset}")
        raw = requests.get(url)
        lists = raw.text.split("\n")
        for i in lists:
            if password == i:
                print(f"{colors.red}FAILED{colors.reset}")
        else:
            print(f"{colors.green}PASSED{colors.reset}")


def exit_program():
    print("\033[38;5;105m", "[+] Thanks visit again".title())
    exit()


def asnrecord(path="", url="", output=""):
        banner.main()
        banner.attack("ASN")
        if path != "":
            try:
                f = open(path, "r")
                urls = f.read()
                urls = urls.split("\n")
                for url in urls:
                    if url != "":
                        valid=ip_valid(url)
                        if valid==1:
                            try:
                                ipwhois = IPWhois(url)
                                result = ipwhois.lookup_rdap()
                                if output != "":
                                    outputfunc(output, f"{url}\t --> {result['asn']}")
                                print(
                                    f"{colors.blue}[+] {url}\t --> {colors.green}{result['asn']}{colors.reset}"
                                )
                            except KeyboardInterrupt:
                                exit_program()
                            except Exception as err:
                                if output != "":
                                    outputfunc(output, f"{url}\t --> err:{err}")
                                    print(
                                        f"{colors.red}[+] {url}\t --> {colors.red}err:{err}{colors.reset}"
                                    )
                        else:
                            print(f"{colors.red}[-] Something Went Wrong\n[!] Maybe You have Entered Domain Or Ip Range Is Wrong")
            except KeyboardInterrupt:
                exit_program()
            except Exception as err:
                print(
                    f"{colors.red}[-] Something Went Wrong\n[!] {err}\n[!] Check Your File location"
                )
        else:
            try:
                valid=ip_valid(url)
                if valid==1:
                    ipwhois = IPWhois(url)
                    result = ipwhois.lookup_rdap()
                    if output != "":
                        outputfunc(output, f"{url}\t --> {result['asn']}")
                    print(
                        f"{colors.blue}[+] {url}\t --> {colors.green}{result['asn']}{colors.reset}"
                    )
                else:
                    print(f"{colors.red}[-] Something Went Wrong\n[!] Maybe You have Entered Domain Or Ip Range Is Wrong")
            except KeyboardInterrupt:
                exit_program()
            except:
                if output != "":
                    outputfunc(output, f"{url}\t --> Something Went Wrong")
                print(
                    f"{colors.red}[+] {url}\t --> {colors.red}Something Went Wrong{colors.reset}"
                )


def outputfunc(addr, line):

    f = open(addr, "a")
    f.write(line)
    f.write("\n")
    f.close()


def http_status_code(path="", url="", output=""):
        link=domain()['check_http'](url)
        banner.main()
        banner.attack("HTTP Status Code")
        if link=="ip":
            print(f'{colors.red}Something Went Wrong\n[!] You Have Entered IP{colors.reset}')
            return
        else:
            if path != "":
                try:
                    f = open(path, "r")
                    urls = f.read()
                    urls = urls.split("\n")
                    for url in urls:
                        if url != "":
                            link=domain()['check_http'](url)
                            if link=="ip":
                                print(
                                            f"{colors.red}[+] {url}\t --> {colors.red}You Have Entered Ip{colors.reset}"
                                        )
                            else:
                                for url in link:
                                    try:
                                        headers = {
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
                                        }
                                        response = requests.get(url,allow_redirects=False, headers=headers, timeout=20)
                                        status = str(response.status_code)
                                        if status[0] == "1":
                                            print(
                                                f"{colors.blue}[+] {url}\t --> {colors.light_blue}{status}{colors.reset}"
                                            )
                                        elif status[0] == "2":
                                            print(
                                                f"{colors.blue}[+] {url}\t --> {colors.green}{status}{colors.reset}"
                                            )
                                        elif status[0] == "3":
                                            print(
                                                f"{colors.blue}[+] {url}\t --> {colors.yellow}{status}{colors.reset}",end=''
                                            )
                                            try:
                                                response = requests.get(url, headers=headers, timeout=20)
                                                status = str(response.status_code)
                                                new_url=str(response.url)
                                                if status[0] == "1":
                                                    print(
                                                        f"{colors.blue} --> {colors.light_blue}{status} -->{colors.blue} {new_url}{colors.reset}"
                                                    )
                                                elif status[0] == "2":
                                                    print(
                                                        f"{colors.blue} --> {colors.green}{status} -->{colors.blue} {new_url}{colors.reset}"
                                                    )
                                                elif status[0] == "3":
                                                    print(
                                                        f"{colors.blue} --> {colors.yellow}{status} -->{colors.blue} {new_url}{colors.reset}"
                                                    )
                                                elif status[0] == "4":
                                                    print(
                                                        f"{colors.blue} --> {colors.red}{status} -->{colors.blue} {new_url}{colors.reset}"
                                                    )
                                                elif status[0] == "5":
                                                    print(
                                                        f"{colors.blue} --> {colors.purple}{status} -->{colors.blue} {new_url}{colors.reset}"
                                                    )
                                                else:
                                                    print(
                                                        f"{colors.blue} --> {colors.green}{status} -->{colors.blue} {new_url}{colors.reset}"
                                                    )
                                            except Exception as err:
                                                if "timed out" in str(err):
                                                    err = "Connection Time Out"
                                                print(
                                                    f"{colors.red} --> {colors.red}{err}{colors.reset}"
                                                )


                                        elif status[0] == "4":
                                            print(
                                                f"{colors.blue}[+] {url}\t --> {colors.red}{status}{colors.reset}"
                                            )
                                        elif status[0] == "5":
                                            print(
                                                f"{colors.blue}[+] {url}\t --> {colors.purple}{status}{colors.reset}"
                                            )
                                        else:
                                            print(
                                                f"{colors.blue}[+] {url}\t --> {colors.green}{status}{colors.reset}"
                                            )
                                        if output != "":
                                            outputfunc(output, f"{url}\t --> {status}")
                                    except Exception as err:
                                        if "timed out" in str(err):
                                            err = "Connection Time Out"
                                        if output != "":
                                            outputfunc(output, f"{url}\t --> {err}")
                                        print(
                                            f"{colors.red}[-] {url}\t --> {colors.red}{err}{colors.reset}"
                                        )
                                    time.sleep(0.5)
                except KeyboardInterrupt:
                    exit_program()

                except Exception as err:
                    print(f"{colors.red}[-] Something Went Wrong\n[!] {err}")
            else:
                try:
                    if url != "":
                        for url in link:
                            try:
                                headers = {
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
                                }
                                response = requests.get(url,allow_redirects=False , headers=headers, timeout=20)
                                status = str(response.status_code)
                                if status[0] == "1":
                                    print(
                                        f"{colors.blue}[+] {url}\t --> {colors.light_blue}{status}{colors.reset}"
                                    )
                                elif status[0] == "2":
                                    print(
                                        f"{colors.blue}[+] {url}\t --> {colors.green}{status}{colors.reset}"
                                    )
                                elif status[0] == "3":
                                    print(
                                        f"{colors.blue}[+] {url}\t --> {colors.yellow}{status}{colors.reset}"
                                    )
                                elif status[0] == "4":
                                    print(
                                        f"{colors.blue}[+] {url}\t --> {colors.red}{status}{colors.reset}"
                                    )
                                elif status[0] == "5":
                                    print(
                                        f"{colors.blue}[+] {url}\t --> {colors.purple}{status}{colors.reset}"
                                    )
                                else:
                                    print(
                                        f"{colors.blue}[+] {url}\t --> {colors.green}{status}{colors.reset}"
                                    )
                                if output != "":
                                    outputfunc(output, f"{url}\t --> {status}")
                            except Exception as err:
                                if "timed out" in str(err):
                                    err = "Connection Time Out"
                                if output != "":
                                    outputfunc(output, f"{url}\t --> {err}")
                                print(
                                    f"{colors.red}[+] {url}\t --> {colors.red}{err}{colors.reset}"
                                )
                            time.sleep(0.5)
                except KeyboardInterrupt:
                    exit_program()

                except Exception as err:
                    print(f"{colors.red}[-] Something Went Wrong\n[!] {err}")


def password_gen(
    upper=True, lower=True, digit=True, punctuation=True, length="8", check=True
):
        banner.main()
        banner.attack("Password Generators")
        ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
        ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        string_digits = "0123456789"
        string_punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        main_password = ""
        if upper:
            main_password += ascii_uppercase
        if lower:
            main_password += ascii_lowercase
        if digit:
            main_password += string_digits
        if punctuation:
            main_password += string_punctuation
        try:
            result_str = "".join(random.choice(main_password) for i in range(int(length)))
            print(
                f"{colors.blue}[+] Your Passwrod Is: {colors.green}{result_str}{colors.reset}"
            )
            if check:
                checking(result_str)
        except KeyboardInterrupt:
                exit_program()
        except IndexError:
            print(
                f"{colors.red}[-] Please Specify atleast one argument (--upper,--lower,--digits,--punctuation) {colors.reset}"
            )
def generate_wordlist(characters=True, min_length=True, max_length=True, output_file=True):
    try:
        with open(output_file, 'w') as file:

            for length in range(min_length, max_length + 1):

                for combination in itertools.product(characters, repeat=length):

                    word = ''.join(combination)
                    file.write(word + '\n')
        print(f"[+] Wordlist generated and saved to {output_file}.txt")
    except KeyboardInterrupt:
                exit_program()
def remove_dublicates(location,output=''):
        f=open(location,'r')
        lines=f.read()
        lines=lines.split('\n')
        readed=[]
        for line in lines:
            if line not in readed:
                readed.append(line)
        f.close()
        if output=='':
            if not os.path.isdir("duplicate"):
                os.system("mkdir duplicate")
            location=location.split('.')
            location=location[0].split('/')
            fn=open(f"duplicate/{location[(len(location)-1)]}_removed.txt",'a')
            for read in readed:
                fn.write(read)
                fn.write('\n')
            fn.close()
        else:
            location=location.split('.')
            location=location[0].split('/')
            fn=open(f'{output}',"a")
            for read in readed:
                fn.write(read)
                fn.write('\n')
            fn.close()


        

def screenshot(path="", url="",output=''):
        link=domain()['check_http'](url)
        banner.main()
        banner.attack("Screenshotting")
        if link=="ip":
            print(f'{colors.red}Something Went Wrong\n[!] You Have Entered IP{colors.reset}')
            return
        else:
            if path != "":
                try:
                    f = open(path, "r")
                    urls = f.read()
                    urls = urls.split("\n")
                    for url in urls:
                        if url != "":
                            link=domain()['check_http'](url)
                            if link=="ip":
                                print(
                                        f"{colors.red}[-] {url}\t --> {colors.red}It Is a IP{colors.reset}"
                                    )
                            else:
                                for url in link:
                                    driver_path = "main/tools/.driver/geckodriver"
                                    firefox_options = webdriver.FirefoxOptions()
                                    firefox_options.headless = True
                                    driver = webdriver.Firefox(
                                        executable_path=driver_path, options=firefox_options
                                    )
                                    try:
                                        driver.get(url)
                                        url_new = url.split("//")
                                        path = os.getcwd()
                                        if output!='':
                                            screenshot_filename=f'{output}/{url_new[0]}_{url_new[1].replace("/","_")}.png'
                                        else:
                                            if not os.path.isdir("Screenshot"):
                                                os.system("mkdir Screenshot")
                                            screenshot_filename = f'{path}/Screenshot/{url_new[0]}_{url_new[1].replace("/","_")}.png'
                                        driver.save_screenshot(screenshot_filename)
                                        print(
                                            f"{colors.blue}[+] {url}\t --> {colors.green}Screenshot saved to {screenshot_filename}{colors.reset}"
                                        )
                                        driver.quit()
                                    except KeyboardInterrupt:
                                        exit_program()
                                    except Exception as err:
                                        print(
                                            f"{colors.red}[+] {url}\t --> {colors.red}Something Went Wrong\n[!] {err}{colors.reset}"
                                        )
                                    time.sleep(0.5)
                except Exception as err:
                    print(
                        f"{colors.red}[-] Something Went Wrong\n[!] {err}\n[!] Check Your File location"
                    )
            else:
                driver_path = "./main/tools/.driver/geckodriver"
                firefox_options = webdriver.FirefoxOptions()
                firefox_options.headless = True
                driver = webdriver.Firefox(executable_path=driver_path, options=firefox_options)
                for url in link:
                    try:
                        driver.get(url)
                        url_new = url.split("//")
                        path = os.getcwd()
                        if output!='':
                            if not os.path.isdir(output):
                                os.mkdir(output)
                            screenshot_filename=f'{output}/{url_new[0]}_{url_new[1].replace("/","_")}.png'
                        else:
                            if not os.path.isdir("Screenshot"):
                                os.system("mkdir Screenshot")
                            screenshot_filename = f'{path}/Screenshot/{url_new[0]}_{url_new[1].replace("/","_")}.png'
                        if not os.path.isdir("Screenshot"):
                            os.system("mkdir Screenshot")
                        driver.save_screenshot(screenshot_filename)
                        print(
                            f"{colors.blue}[+] {url}\t --> {colors.green}Screenshot saved to {screenshot_filename}{colors.reset}"
                        )
                        #driver.quit()
                        #time.sleep(5)
                    except KeyboardInterrupt:
                        exit_program()
                    except Exception as err:
                        print(
                            f"{colors.red}[+] {url}\t --> {colors.red}Something Went Wrong\n[!] {err}{colors.reset}"
                        )
                    time.sleep(0.5)
                driver.quit()
def domain():
    def check_http(url):
        urls=[]
        if "https://" not in url and "http://" not in url:
            valid=ip_valid(url)
            if valid==3:
                urls.append("http://"+url)
                urls.append("https://"+url)
            else:
                urls="ip"
        else:
            urls.append(url)
        return urls
    def no_http(url):
        if "http://" and "https://" not in url:
            valid=ip_valid(url)
            if valid==3:
                return url
            else:
                url="ip"
        else:
            if "http://" in url:
                url=url.split("http://")
                url=url[1]
            elif "https://" in url:
                url=url.split("https://")
                url=url[1]

            return url
    return {"check_http":check_http,"no_http":no_http}

def ip_valid(user_input):
    parts = user_input.split(".")
    for part in parts:
        try:
            part=int(part)
            if len(parts) == 4:
                is_ip_address = True
                for part in parts:
                    if not part.isdigit() or not (0 <= int(part) <= 255):
                        is_ip_address = False
                        break
                if is_ip_address:
                    return 1
                else:
                    return 2
        except:
            return 3
