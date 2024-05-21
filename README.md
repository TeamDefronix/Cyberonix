<div align="center"><p>
    <h1>CYBERONIX</h1>
    <img style="filter: brightness(200%)" src="https://user-images.githubusercontent.com/122822828/216810369-34904b5a-d063-48a9-a87d-11caf293243b.png" width="50%"><br>
    <img src="https://forthebadge.com/images/badges/made-with-python.svg">
    <img src="https://forthebadge.com/images/badges/built-with-love.svg">
    <br><br>
    <a href="https://github.com/TeamDefronix/Cyberonix/releases/latest">
      <img alt="Latest release" src="https://img.shields.io/github/v/release/TeamDefronix/Cyberonix?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/TeamDefronix/Cyberonix/pulse">
      <img alt="Last commit" src="https://img.shields.io/github/last-commit/TeamDefronix/Cyberonix?style=for-the-badge&logo=starship&color=8bd5ca&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/TeamDefronix/Cyberonix/blob/main/LICENSE">
      <img alt="License" src="https://img.shields.io/github/license/TeamDefronix/Cyberonix?style=for-the-badge&logo=starship&color=ee999f&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/TeamDefronix/Cyberonix/stargazers">
      <img alt="Stars" src="https://img.shields.io/github/stars/TeamDefronix/Cyberonix?style=for-the-badge&logo=starship&color=c69ff5&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/TeamDefronix/Cyberonix/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/TeamDefronix/Cyberonix?style=for-the-badge&logo=bilibili&color=F5E0DC&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/TeamDefronix/Cyberonix">
        <img alt="Repo Size" src="https://img.shields.io/github/repo-size/TeamDefronix/Cyberonix?color=%23DDB6F2&label=SIZE&logo=codesandbox&style=for-the-badge&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://twitter.com/intent/follow?screen_name=niteshlike123">
      <img alt="follow on Twitter" src="https://img.shields.io/twitter/follow/niteshlike123?style=for-the-badge&logo=twitter&color=8aadf3&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://discord.gg/defronix">
      <img alt="Discord" src="https://img.shields.io/discord/1072407436348112896?style=for-the-badge&logo=starship&color=c69ff5&logoColor=D9E0EE&labelColor=302D41"/>
    </a>
  </p>
  <p align="center">
    <img src="https://stars.medv.io/TeamDefronix/Cyberonix.svg", title="commits"/>
  </p>

<h1 align="left">Description</h1>

<p align="left">
    Cyberonix is an open-source and free tool developed by Team Defronix Cyber Security Pvt. Ltd. Initially created by a team of students during their internship at Defronix after completing their Diploma in Cyber Security Training. </p>

<p align="left"> This tool serves as a comprehensive resource hub for the Cyber Security Community. Our objective is to establish it as a one-stop solution for hackers, providing resources on various topics within Cyber Security. We are committed to regularly updating the tool and incorporating new and relevant resources.</p>

<p align="left"> Please feel free to suggest any features you would like to see in this tool, we welcome your input and will be delighted to include suggested features in our upcoming updates. 
</p>

---

**[<kbd> <br> Install <br> </kbd>][Install]** 
**[<kbd> <br> Usage <br> </kbd>][Usage]** 
**[<kbd> <br> Categories <br> </kbd>][Categories]** 
**[<kbd> <br> ScreenShots <br> </kbd>][ScreenShots]** 
**[<kbd> <br> Contributors <br> </kbd>][Contributors]**

---

[Categories]: #Categories
[Install]: #Installation
[ScreenShots]: #ScreenShots
[Contributors]: #Contributors
[Usage]: #Usage

</div>

# Installation

1. Update your system packages:

```shell script
sudo apt update -y && apt full-upgrade -y
```

2. Clone the Cyberonix repository from GitHub:

```shell script
git clone https://github.com/TeamDefronix/Cyberonix.git
```

3. Navigate to the Cyberonix directory:

```shell script
cd Cyberonix
```

4. Make the setup script executable:

```shell script
chmod +x setup.py
```

5. Run the setup script using Python3:

```shell script
sudo python3 setup.py
```

6. Execute Cyberonix:

```shell script
cyberonix
```

## PIP intallation

```shell script
pip install cyberonix
```

If you encounter the "Externally-Managed-Environment" issue on your machine, please refer to our blog for a solution. You can find detailed information and steps to resolve this problem by clicking <a href="https://technicalnavigator.in/how-to-fix-error-externally-managed-environment-in-python-kali-linux/" target="_blank">here</a>.

