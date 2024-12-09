'''
User Story - 0013 - Project 3 Simple Password Generator
● Objective : : Generate strong, random passwords.
● Key Concepts
     ○ String manipulation and random library.
     ○ Lists and loops for character selection.
● Features
     ○ Input desired password length.
     ○ Include letters (uppercase and lowercase), numbers, and special characters.
     ○ Display the generated password.
● Bonus
     ○ Option to specify requirements (e.g., at least one uppercase letter, one
number, etc.).
'''
import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "|", "\\", ";", ":", "'", "\"", ",", ".", "/", "<", ">", "?", "~", "`"
]


password_length = int(input("Enter the password length = "))

password = ""

for i in range(1,password_length):
     character = random.choice(letters)
     password += character
for i in range(password_length):
     character = random.choice(numbers)
     password += character
for i in range(password_length):
     character = random.choice(symbols)
     password += character
     
print(password)     