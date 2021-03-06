from datetime import datetime
from colorama import Style
from colorama import Fore
import os
from colorama import init
now = datetime.today()
now2 = now.strftime("%d/%m/%Y %H:%M:%S")

def convert(string):
    li = list(string.split("\n"))
    return li

init()
print(f"{Fore.YELLOW} _____      ______        _     _     _   \n|_   _|     |  _  \      | |   (_)   | |  \n  | | ___   | | | |___   | |    _ ___| |_ \n  | |/ _ \  | | | / _ \  | |   | / __| __|\n  | | (_) | | |/ / (_) | | |___| \__ \ |_ \n  \_/\___/  |___/ \___/  \_____/_|___/\__|{Style.RESET_ALL}")

print(f"{Fore.RED}Type 'help' for a list of commands{Style.RESET_ALL}")


while True:
    init(convert=True)
    try:
        open("output.txt", "r")       
    except FileNotFoundError:
        open("output.txt", "w")

    fr = open("output.txt", "r+")

    line_count = 0
    for line in fr:
        if line != "\n":
            line_count += 1

    print(f"{Fore.YELLOW}Enter a command:{Style.RESET_ALL}")
    start = input()

    if start == "help":
        print(f"{Fore.BLUE}Commands:{Style.RESET_ALL}{Fore.RED}\nadd {Fore.GREEN}(add a task)\n{Fore.RED}see {Fore.GREEN}(see your tasks)\n{Fore.RED}remove {Fore.GREEN}(remove a task)\n{Fore.RED}complete {Fore.GREEN}(mark a task as completed)\n{Fore.RED}wipe {Fore.GREEN}(wipes your entire list)\n{Fore.RED}exit {Fore.GREEN}(exits the program){Style.RESET_ALL}")


    if start == "add":
        f = open("output.txt", "a")
        a = input("Input:\n")
        f.write(f"{line_count}. {a}")
        f.write("\n")
        f.close()
        print(f"\nAdded todo: {a} \n")

    if start == "see":
        fr = open("output.txt", "r+")
        print("\ntasks:\n" + fr.read() + "\n")
        fr.close()

    if start == "remove":
        fr = open("output.txt", "r+")
        str1 = " "
        l = fr.readlines()
        x = int(input("Enter the number of the task you want to remove:\n"))
        fr.truncate(0)
        del l [x]
        fr.seek(0)
        fr.write(str1.join(l))

        fr = open("output.txt", "r+")
        t = -1
        str1 = ""
        line_count = 0
        l = convert(fr.read())
        del l [-1]
        fr.seek(0)
        fr.truncate(0)
        fixy = [amoogus[3:] for amoogus in l]
        for i in l:
            t += 1
            fr.write(f"{line_count}. {str1.join(fixy[t])}\n")
            line_count += 1
        
    if start == "complete":
        fr = open("output.txt", "r+")
        str1 = ""
        complete = int(input("Which task would you like to mark as complete?\n"))
        l = convert(fr.read())
        l[complete] = l[complete] + f" {Fore.GREEN}[x] {now2}{Style.RESET_ALL}"
        fixy2 = [s + "\n" for s in l]
        del fixy2 [-1]
        fr.truncate(0)
        fr.seek(0)
        fr.write(str1.join(fixy2))
        print("\n")
        print(f"succesfully marked task {complete} as complete")

    if start == "wipe":
        fr = open("output.txt", "r+")
        fr.truncate(0)
        fr.seek(0)
        fr.close()

    if start == "exit":
        exit(0)