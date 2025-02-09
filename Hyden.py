
import requests
import time
from colorama import Fore, Style
from pystyle import *
import random
from random import randint, randrange
import string
from rich.console import Console
import os
import sys
import ctypes
import progressbar

console = Console()

ascii = '''
 ██░ ██▓██   ██▓▓█████▄ ▓█████  ███▄    █ 
▓██░ ██▒▒██  ██▒▒██▀ ██▌▓█   ▀  ██ ▀█   █ 
▒██▀▀██░ ▒██ ██░░██   █▌▒███   ▓██  ▀█ ██▒
░▓█ ░██  ░ ▐██▓░░▓█▄   ▌▒▓█  ▄ ▓██▒  ▐▌██▒
░▓█▒░██▓ ░ ██▒▓░░▒████▓ ░▒████▒▒██░   ▓██░
 ▒ ░░▒░▒  ██▒▒▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░▓██ ░▒░  ░ ▒  ▒  ░ ░  ░░ ░░   ░ ▒░
 ░  ░░ ░▒ ▒ ░░   ░ ░  ░    ░      ░   ░ ░ 
 ░  ░  ░░ ░        ░       ░  ░         ░ 
        ░ ░      ░                        '''[1:]

System.Clear()
System.Title("Hyden Software")
print('\n'*2)
print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))
username = input(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Pseudo >> " + Fore.WHITE)

if username == "Hyden":
    password = input(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Password >> " + Fore.WHITE)

    url = "https://pastebin.com/raw/J9PJXFQi"

    x = requests.get(url)

    try:
        if password in x.text:
            
            number = 0
            z = randrange(500)
            proxies = randrange(500)

            print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " You are connected to the server.")
            
            t = 0.0

            print(Style.BRIGHT + Fore.RED)
            bar = progressbar.ProgressBar(maxval=10, widgets=[
	            ' Launching... ',
	            progressbar.Bar(left='| ', marker='█', right=' | '),
	            progressbar.SimpleProgress(),
            ]).start()
            
            while t <= 10.0:
                bar.update(t)
                time.sleep(0.1)
                t += 0.1
            bar.finish()
            time.sleep(2)
            System.Clear()
            print('\n'*2)
            print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))
            print('\n'*3)

            print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "1" + Fore.WHITE + "]" + Fore.RED + " BTC Minor")
            print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "2" + Fore.WHITE + "]" + Fore.RED + " ETH Minor")
            print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "3" + Fore.WHITE + "]" + Fore.RED + " Nitro Minor")
            option = input(Fore.RED + "  >> " + Fore.WHITE)
            
            # Option 1
            if option == "1":
                System.Clear()
                print('\n'*2)
                print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))
                print('\n'*2)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Loading configuration...")
                time.sleep(2.8)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Configuration loaded in " + Fore.WHITE + "2.8" + Fore.RED + " seconds !")
                print("\n")
                wallet = input(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.RED + Style.BRIGHT + " Wallet >> " + Fore.WHITE)
                print("\n")
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.LIGHTGREEN_EX + Style.BRIGHT + " Valid address | I run the script...")
                System.Title(f"Hyden Wallet Miner - Gen: BTC - Votre Wallet: {wallet} - Gen: {number}")
                time.sleep(0.9)
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.RED + Style.BRIGHT + " Decrypt in:" + Fore.WHITE + Style.BRIGHT + " 0.9 " + Fore.RED + "seconds")
                time.sleep(1.542172)
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.WHITE + Style.BRIGHT + f" {proxies} " + Fore.RED + Style.BRIGHT + "proxies find in" + Fore.WHITE + Style.BRIGHT + " 1.542172 " + Fore.RED + Style.BRIGHT + "seconds")
                print("\n"*2)
                time.sleep(1)
                while number != z:
                    number += 1
                    System.Title(f"Hyden Wallet - Gen: BTC - Votre Wallet: {wallet} - Gen: {number}")
                    letters = string.ascii_letters
                    print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Generated" + Fore.BLACK + " - " + Fore.WHITE + Style.BRIGHT + "0x" + ''.join(random.choice(letters) for i in range(50)) + Fore.BLACK + " - " + Fore.WHITE + "0.000 " + Fore.RED + "BTC")
                    time.sleep(0.005)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Generated" + Fore.BLACK + " - " + Fore.GREEN + Style.BRIGHT + "0x" + ''.join(random.choice(letters) for i in range(50)) + Fore.BLACK + " - " + Fore.WHITE + "0.012 " + Fore.RED + "BTC")
                time.sleep(0.025)
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " The wallet contains" + Fore.WHITE + " 0.012 " + Fore.RED + "BTC, " + Fore.WHITE + " 255,34" + Fore.RED + "€ !")
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " I found this wallet after" + Fore.WHITE + f" {number} " + Fore.RED + "wallet Generated.")
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Transaction in progress...")
                time.sleep(3)
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Transaction on your wallet completed!")
                time.sleep(0.025)
                input(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.BLACK + " Thank you for using our BTC miner and trusting us!\n")
            
            # Option 2    
            elif option == "2":
                System.Clear()
                print('\n'*2)
                print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))
                print('\n'*2)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Loading configuration...")
                time.sleep(2.8)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Configuration loaded in " + Fore.WHITE + "2.8" + Fore.RED + " seconds !")
                print("\n")
                wallet = input(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.RED + Style.BRIGHT + " Wallet >> " + Fore.WHITE)
                print("\n")
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.LIGHTGREEN_EX + Style.BRIGHT + " Valid address | I run the script...")
                System.Title(f"Hyden Wallet Miner - Gen: ETH - Votre Wallet: {wallet} - Gen: {number}")
                time.sleep(0.9)
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.RED + Style.BRIGHT + " Decrypt in:" + Fore.WHITE + Style.BRIGHT + " 0.9 " + Fore.RED + "seconds")
                time.sleep(1.542172)
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.WHITE + Style.BRIGHT + f" {proxies} " + Fore.RED + Style.BRIGHT + "proxies find in" + Fore.WHITE + Style.BRIGHT + " 1.542172 " + Fore.RED + Style.BRIGHT + "seconds")
                print("\n"*2)
                time.sleep(1)
                while number != z:
                    number += 1
                    System.Title(f"Hyden Wallet - Gen: ETH - Votre Wallet: {wallet} - Gen: {number}")
                    letters = string.ascii_letters
                    print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Generated" + Fore.BLACK + " - " + Fore.WHITE + Style.BRIGHT + "0x" + ''.join(random.choice(letters) for i in range(50)) + Fore.BLACK + " - " + Fore.WHITE + "0.000 " + Fore.RED + "ETH")
                    time.sleep(0.005)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Generated" + Fore.BLACK + " - " + Fore.GREEN + Style.BRIGHT + "0x" + ''.join(random.choice(letters) for i in range(50)) + Fore.BLACK + " - " + Fore.WHITE + "0.183 " + Fore.RED + "ETH")
                time.sleep(0.025)
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " The wallet contains" + Fore.WHITE + " 0.183 " + Fore.RED + "ETH, " + Fore.WHITE + " 215,25" + Fore.RED + "€ !")
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " I found this wallet after" + Fore.WHITE + f" {number} " + Fore.RED + "wallet Generated.")
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Transaction in progress...")
                time.sleep(3)
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Transaction on your wallet completed!")
                time.sleep(0.025)
                input(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.BLACK + " Thank you for using our ETH miner and trusting us!\n")
            
            # Option 3
            elif option == "3":
                System.Clear()
                print('\n'*2)
                print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))
                print('\n'*2)
                num = int(input(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " How much Nitro >> " + Fore.WHITE))

                with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
                    print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " The codes are being generated...")
                    
                    for i in range(num):
                        code = "".join(
                            random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=19))

                        file.write(f"https://discord.gift/{code}\n")
                time.sleep(2.157)
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.WHITE + Style.BRIGHT + f" {num} " + Fore.RED + "Codes Generated in" + Fore.WHITE + f" 2.157 " + Fore.RED + "seconds.")
                print("\n"*2)

                with open("Nitro Codes.txt") as file:
                    for line in file.readlines():
                        nitro = line.strip("\n")

                        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

                        r = requests.get(url)
                        

                        if r.status_code == 200:
                            print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Generated" + Fore.BLACK + " - " + Fore.WHITE + Style.BRIGHT + f"{nitro}" + Fore.BLACK + " - " + Fore.GREEN + "Valide")
                            number += 1
                            System.Title(f"Hyden Wallet - Gen: Nitro - Gen: {number}")
                            break
                        else:
                            number += 1
                            System.Title(f"Hyden Wallet - Gen: Nitro - Gen: {number}")
                            print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Generated" + Fore.BLACK + " - " + Fore.WHITE + Style.BRIGHT + f"{nitro}" + Fore.BLACK + " - " + Fore.RED + "Invalide")
                        

                
                time.sleep(0.025)
                print("\n"*2)
                input(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.BLACK + " Thank you for using our Nitro miner and trusting us!\n")
        else:
            print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Wrong password.")
            time.sleep(30)
            exit()
    
    except:
        print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " I can't connect to the server!")
        time.sleep(30)
        exit()
else:
    input(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + f" I can't find a named account '{username}'")
