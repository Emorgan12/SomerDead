from time import sleep
from os import system

def road_block(family):
    print("You leave your house and jump in the car.")
    sleep(2)
    if family:
        print("Your daughters are in the back and your wife is next to you in the passenger seat. Everyone is worriedly silent, not sure what to say to make the mood lighter.")
    else:
        print("The car is eerily silent until you see some form of civilization.")
    sleep(2)
    print("There's a road block ahead. People are running everywhere and there's no chance of getting a car through this chaos.")
    sleep(2)
    print("You decide to get out of the car and walk. You're not sure where you're going, but you know you have to get out of here.")
    sleep(2)
    print("Before getting out the car, you try to formulate a plan.")
    sleep(2)
    system('cls')

    print("There's a military base nearby, you could try to get there.")
    sleep(2)
    print("It won't be easy, but it's the best option for safety.")

def fields(family):
    pass

road_block(False)