# Usage

- To display the help menu, use the following command: `cyberonix -h`

- To exit the Cyberonix tool, press: `ctrl+c`

- Press the `enter` key to navigate back.

Below are the instructions to access the tool's help function, along with a complete list of all available switches:

```console
Welcome to Cyberonix - Your Cyber Security Resource Hub!

Basic Options:

  -h, --help                  : Get this help message.
  --domain DOMAIN, -D DOMAIN   : Target a specific domain.
  --output OUTPUT, -o OUTPUT   : Save results to a file (provide the file path).
  --file FILE, -f FILE         : Read input from a file (provide the file path).
  --ip IP, -ip IP             : Target a specific IP address.

Main Functions:

  --tools, -t                 : Access various cybersecurity tools.
  --cheatsheet, -c            : Get a cybersecurity reference guide.

IP Operations:

  --getip, -gip               : Get the IP address of a domain.
  
  Can use with: --domain, --file, --output

  --ipinfo, -ipi              : Get information about an IP address.

  Can use with: --ip, --file, --output

DNS Operations:

  --dnsrecord, -dns           : Get DNS records for a domain.

  Can use with: --domain, --file, --output

  --record RECORD, -r RECORD   : Specify the type of DNS record (e.g., A, TXT, MX).

  usage: --record <type>

ASN Record:

  --asnrecord, -asn           : Get ASN (network) information.

  Can use with: --ip, --file, --output

Screenshoting:

  --screenshot, -s            : Take a website screenshot.

  Can use with: --domain, --file, --output

HTTP Status:

  --http-status, -S           : Check a website's HTTP status code.

  Can use with: --domain, --file, --output

Remove Duplicate:

  --remove-duplicate, -rd     : Remove duplicate lines from a file.

  Can use with: --file, --output

Password Generation:

  --passwordgen, -P           : Generate a secure password.
  --default-password-gen, -pass: Generate a strong random password (recommended).

  Customization Options:

  --upper, -u                 : Include uppercase letters.
  --lower, -l                 : Include lowercase letters.
  --digits, -d                : Include numbers.
  --punctuation, -p           : Include symbols.
  --length LENGTH, -L LENGTH   : Set password length (default is 8).
  --checkpassword, -C         : Test the strength of a password.

Worlist Generation:

  --worlist, -w                : To generate a wordlist
  --characters,-c              : Set of characters to include in the wordlist (Default = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 )
  --min_length, -min           : Minimum length of the words  ( Default = 4 )
  --max_length, -max           : Maximum length of the words  ( Default = 6 )
  --output_file, -ot           : Output file name   ( Default = custom_wordlist.txt )
```

# Categories

- ## Tools

<div align="center">

### `Information Gathering`

| Tool Name | Tool Name                                   | Tool Name  |
| ------- | --------------------------------------------- | ------ |
| Useful Websites    | Nmap | Subfinder |
| Maltego    | Dracnmap | Red_Hawk |
| Th3Inspector    | Hping3 | Arping |
| Netdiscover    | The Harvester | Wafw00f |
| Recon-Ng    | Sublist3R | Spiderfoot |
| Amass    |  |  |

### `Vulnerability Analysis`

| Tool Name | Tool Name                                   | Tool Name  |
| ------- | --------------------------------------------- | ------ |
| Wpscan    | Wireshark | Wapiti |
| Nmap    | Legion | Nikto |
| Wfuzz    |  |  |

### `Web Application Analysis`

| Tool Name | Tool Name                                   | Tool Name  |
| ------- | --------------------------------------------- | ------ |
| Burp Suite    | Dirsearch | Owasp Zap |
| Dirbuster    | Nikto | Wapiti |
| Nessus    | Dirb | Nuclei |
| Ffuf    |  |  |

### `Password Attacks`


 #### _Brute Force Attacks_

| Tool Name | Tool Name                                   |  Tool Name |
| ------- | --------------------------------------------- | ------ |
| Hashcat    | John The Ripper | Hydra |
| Johnny (GUI John)    | Brutus | Dirbuster |
| Reaver    | Dirsearch |  |

 #### _Dicitionary Attacks_

| Tool Name | Tool Name                                   |  Tool Name |
| ------- | --------------------------------------------- | ------ |
| Hashcat    | John The Ripper | Hydra |
| Medusa    | Ncrack | Johnny (GUI John) |

 #### _Rainbow Table Attacks_

