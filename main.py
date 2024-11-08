import json
from time import sleep
import os

items = open('items.json', 'r')
items = json.load(items)
inventory = []

def pizza_guy():
    while True:
        print("You can answer the door (1)")
        print("Or you can ignore the door (2)")
        answer = input("What do you do? ")
        if answer == "1":
            os.system('cls')
            print("You open the door to see who it is. It's just the pizza delivery guy. You take the pizza and pay him. You close the door and go back to the living room.")
            print("You sit back down on the couch and continue watching your daughters play.")
            break
        elif answer == "2":
            os.system('cls')
            print("You ignore the door and continue watching your daughters play. The knocking continues. You decide to ignore it and continue watching your daughters play.")
            print("There's a shout, it's the pizza delivery guy, announcing he's here")
        else:
            os.system('cls')
            print("Invalid input. Please try again.")
def title():
    print("░▒▓███████▓▒░░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
    print(" ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
    print("       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
    print("       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
    print("░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  ")

def tutorial():
    print("You're home, with your family. Your daughters, Chelsea and Amber are playing on the floor, you and your wife, Eve, are sitting on the couch, watching them play. You hear a knock on the door.")
    pizza_guy()
    sleep(7)
    os.system('cls')
    print("The evening continues as it usually would on a Friday, with you and your family enjoying each other's company. You decide to go to bed early, as you have a long day ahead of you tomorrow.")
    sleep(7)
    os.system('cls')
    print("You've been invited to the Amazon Rainforest as part of a research team by the MI6, you're an incredible scientist, one of the best in your field. \nA new virus has been found due to the deforestation. You're excited to go, but you're also nervous. You've never been to the Amazon before, and you've heard stories of people getting lost in the forest and never being found \nAnd this virus could turn out to be deadly.")


    


def airport():
    print("You feel the cool cloth of your bedsheets against your skin as you slowly come round, your eyes open and your sight is blurry but you can just about make out your room, you look to your right and see your wife asleep gently snoring. you say your goodbyes and kiss her on the forhead   ")

def house():
    #return True if staying else return False
    pass

def road_block():
    pass

def fields():
    pass


def mil_base_outskirts():
    ans = input("After a long walk along the heedgerows of the fields, you find yourself at a barbed wire fence with a sign reading \"NO ENTRY\". This must be the military base. You follow the fence west, as that must be where the entrance is.\n\nIn the distance, you can see the gate. Something is off. There is not a single person in sight. You get closer and realize that the gate has been forced open. Upon closer inspection, you notice bodies in and around the cars lined up in front of the gate. \nA firefight seems to have broken out between the military and an unknown third party, resulting in the death of a guard sitting in a gatehouse on the right side of the gate.\n\nSearch his body?\n\nY- Yes\nN- No\n\n")

    if ans == "y":
        os.system("cls")
        print("A fowl stench attacks your nose. On his body, you obtain a keycard; but also another question: How is the guard's body emitting this stench if he's only died recently?\nYou brush it off and move on. As you leave, you feel like you saw something move in the corner of your eye.")
        #he obtains the keycard here
    else:
        os.system("cls")
        print("Even as a top of the line biologist, dead bodies give you the ick. You decide to pass.")

    print("You walk through yet another open field, towards a group of buildings.  One of them reads: \"MUNITIONS STORAGE\"")


def mil_base():
    pass

def main():
    title()
    tutorial()
    '''
    airport()
    stay = house()
    if stay:
        exit()
    road_block()
    fields()
    mil_base_outskirts()
    mil_base()
    '''
    
if __name__ == "__main__":
    main()