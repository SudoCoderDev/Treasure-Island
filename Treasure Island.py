print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input('Which Direction would you like to go? "left" or "right"?\n').lower()
if choice_1 == "left":
    choice_2 = input('There is a Sea Which You Have to cross. '
                     'Now choose "swim" to swim accross or "wait" to wait for a while.\n').lower()
    if choice_2 == "wait":
        choice_3 = input('A Boat Picked You Up And Carried You To The Island Safely.'
                          ' There are three color of doors in front of you.'
                          ' Choose Among "yellow", "blue" or "green".\n').lower()
        if choice_3 == "green":
            print("The room is full of fires. You chose the wrong door. Game Over.")
        elif choice_3 == "yellow":
            print("Congratulations! You found the treasure.")
        elif choice_3 == "blue":
            print("The room is full of beasts. You chose the wrong door. Game Over.")
        else:
            print("You failed to choose any door. You are eliminated. Better luck next time.")

    else:
        print('The crocodiles in the sea ate you. Game Over.')


else:
    print("Oh no! There is a Dead End. Game Over.")
