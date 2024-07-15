import random
# import random_mod

# print(random_mod.pi)

# random_int = random.randint(1,10)
# print(random_int)

# random_float = random.random() + random.randint(0,5)
# print(random_float)

# random_float = random.random() * 5
# print(random_float)

#-----------------------------------------
# #Storing lists holds the order:
# states_of_us = ["Delaware", "Pennsylvania"]
# print(states_of_us[0])
# print(states_of_us[-2])

# # Changing the items in the list:
# states_of_us[1] = "Pencilvania"

# # Add an item or items to the list:
# states_of_us.append("New Jersey")
# states_of_us.extend("New Mexico, New York")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_input = int(input('What\'s your move? Rock (type 0), paper (type 1), or scissor (type 2)?\n'))
if user_input >= 3 or user_input <0:
    print("invalid input!")
    
else:
    print(game_images[user_input])
    
    cpu_choice = random.randint(0,2)
    print(f"Computer chose: {game_images[cpu_choice]}")

    if cpu_choice == 2 and user_input == 0:
        print("You win!")
    elif cpu_choice == 0 and user_input == 2:
        print("You lose!")
    elif cpu_choice > user_input:
        print("You lose!")
    elif user_input > cpu_choice:
        print("You win!")
    elif cpu_choice == user_input:
        print("It's a draw!")
