#!/usr/bin/python3
# This Programm write by Mr.nope
# ░▒▓█ Make-Tool █▓▒░ 1.4.1
import os
from time import sleep
import sys
import webbrowser
from platform import uname
from types import CodeType
try:
    from colorama import Fore,init
except ImportError:
    os.system("pip3 install colorama")
system = uname()[0]
End = '\033[0m'
help = """
version
help
developer
"""
opt = "\nPress Enter To " + Fore.GREEN + "Start..." + End
opt_2 = Fore.YELLOW + "\nEnter Project Name: " + End
Make_File_Version = "1.4.1"
banner = Fore.CYAN + """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░
░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░
░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░
░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░
░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░
░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░
░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░   """ + Fore.RED + "Ok, " + Fore.LIGHTBLUE_EX + "Please Enter name...!" + End + Fore.CYAN + """
░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░
░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░  """ + Fore.BLUE + "Usage: " + Fore.RED + "help " + Fore.BLUE + "for Read " + Fore.GREEN + "Command" + Fore.CYAN + """
░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░
░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░
░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░
░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░
░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░
░░░░█░░░░░░░░░░░░░░░░░░░░░█░░
░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░
░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""" + End
def title():
    if system == 'Linux':
        os.system("xtitle Make-Tool")
    elif system == 'Windows':
        os.system("title Make-Tool")
    else:
        print("\nPlease, Run This Programm on Windows, Linux or MacOS!\n")
        sys.exit()
def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print("\nPlease, Run This Programm on Windows, Linux or MacOS!\n")
        sys.exit()
def main():
    title()
    cls()
    print(banner)
    file_name = input(opt_2)
    if file_name == '':
        main()
    elif file_name == 'help':
        print(help)
        try2()
    elif file_name == 'version':
        print(Make_File_Version)
        try2()
    elif file_name == 'developer':
        print("\nThis Programm write by Mr.nope\n")
        print("Open Github...\n")
        sleep(2)
        webbrowser.open_new_tab("https://github.com/mrprogrammer2938")
        print("\n----------------")
        try2()
    else:
        return start(file_name)
def start(file_):
    print("\n--------------------\n")
    sleep(1)
    print("\nLevel 1\n")
    sleep(0.50)
    file = open("run.py","w")
    file.write("""
#!/usr/bin/python3
# Version 1.0

'''
Imports
'''

from modules import banner,argument
from Core import programm

import os
import time
import sys
import subprocess
import socket
import platform

opt = "choose/> "

def main():
    # Edit Code
    argument.arg()
    os.system("clear")
    print(banner.banner)
    print("{1}.Start")
    print("{99}.Exit")
    choose = input(opt)
    if choose == '1':
        print("Start")
        sys.exit()
        # Code
    elif choose == '99':
        print("Exiting...")
        sys.exit()
        # Code
    else:
        main()
# Enter Code
if __name__ == '__main__':
    try:
        main()
    except IndexError:
        print("Usage: --start")
        # Code
        sys.exit()""")
    file.close()
    file_2 = open("banner.py","w")
    file_2.write("""
#!/usr/bin/python3

import os, time

banner = "banner"
""")
    file_2.close()
    file_3 = open("argument.py","w")
    file_3.write("""
#!/usr/bin/python3

import sys

def arg():
    if sys.argv[1] == '--start':
        pass
    else:
        print("Please, Check Argument")
        sys.exit()
        """)  
    file_3.close()
    file_4 = open("programm.py","w")
    file_4.write("""
# Code
""")
    file_4.close()
    if system == 'Linux':
        os.system("mkdir " + file_)
        os.system(f"cd {file_} && mkdir modules && mkdir Core")
        os.system(f"mv run.py {file_}/ && mv banner.py {file_}/modules && mv programm.py {file_}/Core && mv argument.py {file_}/modules")
        print(f'File: {file_} Created!\n')
        try1()
    elif system == 'Windows':
        os.system("mkdir " + file_)
        os.system(f"cd {file_} && mkdir modules && mkdir Core")
        os.system(f"move run.py {file_}/ && move banner.py {file_}/modules && move programm.py {file_}/Core && move argument.py {file_}/modules")
        print(f'File: {file_} Created!\n')
    else:
        print("\nSorry, Please Run This Programm on Windows, Linux or MacOS!\n")
        sys.exit()
def try1():
    print("\nOk, Have Nice Day ;)\n")
    sys.exit()
def try2():
    try_to_menu = input("\npress Enter...")
    if try_to_menu == '':
        main()
    else:
        main()
if __name__ == '__main__':
    try:
        try:
            if os.getuid() != 0:
                print("\nPlease, Run This Programm as Root!")
            else:
                main()
        except EOFError:
            print("\nCtrl + D")
            print("\nExiting...")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nExiting...")
        sys.exit()
