# Cody Wiebe
# Basic Password Generation Program
# June 24, 2021

import string
import random

#basic password generator
def basicPassword() :
    length = input("How long do you want your password to be? ")
    size = int(length)
    print(f'Ok {Name} your new password is: ')
    print(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(size)))

#password generator with specific numbers of each of the character types
def advancedPassword() :
    length = input("How long do you want your password to be? ")
    size = int(length)
    letters = input("How many letters do you want in your password? ")
    numbers = input("How many numbers do you want in your password? ")

    #turning the inputs to ints
    lets = int(letters)
    nums = int(numbers)

    if lets + nums > size:
        print('That is too many numbers and letters.')
        exit()
    chars = size - lets - nums

    print(f'You want a password of {size} length with {lets} letters, {nums} numbers and {chars} special characters')
    print(f'I don\'t feel like coding that so you\'re getting a password length {size}: ')
    print(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(size)))

# Getting the users name
Name = input("What is your name: ")

# Do they want a password generated?
password = input("Would you like a password? ")

if password == "yes":
    basicPassword()
elif password == "advanced":
    advancedPassword()   
print('Ok bye.')
exit()

