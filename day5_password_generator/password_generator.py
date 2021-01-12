import random

SYMBOLS = "! % / @ # ( ) _ $ < >"
CHARS = "A B C D E F G H I J K L M N O P Q U R S T X Y Z W V"

pw_len = int(input("How many characters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like?\n"))
number_count = int(input("How many numbers would you like?\n"))
char_count: int = pw_len - symbol_count - number_count

generated_passwd = []
for char in range(0, char_count):
    generated_passwd.append(str(random.choice(CHARS.split())))
for index_to_lowercase in range(0, char_count):
    random_lowercase = random.randint(0, 1000)
    if random_lowercase % 2 == 0:
        generated_passwd[index_to_lowercase] = generated_passwd[index_to_lowercase].lower()

for char in range(0, number_count):
    generated_passwd.append(str(random.randint(0, 9)))
for char in range(0, symbol_count):
    generated_passwd.append(str(random.choice(SYMBOLS.split())))

random.shuffle(generated_passwd)
# List to string
final_password: str = ''.join(str(elem) for elem in generated_passwd)
print(F"Your generated password is: {final_password}")
