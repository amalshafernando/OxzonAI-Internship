import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "|", "\\", ";", ":", "'", "\"", ",", ".", "/", "<", ">", "?", "~", "`"
]

password_length = int(input("Enter the password length = "))

# Ensure at least one character from each category is included
password = [
    random.choice(letters),
    random.choice(numbers),
    random.choice(symbols)
]

# Fill the remaining characters
remaining_length = password_length - len(password)
all_characters = letters + numbers + symbols

for _ in range(remaining_length):
    password.append(random.choice(all_characters))

# Shuffle the password to randomize order
random.shuffle(password)

# Convert list to a string
final_password = ''.join(password)
print("Generated Password:", final_password)
