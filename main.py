import random
import string
import sys
import time
import colorama
from colorama import Fore
from termcolor import colored
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def servers():
    server = ["DENMARK-1", "DENMARK-2", "JAPAN-1","JAPAN-2","RUSSIA-1","RUSSIA-2","USA-1","USA-2","CZECHIA-1","CZECHIA-2","SLOVAKIA-1","SLOVAKIA-2","MOLDAVIA-1","MOLDAVIA-2","ROMANIA-1","ROMANIA-2","GERMANY-1","GERMANY-2","POLAND-1","POLAND-2","FINNLAND-1","FINNLAND-2","SWITZERLAND-1","SWITZERLAND-2"]
    final_server = random.choice(server)
    connect_ = f"{Fore.LIGHTMAGENTA_EX}Connecting to '{final_server}'.\n"
    for char in connect_:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)

random_int = random.randint(1, 501)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (------------)                                  ","red"))
print(colored("                               IMPORTING LIBS.                                  ","red"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(0.5)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (====>-------)                                  ","cyan"))
print(colored("                             CHECKING RESOURCES.                                  ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(0.5)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (========>---)                                  ","red"))
print(colored("                                LOAD SUCCESS.                                  ","red"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(0.5)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (===========>)                                  ","cyan"))
print(colored("                                  HAVE FUN.                                    ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(0.3)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (===========>)                                  ","red"))
print(colored("                                  HAVE FUN.                                    ","red"))
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(0.3)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print(colored("                               (===========>)                                  ","cyan"))
print(colored("                                  HAVE FUN.                                    ","cyan"))
print("")
print("")
print("")
print("")
print("")
print("")
print("")
clear()
time.sleep(0.3)
print("")
time.sleep(0.03)
print(colored("      ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗","cyan"))
time.sleep(0.03)
print(colored("     ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗","cyan"))
time.sleep(0.03)
print(colored("     ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝","cyan"))
time.sleep(0.03)
print(colored("     ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗","cyan"))
time.sleep(0.03)
print(colored("     ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║","cyan"))
time.sleep(0.03)
print(colored("      ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝","cyan"))
time.sleep(0.03)
print("")
time.sleep(0.03)

welcome = Fore.LIGHTMAGENTA_EX + "Welcome, ready to hunt some coins?\n"
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)
time.sleep(0.5)
threads = f"{Fore.LIGHTGREEN_EX}>>> {Fore.LIGHTRED_EX}Cryptohunt threads set 120  \n"
for char in threads:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)
successfull = f"{Fore.LIGHTMAGENTA_EX}Successfully set.\n"
for char in successfull:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
server_ = f"{Fore.LIGHTGREEN_EX}>>> {Fore.LIGHTRED_EX}Connecting to the fastest cryptohunter server\n"
for char in server_:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(1.4)
print(f"{Fore.LIGHTMAGENTA_EX}Checking if you have subscription....")
time.sleep(1)
subscription = f"{Fore.LIGHTGREEN_EX}>>> {Fore.LIGHTRED_EX}Subscription valid!\n"
for char in subscription:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
servers()
time.sleep(0.6)
print(f"{Fore.LIGHTRED_EX}Connected!")
time.sleep(0.2)
time.sleep(0.5)
print(f"{Fore.LIGHTGREEN_EX}>>>{Fore.LIGHTMAGENTA_EX}Launched")
start = f"{Fore.LIGHTRED_EX}cryptohunter started!\n"
for char in start:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)



def random_string(lenght):
    letters = string.ascii_uppercase + string.digits
    result_string = ''.join(random.choice(letters) for i in range(lenght))
    print(f"{Fore.WHITE}[{Fore.CYAN}CRYPTOHUNT{Fore.WHITE}] TESTING WALLET: {Fore.LIGHTRED_EX}{result_string} {Fore.WHITE}[{Fore.CYAN}RESULT {Fore.RED}0.00 BTC{Fore.WHITE}]")

for i in range(500):
    random_string(30)
    time.sleep(0.02)

def random_wallet(lenght):
    letters = string.ascii_uppercase + string.digits
    result_string = ''.join(random.choice(letters) for i in range(lenght))
    print(f"{Fore.WHITE}[{Fore.CYAN}CRYPTOHUNT{Fore.WHITE}] TESTING WALLET: {Fore.GREEN}{result_string} {Fore.WHITE}[RESULT {Fore.GREEN}6.45 BTC{Fore.WHITE}]")

time.sleep(0.3)
random_wallet(30)
time.sleep(0.2)

print("")
print("")
time.sleep(1)
print(f"{Fore.CYAN} CRYPTOHUNT is closing..")
time.sleep(1)
print(f"{Fore.CYAN} HAVE A NICE DAY :)")
time.sleep(1)
bye = f"{Fore.CYAN} CRYPTOHUNTER by tastefulblatant\n"
for char in bye:
     sys.stdout.write(char)
     sys.stdout.flush()
     time.sleep(0.04)
Fore.RESET
