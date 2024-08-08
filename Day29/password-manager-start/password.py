import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.',
           '?', '/']

num_alpha = random.randint(8, 15)
num_numbers = random.randint(2, 4)
num_symb = random.randint(2, 4)

password_list = []

password_list += [random.choice(alphabets) for i in range(num_alpha)]
password_list += [random.choice(numbers) for j in range(num_numbers)]
password_list += [random.choice(symbols) for k in range(num_symb)]
random.shuffle(password_list)
password = ""
for p in password_list:
    password += p
print(password)
