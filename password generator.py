import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

choice = int(input("Quick password, or custom tool? Type 1 for quick, 2 for custom.\n"))
if choice <1 or choice > 2:
    print("Invalid input. Please input 1 or 2. Run the program again.")
else:

    if choice == 1:
        for char in range(1, 4):
            password_list += random.choice(letters)
        for num in range(1, 4):
            password_list += random.choice(numbers)
        for symb in range(1, 4):
            password_list += random.choice(symbols)
    else:
        chars = int(input("How many letters would you like?\n"))
        nums = int(input("How many numbers would you like?\n"))
        symbs = int(input("How many symbols would you like?\n"))

        for char in range(1, chars + 1):
            password_list += random.choice(letters)

        for num in range(1, nums + 1):
            password_list += random.choice(numbers)

        for symb in range(1, symbs + 1):
            password_list += random.choice(symbols)

    random.shuffle(password_list)
    password = ""
    for item in password_list:
        password += item

    print(f"Here is your password: {password}")

    
    
