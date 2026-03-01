import random


lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

chars = lowercase + uppercase + digits


length = int(input("Enter desired password length: "))


if length < 3:
    print("Password length must be at least 3.")
else:
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    
    for i in range(length - 3):
        password.append(random.choice(chars))

    random.shuffle(password)
    final_password = ''.join(password)

    print("Generated Password:", final_password)