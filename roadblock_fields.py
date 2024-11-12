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

road_block(True)
fields(True)