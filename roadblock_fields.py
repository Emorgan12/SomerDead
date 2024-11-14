from time import sleep
from os import system

def road_block(family):
    system('cls')
    print("You leave your house and jump in the car.")
    sleep(2)
    if family:
        print("Your daughters are in the back and your wife is next to you in the passenger seat. Everyone is worriedly silent, not sure what to say to make the mood lighter.")
    else:
        print("The car is eerily silent until you see some form of civilization.")
    sleep(2)
    print("There's a road block ahead. People are running everywhere and there's no chance of getting a car through this chaos.")
    sleep(2)
    print("You can see a handful of the strange-looking creatures that caused all this. They're definitely dangerous")
    sleep(2)
    print("You conclude that there's no option but to get out of the car and walk. You're not sure where you're going, but you know you have to get out of here.")
    sleep(2)
    print("Before getting out the car, you try to formulate a plan.")
    sleep(2)
    system('cls')
    print("There's a military base nearby, you could try to get there.")
    sleep(2)
    print("It won't be easy, but it's the best option for safety.")
    sleep(2)
    system('cls')
    if family:
        print("You continue, your wife holding Chelsea's hand and you holding Amber's.")
        sleep(2)
        print("Above everything, you need to keep your family safe.")
        sleep(2)
        print("Especially Amber and Chelsea, they're so young and innocent.")
    else:
        print("You continue, alone, worry for your family in the back of your mind")
        sleep(4)
        system('cls')
        print("But it's for the best, right?")
    sleep(2)


def fields(family):
    system('cls')
    print("You've not been walking long, maybe 15 minutes, when you come across a field.")
    sleep(2)
    print("The field is bright green with specs of other colours. It's serene and calm.")
    sleep(1)
    print("There's no one in the field.")
    sleep(2)
    if family:
        print("Just you, and your family.")
    else:
        print("It's just you, walking alone.")
    sleep(2)
    system('cls')
    print("There's a few birds, but they're dead silent.")
    sleep(2)
    print("It's as if they're aware and of the danger and they're scared.")
    sleep(2)
    system('cls')
    if family:
        print("Despite the fact you've not been walking long, Chelsea and Amber are complaining their legs hurt.")
        sleep(2)
        print("You decide to take a break, and sit down in the field, but not for long.")
        sleep(2)
        system('cls')
        print("You're sat there for around 2 minutes, quiet talking in an attempt to calm them down.")
        sleep(2)
        print("You're scared, but you know everything will be okay when you get to the military base, together")
        sleep(2)
        print("You need to keep moving, you all stand up and continue walking.")
    else:
        print("The field is empty, most people are running in the roads and in the streets, aimlessly")

    sleep(2)
    system('cls')
    print("The fields feel safe, but you must keep your guard up, nowhere is safe when there's these creatures flooding the streets")
    sleep(2)
    print("Anything could appear, you have to stay aware of your surroundings")
    sleep(2)
    system('cls')
    print("You come accross a massive patch of mud.")
    sleep(2)
    print("There's a path that goes around, but that could add another 15-20 minutes to your journey")
    sleep(1)
    print("You have to decide whether to go around it or go through it.")
    sleep(2)
    if family:
        print("Both Chelsea and Amber are urging you to go around,")
        sleep(1)
        print("but your wife trusts your decision will be best.")
        sleep(2)
    system('cls')
    while True:
        print("Will you go through the mud?")
        sleep(0.5)
        ans = input("Y- Yes \nN- No \n\n").upper()
        if ans == "Y":
            system('cls')
            print("You go through the mud")
            sleep(2)
            print("It's deeper than you thought.")
            sleep(2)
            print("Your entire feet and ankles are submerged.")
            sleep(2)
            if family:
                print("Not being very tall, it comes up halfway up the bottom of your daughter's legs")
                sleep(2)
                system('cls')
                print("They are *not* happy about it.")
            print("You get through the mud but you are now covered in mud.")
            break
        elif ans == "N":
            system('cls')
            print("You go around the mud.")
            if family:
                print("Amber and Chelsea's mood seems to have lifted")
                print("They really didn't want to go through that mud")
            print("You may have stayed clean and dry but added 20 minutes to your journey")
            break
        else:
            print("\nInvalid Input")
            print()
            sleep(1)
            system('cls')
    print("You continue walking for about 30 minutes until you spot your destination up ahead")


road_block(False)
fields(False)