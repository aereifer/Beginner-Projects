#Password Generator
"""
Generate secure and random passwords based on user specified criteria (length, special characters, etc)
"""

import random

letters = tuple("abcdefghijklmnopqrstuvwxyz")
numbers = tuple("0123456789")
special_chars = tuple("!@#$%&_")

random_dict = {letters:26, numbers:10, special_chars:7}

def check_ans(ans):
    if ans not in ["Y","N"]:
        ans = input("Invalid input. Please enter Y or N.")
    else:
        return ans
    
def check_int(num):
    check = False
    
    while not check:
        if num.lstrip("-").isdigit():
            num = int(num)
            
            if num <= 0:
                num = input("Invalid input. Please enter a number greater than 0.")
            else:
                check = True
        else:
            num = input("Invalid input. Please enter a number.")
            
    return num

def gen_password(length, num_ans, special_ans):
    options = [letters]
    password = ""
    
    if num_ans == "Y":
        options.append(numbers)
    if special_ans == "Y":
        options.append(special_chars)


    while len(password) < length:
        char_type = random.randint(0, len(options)-1)
        
        password += options[char_type][random.randint(0, random_dict[options[char_type]]-1)]
    
    return password


keep_going = check_ans(input("Would you like to generate a random password? (Y/N)"))

while keep_going == "Y":
    password = gen_password(check_int(input("Enter the length of the password.")), check_ans(input("Would you like the password to include numbers? (Y/N)")), check_ans(input("Would you like the password to include special characters? (Y/N)")))
    
    print("\n" + password)
    
    keep_going = check_ans(input("Would you like to generate another password? (Y/N)"))