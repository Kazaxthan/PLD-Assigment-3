from tkinter import simpledialog
import tkinter as tk
import colorama
import pyfiglet
from colorama import Back, Style, Fore

colorama.init(autoreset=True)

print(Style.BRIGHT + Fore.LIGHTRED_EX + pyfiglet.figlet_format("Welcome to \nRheo's HUB", font="lean", justify="center"))
print(Style.NORMAL + Back.MAGENTA + Fore.BLACK + pyfiglet.figlet_format("To create a profile please comply to the following requests", justify= "center", font= "term"))

while True:
    user_name = input(Fore.CYAN + Back.BLACK+ "What shall we call you? (username): ")
    print(Style.BRIGHT + Fore.LIGHTRED_EX + pyfiglet.figlet_format("\nHello " + str(user_name) + "!", font="stampatello", justify="center"))


    user_full_name = input(Fore.CYAN + Back.BLACK+"Format: (Given Name / Middle Initial / Surname)\nWhat is your name? ")
    while True:
        user_age = input(Fore.CYAN + Back.BLACK+ "How old are you? ")
        if user_age.isdigit() and int(user_age) in range(18, 30):
            break
        if not user_age.isdigit():
            print()
            print(Style.BRIGHT + Back.MAGENTA + Fore.BLACK +"That is not a number you silly")
        if not user_age in range(17, 31) and user_age.isdigit():
            print()
            print(Style.BRIGHT + Back.MAGENTA + Fore.BLACK +"You cannot be possibly that old ")
    print()
    print(Fore.CYAN + Back.BLACK+ "Format: (Street name,Barangay,City,Municipality or Province)")
    user_address = input(Fore.CYAN + Back.BLACK+ "Where do you live? ")
    print()
    print(Style.BRIGHT + Back.MAGENTA + Fore.BLACK + "Your username is " + str(user_name))
    print(Style.BRIGHT + Back.MAGENTA + Fore.BLACK + "Your name is " + str(user_full_name))
    print(Style.BRIGHT + Back.MAGENTA + Fore.BLACK + "And you are " + str(user_age) + " years old")
    print(Style.BRIGHT + Back.MAGENTA + Fore.BLACK + "That lives in " + str(user_address))
    print()
    confirmation = input(Fore.CYAN + Back.BLACK + "Is this information correct? (yes/no): ")

    # Check confirmation
    if confirmation.lower() == "yes":
        print()
        print(Style.BRIGHT + Back.MAGENTA + Fore.BLACK +"Congratulations! This is your profile.\n")
        print()
        break  # Exit the loop if confirmed
    else:
        print(Style.BRIGHT + Back.MAGENTA + Fore.BLACK +"Let's try again.")
        print()

root = tk.Tk()
root.withdraw()
simpledialog.messagebox.showinfo(str(user_name) +"'s Profile", "Name: " + str(user_name) + "\n Age: " + str(user_age) + "\nAddress: " + str(user_address) )

print(Style.DIM + Fore.LIGHTRED_EX + pyfiglet.figlet_format(str(user_name) + "'s Profile", justify= "center", font= "banner3"))
print(Style.DIM + Fore.WHITE + Back.BLACK + pyfiglet.figlet_format("Name: " + str(user_full_name), font= "bigchief"))
print(Style.BRIGHT + Fore.CYAN + Back.BLACK +pyfiglet.figlet_format("Age: " + str(user_age), font= "bigchief"))
print(Style.BRIGHT + Fore.MAGENTA + Back.BLACK +pyfiglet.figlet_format("Address: " + str(user_address), font= "bigchief"))