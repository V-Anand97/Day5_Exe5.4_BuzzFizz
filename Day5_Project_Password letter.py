import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
'''
password = ''
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password = password + random_char
for char in range (1, nr_numbers):
    random_numbers = random.choice(numbers)
    password = password + random_numbers
for char in range (1, nr_symbols):
    random_symbols = random.choice(symbols)
    password = password + random_symbols
print(password)
'''
password = []
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password.append(random_char)
for char in range (1, nr_numbers):
    random_numbers = random.choice(numbers)
    password.append(random_numbers)
for char in range (1, nr_symbols):
    random_symbols = random.choice(symbols)
    password.append(random_symbols)
print(password)
shuffled_password= []
random.shuffle(password)
final_password = ''
for char in password:
    final_password +=char
print(f"you password is {final_password}")
