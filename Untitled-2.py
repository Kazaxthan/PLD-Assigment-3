from colorama import Fore, Back, Style, init #for text color 
init(convert=True) 
from pyfiglet import Figlet
f = Figlet(font='slant')


print (Fore.LIGHTMAGENTA_EX+"Hello! Thank you for participating.")
given_name = input ("Kindly enter your name:")

print (Fore.GREEN+"\033[1mMaligayang araw sayo!\033[0m" ,given_name)
print (Fore.RED+"Please you capital letters in answering the questions",Style.RESET_ALL)

given_age = input ("How old are you?")

print (Fore.LIGHTYELLOW_EX+"Where do you live?")
question_address = input (" A. Luzon B. Visayas C. Mindanao ")
if question_address == "A":
    print (Fore.BLUE+"Luzon is a wonderful place!")   

if question_address == "A": 
    part_address = input ("What exact part of Luzon are you from?")
    print (Fore.BLUE+"\033[1mWhat a nice place to live your life to thr fullest\033[0m")

if question_address == "B":
    print (Fore.YELLOW+"Visayas has a plenty of beautiful scnenery!")   

if question_address == "B": 
    part_address = input ("What exact part of Visayas are you from?") 
    print (Fore.YELLOW+"\033[1mWhat a nice place to live your life to thr fullest\033[0m")


if question_address == "C":
    print (Fore.RED+"Mindanao and its various fruits!")

if question_address == "C": 
    part_address = input ("What exact part of Mindanao are you from?")
    print (Fore.RED+"\033[1mWhat a nice place to live your life to thr fullest\033[0m")

print (Fore.YELLOW+"To end our questions, we would like to clarify your details:",Style.RESET_ALL)
print ("\033[1mName:\033[0m",given_name)
print ("\033[1mAge:\033[0m",given_age)
print ("\033[1mAddress:\033[0m",part_address)

print (Fore.LIGHTRED_EX+"Is this correct?")
user_answer = input ("(YES/NO):")
if user_answer == "YES":
    print (Fore.BLUE+"\033[1mCongratulations for completing the questions! Thank you for answering!\033[0m")

if user_answer == "NO":
    correct_info = input (Fore.LIGHTYELLOW_EX+"May I know what information is wrong?")
if user_answer == "NO":
    wrong_info = input (Fore.CYAN+"Kindly put the right information:")  
    print (Fore.GREEN+"",wrong_info)
    fix_info = input ("Is this correct? (YES/NO):")
    if fix_info == "YES":  
     print (Fore.BLUE+"\033[1mCongratulations for completing the questions!\033[0m")

print(Fore.LIGHTMAGENTA_EX+ f.renderText('Thank you for answering!'))