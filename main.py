from sys import exit
from os import _exit
import subprocess


from os import path
import urllib
import request
import requests

from colorama import Fore, init
from libs.logo import print_logo
from libs.utils import print_success
from libs.utils import print_error
import time
from libs.utils import ask_question
import os
from libs.utils import print_status
from libs.utils import parse_proxy_file
from libs.proxy_harvester import find_proxies
from libs.attack import report_profile_attack
from libs.attack import report_video_attack

from multiprocessing import Process
from colorama import Fore, Back, Style

init(convert=True)

content = urllib.request.urlopen("AUTH_API (AUTH.GG)")

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def profile_attack_process(username, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_profile_attack(username, None)
        return

    for proxy in proxy_list:
        report_profile_attack(username, proxy)

def video_attack_process(video_url, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_video_attack(video_url, None)
        return

    for proxy in proxy_list:
        report_video_attack(video_url, proxy)

def video_attack(proxies):
    video_url = ask_question("Enter the link of the video you want to report")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=video_attack_process, args=(video_url, [],))
            p.start()
            print_status(str(k + 1) + ". Transaction Opened!")
            if (k == 5): print()
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Video complaint attack is on!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=video_attack_process, args=(video_url, proxy_list,))
        p.start()
        print_status(str(i) + ". Transaction Opened!")
        if (k == 5): print()
        i = i + 1

def GetUUID():
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n") + 2
    uuid = uuid[pos1:-15]
    return uuid.encode("utf-8")


def hwid():
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n") + 2
    uuid = uuid[pos1:-15]
    return uuid


def profile_attack(proxies):
    username = ask_question("Enter the username of the person you want to report")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=profile_attack_process, args=(username, [],))
            p.start()
            print_status(str(k + 1) + ". Transaction Opened!")
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Profile complaint attack is starting!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=profile_attack_process, args=(username, proxy_list,))
        p.start()
        print_status(str(i) + ". Transaction Opened!")
        if (k == 5): print()
        i = i + 1

def check():
    os.system('title Starting...')
    print(Fore.MAGENTA + '[ TRY ] ' + Fore.WHITE + 'Request to AUTH.GG/ID' + '"' + str(hwid()) + '"')
    print(" ")
    a = content.read()
    b = GetUUID()
    time.sleep(1)
    if b in a:
        print(Fore.LIGHTGREEN_EX + '[ SUCCESS ] ' + Fore.WHITE + 'HWID FOUND')
        time.sleep(2)
        main()
    else:
        print(Fore.LIGHTRED_EX + '[ ERROR ] ' + Fore.WHITE + 'We can''t find your HWID in our database. Please join: discord')
        print(Fore.LIGHTYELLOW_EX + '[ INFO ] ' + Fore.WHITE + 'Your HWID: ' + str(hwid()))
        os.system('PAUSE')




def main():
    os.system('title Instagram Mass Report ^| Developed by Martizio ^| V1')
    print(Fore.MAGENTA + '[ TRY ] ' + Fore.WHITE + 'Load API...')
    print(" ")
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + '[ SUCCESS ] ' + Fore.WHITE + 'Requests API Loaded !')
    time.sleep(0.9)
    print(Fore.LIGHTGREEN_EX + '[ SUCCESS ] ' + Fore.WHITE + 'Facebook API Loaded !')
    print(" ")
    print(" ")
    print(" ")

    proxies = []

    print(Fore.MAGENTA + '[ TRY ] ' + Fore.WHITE + 'Scrape Proxys from API')
    print(" ")
    print(" ")

    rfinder = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=7000&country=ALL&anonymity=elite&ssl=no')
    LISTPROXY = rfinder.text
    proxies = str(LISTPROXY)
    

    print_success(str(len(proxies)) + " Number of proxy found!\n")


    

    print("")
    print(Fore.LIGHTMAGENTA_EX + "[ CHOOSE ] " + Fore.WHITE + "1 - Report Profile")
    print(Fore.LIGHTMAGENTA_EX + "[ CHOOSE ] " + Fore.WHITE + "1 - Report a video")
    print(" ")

    report_choice = input(Fore.WHITE + "Choose option : ")
    print("")

    if (report_choice.isdigit() == False):
        print_error("The answer is not understood.")
        exit(0)
    
    if (int(report_choice) > 2 or int(report_choice) == 0):
        print_error("The answer is not understood.")
        exit(0)

    if (int(report_choice) == 1):
        profile_attack(proxies)
    elif (int(report_choice) == 2):
        video_attack(proxies)

if __name__ == "__main__":
    print_logo()
    try:
        check()
        print(Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "[*] Program is closing!")
        print(Style.RESET_ALL)
        _exit(0)
