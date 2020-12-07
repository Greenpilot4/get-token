from colorama import Fore, init
from os import system
import platform
import requests
import sys

os = platform.system()
if os == "Windows":
    init()


def main():
    if os == "Windows":
        system("cls")
    else:
        system("clear")
    print(Fore.LIGHTRED_EX + """\n
    ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝             
    """ + Fore.LIGHTYELLOW_EX)

    email = str(input("Email: "))
    password = str(input("Password: "))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    }
    account = {
        "email": email,
        "password": password
    }
    r = requests.post('https://discord.com/api/v8/auth/login', headers=headers, json=account).json()
    if "errors" in r:
        print(Fore.RED + "\nInvalid credentials provided.")
    elif "captcha_key" in r:
        print(Fore.RED + "You've trigged a captcha.")
    elif r["token"] == None:
        mfa(r, headers)
    else:
        print(Fore.CYAN + "Token is: " + r["token"])
        sys.exit()


def mfa(r, headers):
    code = input("\n2 Factor code: ")
    mfa_code = {
        "code": code,
        "ticket": r["ticket"]
    }
    r2 = requests.post('https://discord.com/api/v8/auth/mfa/totp', headers=headers, json=mfa_code).json()
    if "message" in r2:
        print(Fore.RED + "\nInvalid code provided." + Fore.RESET)
    else:
        print(Fore.CYAN + "Token is: " + r2["token"])
        sys.exit()


main()