| Tool Name |              Tool Name                      |
| ------- | --------------------------------------------- |
| Rainbowcrack    | Ophcrack |

 #### _Wordlist Generator_

| Tool Name | Tool Name                                   | Tool Name  |
| ------- | --------------------------------------------- | ------ |
| Crunch    | Cupp | Bopscrk |

 #### _Phishing Attacks_

| Tool Name | Tool Name                                   |  Tool Name |
| ------- | --------------------------------------------- | ------ |
| Social-Engineer Toolkit (SET)    | Hiddeneye | R3Bu5 |
| Zphisher    | Shellphish | Gophish (GUI) |
| Camphish    |  |  |

 #### _Keylogger Attacks_

| Tool Name |              Tool Name                      |
| ------- | --------------------------------------------- |
| Zlogger    | Keylogger |

### `Wireless Attacks`

| Tool Name | Tool Name                                   | Tool Name  |
| ------- | --------------------------------------------- | ------ |
| Kismet    | Wifite | Fern Wifi Cracker |
| Aircrack-Ng    | Fluxion | Wifiphisher |

### `Exploitation Tools`

| Tool Name | Tool Name                                   |  Tool Name |
| ------- | --------------------------------------------- | ------ |
| Metasploit    | Crackmapexec | Searchsploit |
| Beef    | Routersploit | Sqlmap |
| Seclists    | Airmitage |  |

### `Sniffing And Spoofing`

| Tool Name | Tool Name                                   |  Tool Name |
| ------- | --------------------------------------------- | ------ |
| Wireshark    | Bettercap | Tcpdump |
| Arpspoof    | Dsniff | Scapy |
| Netsniff-Ng    | Macchanger | Responder |
| Airgeddon    | Sharesniffer | Wifi-Pumpkin-3 |
| Mitmproxy    | Zaproxy |  |


### `Post Exploitation`
 
|      Tool Name                      | Tool Name                           |               Tool Name             |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| Metasploit-Framework                | Linpeas                             | Linenum                             |
| Sudo Killer                         | Beroot                              | Linux Exploit Suggester 2           |
| LSE (Linux Smart Enumeration)       | Pspy                                | Bashark                             |
| Linux Private-I                     | Shellter                            | Amber                               |
| Upx (Ultimate Packer for Executable) | Covermyass                          |                                     |


### `Anonymity`
   
|  Tool Name | Tool Name   |  Tool Name  |
|------------|-------------|-------------|
| Tor        | Anonsurf    | Nipe         |
| Proxychain |         |             |

### `Framework`

| Tool Name  | Tool Name   | 
|------------|-------------|
| OSINT Framework        | MITRE Framework    |


### `Pentesting And Bug-Bounty`

 #### _Information Gathering_

| Tool Name | Tool Name                                   |  Tool Name |
| ------- | --------------------------------------------- | ------ |
| Useful Websites    | Nmap | Subfinder |
| Maltego    | Dracnmap | Red_Hawk |
| Th3Inspector    | Hping3 | Arping |
| Netdiscover    | The Harvester | Wafw00f |
| Recon-Ng    | Sublist3R | Spiderfoot |
| Amass    |  |  |

 #### _Configuration Management_

 |   Tool Name    | Tool Name       |   Tool Name     |
|----------------|-----------------|-----------------|
| Dirb           | gobuster        | Nikto           |
| Wfuzz          | Skipfish        | Dirbuster       |
| Feroxbuster    | Nmap            | Httpie          |
| Metasploit     | Securityheaders | Sqlmap          |
| Trufflehog     | Gitleaks        | Secretfinder    |

 #### _Secure Transmission_

| Writeups                                       |   Writeups                                    |
|-------------------------------------------------|------------------------------------------------|
| Check SSL Version, Algorithms, Key Length        | Check for Digital Certificate Validity         |
| Check Credentials Only Delivered Over HTTPS      | Check Session Tokens Only Delivered Over HTTPS |
| Check if HTTP Strict Transport Security (HSTS)   |                                                |

 #### _Authentication_

|        Writeups                   | Writeups                               |     Writeups                           |
|------------------------------------|-----------------------------------------|-----------------------------------------|
| User Enumeration                   | Authentication Bypass                   | Vulnerable Remember Me Functionality    |
| Password Reset                     | Captcha Bypass                          | Autocomplete On                         |
| Multifactor Authentication         | Logout Functionality                    | Cache Management                        |
| Default Credentials                |                                         |                                         |


 #### _Session Management_

