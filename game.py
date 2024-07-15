print('''
                                   /\
                              /\  //\\
                       /\    //\\///\\\        /\
                      //\\  ///\////\\\\  /\  //\\
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\
  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\       |
 / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |           |
/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo  |
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
''')

print("Welcome to the cabin in the green mountains!\nYour mission is to find the right trail to get you to the top of the mountain.")

choice1 = input('You begin hiking and you arrive at a crossroad. Which way should you go? Type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input('You begin the ascent. You arrive at a campsite. Do you want to see if anyone is there? Type "Yes" or "No".').lower()
    if choice2 == "no":
        choice3 = input('Probably a good idea... Never know what you might find. You continue up until you reach a lake. Should you go for a swim? Type "Swim" or "Pass".')
        if choice3 == "pass":
            choice4 = input('Focused, good choice. Now you see a sign that say\'s \"Dangerous!". Type "forward" to keep going, "wait" to stop and snack, or "back" to turn around and go back down.').lower()
            if choice4 == "forward":
                print("CONGRATULATIONS! You made it to the top!")
            elif choice4 == "wait":
                print("Game Over. You almost made it, but by choosing to eat you took too long, it got dark, and you never made it back to your cabin :(")
            else:
                print("Game Over. You made it back to the cabin safely, but you didn't take the risk and try going to the top!")
        else:
            print('Game Over. You were eaten by the Loch Ness monster!')
    else:
        print("Game Over. You looked inside and found someone who is being hunted for a prison break... You know what happened next.")
else:
    print('Game Over. Your trail veered aroudn the mountain and you had to eventually turn back.')

