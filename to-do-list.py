from datetime import datetime
from colorama import Style
from colorama import Fore
now = datetime.today()
now2 = now.strftime("%d/%m/%Y %H:%M:%S")

try:
    open("output.txt", "r")       
except FileNotFoundError:
    open("output.txt", "w")

fr = open("output.txt", "r+")

line_count = 0
for line in fr:
    if line != "\n":
        line_count += 1

start = input("Would you like to add, remove, complete or see your tasks?\n")

def convert(string):
    li = list(string.split("\n"))
    return li


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