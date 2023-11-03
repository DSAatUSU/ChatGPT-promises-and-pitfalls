# This program will read a specific line from the file called in line 7 and 8

import os

number_chosen = (int(input("This program is designed to print a specific line\nfrom a specific file. The program will first check\nto see if line_numbers.txt exists. If it does, it will execute.\nPlease enter the number you'd like to print:\n")) - 1)

if os.path.exists("./line_numbers.txt"):
    file = open('line_numbers.txt')
    content = file.readlines()
    print(content[number_chosen])
