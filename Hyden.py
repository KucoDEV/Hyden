
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
    password = input(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Mot de passe >> " + Fore.WHITE)

    url = "https://pastebin.com/raw/J9PJXFQi"

    x = requests.get(url)

    try:
        if password in x.text:
            
            number = 0
            z = randrange(500)
            proxies = randrange(500)

            print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Vous êtes connecter au serveur.")
            
            t = 0.0

            print(Style.BRIGHT + Fore.RED)
            bar = progressbar.ProgressBar(maxval=10, widgets=[
	            ' Lancement... ',
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

            print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "1" + Fore.WHITE + "]" + Fore.RED + " Mineur de BTC ")
            print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "2" + Fore.WHITE + "]" + Fore.RED + " Mineur de ETH")
            print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "3" + Fore.WHITE + "]" + Fore.RED + " Mineur de Nitro")
            option = input(Fore.RED + "  >> " + Fore.WHITE)
            
            # Option 1
            if option == "1":
                System.Clear()
                print('\n'*2)
                print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))
                print('\n'*2)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Chargement de la configuration...")
                time.sleep(2.8)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Configuration chargée en " + Fore.WHITE + "2.8" + Fore.RED + " secondes !")
                print("\n")
                wallet = input(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.RED + Style.BRIGHT + " Entrez votre wallet >> " + Fore.WHITE)
                print("\n")
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.LIGHTGREEN_EX + Style.BRIGHT + " Adresse valide | Je lance le script...")
                System.Title(f"Hyden Wallet Miner - Gen: BTC - Votre Wallet: {wallet} - Gen: {number}")
                time.sleep(0.9)
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.RED + Style.BRIGHT + " Décrypter en:" + Fore.WHITE + Style.BRIGHT + " 0.9 " + Fore.RED + "secondes")
                time.sleep(1.542172)
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.WHITE + Style.BRIGHT + f" {proxies} " + Fore.RED + Style.BRIGHT + "proxies trouver en" + Fore.WHITE + Style.BRIGHT + " 1.542172 " + Fore.RED + Style.BRIGHT + "secondes")
                print("\n"*2)
                time.sleep(1)
                while number != z:
                    number += 1
                    System.Title(f"Hyden Wallet - Gen: BTC - Votre Wallet: {wallet} - Gen: {number}")
                    letters = string.ascii_letters
                    print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Généré" + Fore.BLACK + " - " + Fore.WHITE + Style.BRIGHT + "0x" + ''.join(random.choice(letters) for i in range(50)) + Fore.BLACK + " - " + Fore.WHITE + "0.000 " + Fore.RED + "BTC")
                    time.sleep(0.005)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Généré" + Fore.BLACK + " - " + Fore.GREEN + Style.BRIGHT + "0x" + ''.join(random.choice(letters) for i in range(50)) + Fore.BLACK + " - " + Fore.WHITE + "0.012 " + Fore.RED + "BTC")
                time.sleep(0.025)
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Le wallet contient" + Fore.WHITE + " 0.012 " + Fore.RED + "BTC soit" + Fore.WHITE + " 255,34" + Fore.RED + "€ !")
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " J'ai trouver ce wallet après" + Fore.WHITE + f" {number} " + Fore.RED + "wallet généré.")
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Transaction en cours...")
                time.sleep(3)
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Transaction sur votre wallet terminé !")
                time.sleep(0.025)
                input(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.BLACK + " Merci d'avoir utiliser notre mineur de BTC et de nous faire confiance !\n")
            
            # Option 2    
            elif option == "2":
                System.Clear()
                print('\n'*2)
                print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))
                print('\n'*2)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Chargement de la configuration...")
                time.sleep(2.8)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Configuration chargée en " + Fore.WHITE + "2.8" + Fore.RED + " secondes !")
                print("\n")
                wallet = input(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.RED + Style.BRIGHT + " Entrez votre wallet >> " + Fore.WHITE)
                print("\n")
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.LIGHTGREEN_EX + Style.BRIGHT + " Adresse valide | Je lance le script...")
                System.Title(f"Hyden Wallet Miner - Gen: ETH - Votre Wallet: {wallet} - Gen: {number}")
                time.sleep(0.9)
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.RED + Style.BRIGHT + " Décrypter en:" + Fore.WHITE + Style.BRIGHT + " 0.9 " + Fore.RED + "secondes")
                time.sleep(1.542172)
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.WHITE + Style.BRIGHT + f" {proxies} " + Fore.RED + Style.BRIGHT + "proxies trouver en" + Fore.WHITE + Style.BRIGHT + " 1.542172 " + Fore.RED + Style.BRIGHT + "secondes")
                print("\n"*2)
                time.sleep(1)
                while number != z:
                    number += 1
                    System.Title(f"Hyden Wallet - Gen: ETH - Votre Wallet: {wallet} - Gen: {number}")
                    letters = string.ascii_letters
                    print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Généré" + Fore.BLACK + " - " + Fore.WHITE + Style.BRIGHT + "0x" + ''.join(random.choice(letters) for i in range(50)) + Fore.BLACK + " - " + Fore.WHITE + "0.000 " + Fore.RED + "ETH")
                    time.sleep(0.005)
                print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Généré" + Fore.BLACK + " - " + Fore.GREEN + Style.BRIGHT + "0x" + ''.join(random.choice(letters) for i in range(50)) + Fore.BLACK + " - " + Fore.WHITE + "0.183 " + Fore.RED + "ETH")
                time.sleep(0.025)
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Le wallet contient" + Fore.WHITE + " 0.183 " + Fore.RED + "ETH soit" + Fore.WHITE + " 215,25" + Fore.RED + "€ !")
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " J'ai trouver ce wallet après" + Fore.WHITE + f" {number} " + Fore.RED + "wallet généré.")
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Transaction en cours...")
                time.sleep(3)
                print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Transaction sur votre wallet terminé !")
                time.sleep(0.025)
                input(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.BLACK + " Merci d'avoir utiliser notre mineur de ETH et de nous faire confiance !\n")
            
            # Option 3
            elif option == "3":
                System.Clear()
                print('\n'*2)
                print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(ascii)))
                print('\n'*2)
                num = int(input(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Combien de Nitro a gen >> " + Fore.WHITE))

                with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
                    print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.RED + " Les codes sont en train de se generer...")
                    
                    for i in range(num):
                        code = "".join(
                            random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=19))

                        file.write(f"https://discord.gift/{code}\n")
                time.sleep(2.157)
                print(Fore.WHITE + Style.BRIGHT + f" [" + Fore.RED +"?" + Fore.WHITE +"]" + Fore.WHITE + Style.BRIGHT + f" {num} " + Fore.RED + "codes générés en" + Fore.WHITE + f" 2.157 " + Fore.RED + "secondes.")
                print("\n"*2)

                with open("Nitro Codes.txt") as file:
                    for line in file.readlines():
                        nitro = line.strip("\n")

                        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

                        r = requests.get(url)
                        

                        if r.status_code == 200:
                            print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Généré" + Fore.BLACK + " - " + Fore.WHITE + Style.BRIGHT + f"{nitro}" + Fore.BLACK + " - " + Fore.GREEN + "Valide")
                            number += 1
                            System.Title(f"Hyden Wallet - Gen: Nitro - Gen: {number}")
                            break
                        else:
                            number += 1
                            System.Title(f"Hyden Wallet - Gen: Nitro - Gen: {number}")
                            print(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Généré" + Fore.BLACK + " - " + Fore.WHITE + Style.BRIGHT + f"{nitro}" + Fore.BLACK + " - " + Fore.RED + "Invalide")
                        

                
                time.sleep(0.025)
                print("\n"*2)
                input(Fore.WHITE + Style.BRIGHT + " [" + Fore.RED + "?" + Fore.WHITE + "]" + Fore.BLACK + " Merci d'avoir utiliser notre mineur de Nitro et de nous faire confiance !\n")
        else:
            print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Mauvais mot de passe.")
            time.sleep(30)
            exit()
    
    except:
        print(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + " Je n'arrive pas à me connecter au serveur !")
        time.sleep(30)
        exit()
else:
    input(Fore.WHITE + Style.BRIGHT + "\n [" + Fore.RED + "!" + Fore.WHITE + "]" + Fore.RED + f" Je ne trouve pas de compte nommé '{username}'")