|            Tool Name               | Tool Name                           |            Tool Name               |
|-------------------------------------|-------------------------------------|-------------------------------------|
| OWASP Zap                           | BurpSuite                           | Nikto                               |
| Nmap                                | Wapiti                              | Nessus                              |
| Nuclei                              | Fiddler                             | Penetration Testers Framework (PTF)|

 #### _Authorization_

|           Tool Name                | Tool Name                           |         Tool Name                  |
|-------------------------------------|-------------------------------------|-------------------------------------|
| BurpSuite                           | Wireshark                           | OWASP Zap                           |
| Nessus                              | Hydra                               | Beef                                |
| Sqlmap                              | Metasploit                          | Nmap                                |
| Penetration Testers Framework (PTF) |                                     |                                     |

 #### _Data Validation_

|      Tool Name              | Tool Name                    |         Tool Name            |
|------------------------------|------------------------------|------------------------------|
| XSS                          | XXE - XML                    | HTML Injection               |
| SQL Injection                | Command Injection            | HTTP Smuggling               |
| HTTP Parameter Pollution     | Open Redirection             | LFI                          |

 #### _Denial Of Service_

| Tool Name         |      Tool Name    |
|--------------------|--------------------|
| Goldeneye          | Slowhttptest       |
| Thc-SSL-Dos        | Slowloris          |

 #### _Business Logic_

| Writeups                                      |     Writeups                                  |
|------------------------------------------------|------------------------------------------------|
| Business Logic                                 | Exploiting Business Logic Vulnerabilities      |
| Web Application — Business Logic Vulnerabilities | Business Logic Flaw                            |

 #### _Cryptography_

|  Tool Name  | Tool Name        |   Tool Name    |
|-------------|------------------|----------------|
| SSLstrip    | Bettercap        | Ettercap        |
| SSLyze      | 0-Saft           | SSLscan        |
| SSLLabs     |                  |                |

 #### _Risky Functionality - File Uploads_

| Tool Name                                      |       Tool Name                                |
|------------------------------------------------|------------------------------------------------|
| Fuxploider                                 | Upload Scanner      |

 #### _Risky Functionality - Card Payment_

|       Tool Name                    | Tool Name                           |           Tool Name                 |
|-------------------------------------|-------------------------------------|-------------------------------------|
| BurpSuite                           | Wireshark                           | OWASP Zap                           |
| Nessus                              | SQLmap                              | Fiddler                             |
| Metasploit                          | Nmap                                | Penetration Testers Framework (PTF)|

 #### _Html 5_

|     Writeups        | Writeups                   |        Writeups        |
|-----------------------|-----------------------------|-------------------------|
| Web Messaging         | Web Storage SQL Injection   | CORS Implementation     |

</div>

