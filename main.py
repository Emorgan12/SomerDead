import json
from time import sleep
import os
from roadblock_fields import road_block, fields
from alexs_epic_storytelling import mil_base_outskirts
from airport_and_house import airport, house


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



def main():
    title()
    tutorial()
    family = airport()
    if family:
        stay = house() 
    if stay:
        exit()
    road_block(family)
    fields(family)
    mil_base_outskirts(family)
    #mil_base(family)
    
if __name__ == "__main__":
    main()