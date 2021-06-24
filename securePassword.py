# Cody Wiebe
# Basic Password Generation Program
# June 24, 2021

import string
import random

print(''.join(random.choice(string.ascii_letters) for i in range(10)))
# Getting the users name
Name = input("What is your name: ")

# Do they want a password generated?
password = input("Would you like a password? ")

if password == "yes":
    length = input("How long do you want your password to be? ")
    size = int(length)
    print(f'Ok {Name} your new password is: ')
    print(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(size)))
elif password == "advanced":
    length = input("How long do you want your password to be? ")
    size = int(length)
    letters = input("How many letters do you want in your password? ")
    lets = string.ascii_letters
    numbers = input("How many numbers do you want in your password? ")
    nums = string.digits
    characs =  input("How many special characters do you want in your password? ")
    chars = string.punctuation
    print(f'You want a password of {length} length with {letters} letters, {numbers} numbers and {characs} characters')
else:
    print('Ok bye.')
    
    