- ## Cheatsheets

  - [Nmap](https://www.tutorialspoint.com/nmap-cheat-sheet)
  - [Maltego](https://static.maltego.com/cdn/Case%20studies/Building-Integrations-for-Maltego-Cheat-Sheet.pdf)
  - [Hping3](https://cyberwar.nl/d/cheatsheets/hping3_cheatsheet_v1.0-ENG.pdf)
  - [Netdiscover](https://linuxcommandlibrary.com/man/netdiscover)
  - [Wafw00F](#)
  - [Metasploit-Framework](https://cdn.comparitech.com/wp-content/uploads/2019/06/Metasploit-Cheat-Sheet-1.webp)
  - [Wireshark](https://www.stationx.net/wireshark-cheat-sheet/) 
  - [Bettercap](https://www.bettercap.org/usage/interactive/)
  - [Tcpdump](#)
  - [Scapy](#)
  - [Responder](https://www.ivoidwarranties.tech/posts/pentesting-tuts/responder/cheatsheet/)
  - [Airgeddon](https://liodeus.github.io/2020/10/29/OSWP-personal-cheatsheet.html#airgeddon) 
  - [Wpscan](https://linuxcommandlibrary.com/man/wpscan)
  - [Wapiti](https://wapiti.limsi.fr/manual.html)
  - [Legion](https://theory.stanford.edu/~aiken/LegionRetreat21/slides/Tools.pdf)
  - [Nikto](https://cdn.comparitech.com/wp-content/uploads/2019/07/NIkto-Cheat-Sheet.pdf)
  - [Burp Suite](https://portswigger.net/burp/documentation/desktop)
  - [Owasp Zap](#)
  - [Nessus](https://limberduck.github.io/nessus-cheat-sheet/nessus-cheat-sheet.pdf)
  - [Dirb](https://manpages.debian.org/unstable/dirb/dirb.1.en.html)
  - [Skipfish](https://linux.die.net/man/1/skipfish)
  - [Nuclei](https://cheatsheet.haax.fr/web-pentest/tools/nuclei/)
  - [Wifite](https://cheatography.com/socket23/cheat-sheets/wifite/)
  - [Aircrack-Ng](#)

- ## Certifications & Roadmap
  - ### Beginner Level Certifications

    - [CEH](https://www.eccouncil.org/)
    - [C|PENT](https://www.eccouncil.org/)
    - [C|HFI](https://www.eccouncil.org/)
    - [CompTIA+](https://www.comptia.org/certifications/a)
    - [CompTIA Linux+](https://www.comptia.org/certifications/linux)
    - [CompTIA Network+](https://www.comptia.org/certifications/network)
    - [CompTIA Security+](https://www.comptia.org/certifications/security)
    - [CCNA](https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html)
    - [DDFS](https://defronix.com/digital-forensics-mastery/)

  - ### Advance Level Certifications
    - [DCSP](https://defronix.com/)
    - [CISSP](https://www.cissp.com/)
    - [OSCP](https://www.offsec.com/courses/pen-200/)
    - [OSWE](https://www.offsec.com/courses/web-300/)

- ## Bug Bounty

  - Bug Bounty for Beginners
  - Reconnaissance
  - Intel Discovery
  - Enumeration
  - Vulnerability Analysis
  - Exploitation
  - Reporting
  
# Screenshots

## ![Main Menu](https://imgur.com/e2b26Mf.png)

## ![Bug Bounty](https://imgur.com/Sa4fdLU.png)

## ![Tools](https://imgur.com/3pc76rB.png)

## ![Information Gathering](https://imgur.com/f1jai90.png)

![Nmap](https://imgur.com/CoYpmNC.png)

<h1 align="left">Socials</h1>

<p align="left">
<a href="https://github.com/TeamDefronix"><img src="https://user-images.githubusercontent.com/696094/196835284-c52d4bd1-7034-439e-848b-47d4f2933dff.svg" width="64" height="64" alt="Github Logo"/></a> <img src="assets/misc/transparent.png" height="1" width="5"/> <a href="https://discord.gg/defronix"><img src="https://user-images.githubusercontent.com/696094/196835282-f5c47d66-29b7-4210-9ee0-d9cdecde3559.svg" width="64" height="64" alt="Discord Logo"/></a> <img src="assets/misc/transparent.png" height="1" width="5"/> <a href="https://twitter.com/niteshlike123"><img src="https://user-images.githubusercontent.com/696094/196835281-52617611-ede6-40da-a4bc-8c5025622bbf.svg" width="64" height="64" alt="Twitter Logo"/></a> <img src="assets/misc/transparent.png" height="1" width="5"/><a href="https://twitter.com/niteshlike123"> <img src="https://user-images.githubusercontent.com/696094/196835281-52617611-ede6-40da-a4bc-8c5025622bbf.svg" width="64" height="64" alt="Facebook Logo"/></a> <img src="assets/misc/transparent.png" height="1" width="5"/>
</p>

<h1 align="left">Support</h1>

<p><a href="https://www.buymeacoffee.com/metaxone" target="_blank"> <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="Buymeacoffee" /></a></p><br><br><br>
<p><a href="https://paypal.me/niteshsinghhacker" target="_blank"> <img align="left" src="https://raw.githubusercontent.com/andreostrovsky/donate-with-paypal/master/blue.svg" height="70" width="210" alt="Donate with paypal" /></a></p><br><br><br>
<p><a href="https://tools.apgy.in/upi/Nitesh+Singh/niteshkumar5@ybl/" target="_blank"> <img align="left" style="border-radius:8px" src="https://user-images.githubusercontent.com/122822828/216837693-3480fcd2-b4fc-40ff-94f8-c5d7d4b82ad5.png" height="50" width="210" alt="Donate with paypal" /></a></p><br><br><br>
<p><a href="https://razorpay.me/@technicalnavigator" target="_blank"> <img align="left" src="https://user-images.githubusercontent.com/122822828/216838288-a946ef91-f215-4286-926f-afa71d0c3760.png" height="50" width="210" alt="Donate with paypal" /></a></p><br><br>

<div align="center">
    <h1 id="Contributors">Thanks To All Contributors</h1>

<a href="https://github.com/TeamDefronix/Cyberonix/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=TeamDefronix/Cyberonix" />
</a>
</div>
