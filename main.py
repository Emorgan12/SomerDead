import os
import time
import json
from time import sleep
from os import system


items = open('items.json', 'r')
items = json.load(items)
inventory = []
has_family = False

def pizza_guy():
    print("You can answer the door (1)")
    print("Or you can ignore the door (2)")
    answer = input("What do you do? ")
    if answer == "1":
        system('cls')
        print("You open the door to see who it is. It's just the pizza delivery guy. You take the pizza and pay him. You close the door and go back to the living room.")
        print("You sit back down on the couch and continue watching your daughters play.")
        return
    elif answer == "2":
        system('cls')
        print("You ignore the door and continue watching your daughters play. The knocking continues. You decide to ignore it and continue watching your daughters play.")
        print("There's a shout, it's the pizza delivery guy, announcing he's here")
        pizza_guy()
    else:
        system('cls')
        print("Invalid input. Please try again.")
        pizza_guy()

def item_drop():

    print("Your inventory is full, please choose an item to drop:")
    for item in inventory:
        print(str(items[item]+ ' ' + ["id"])+items[item]["name"])
    ans = input('\n')
    if ans in inventory:
        print("Dropped" + items[ans]["name"])
        return ans
    else:
        item_drop()
def title():
    system('cls')
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
    sleep(3)
    system('cls')
    print("The evening continues as it usually would on a Friday, with you and your family enjoying each other's company. You decide to go to bed early, as you have a long day ahead of you tomorrow.")
    sleep(3)
    system('cls')
    print("You've been invited to the Amazon Rainforest as part of a research team by the MI6, you're an incredible scientist, one of the best in your field. \nA new virus has been found due to the deforestation. You're excited to go, but you're also nervous. You've never been to the Amazon before, and you've heard stories of people getting lost in the forest and never being found \nAnd this virus could turn out to be deadly.")
    sleep(10)
    system('cls')
def downstairs():
    print("The house is eerily quiet. No sign of your family. You start to look around. There are 3 doors: kitchen, living room, and toilet. Also, stairs lead up.")
    
    while True:
        print("\nWhat do you pick?")
        print("1. Open the kitchen door")
        print("2. Open the living room door")
        print("3. Open the Garage door")
        print("4. Go up the stairs")
        ans1 = input("What do you do? ")

        if ans1 == "1":
            kitchen()

        elif ans1 == "2":
            print("You open the living room door and find it empty, with no signs of your family. The silence is unnerving.")

        elif ans1 == "3":
            garage()


        elif ans1 == "4":
            return upstairs()

def kitchen():
    if 1 not in inventory:
        print("You open the kitchen door to find it barren. There's a kitchen knife on the counter. Should you take it?")
        print("1. Take the knife")
        print("2. Leave the knife")
        ans2 = input("What do you do? ")

        while ans2 != "1" or ans2 != "2":
            if ans2 == "1":
                if len(inventory) == 5:
                    item = item_drop()
                    inventory.remove(item)
                inventory.append(1)  # Add the knife to inventory
                print("You feel the cold steel of the handle as you put it away.you check around the kitchen, looking under the tables making sure to look in every nook and cranny. They are not here. You return back to the hallway, knife sitting in your pocket")
                break
            elif ans2 == "2":
                print("You leave the knife and continue searching.you check around the kitchen, looking under the tables making sure to look in every nook and cranny. They are not here. You return back to the hallway")
                break
            else:
                print("Invalid choice. Try again.")
                
    else:
        print("You open the kitchen door to find it barren, no signs of your familly in here")

def garage():
    print("You open the garage door and enter the darkness, you feel the familiar placing of the lightswitch and illuminate the area, the light shining on your workpace.")
            
    if 6 not in inventory:
        print("\nYou notice that your rope is still here from when you were planning to make a rope swing for your girls. it was meant to be a christmas present for them. Do you really want to take it? ")
        while True:
            print("1. Take the Rope")
            print("2. Leave the Rope, maybe you can still make their present.")
            ans7 = input("What do you do? ")

            if ans7 == "1":
                if len(inventory) == 5:
                    item = item_drop()
                    inventory.remove(item)
                inventory.append(6)
                print("You take the Rope and continue searching.")
                break
                

            elif ans7 == "2":
                print("you leave the Rope and continue searching.")
            
    if 7 not in inventory:
        print("\nAnd finally you see your trusty torch, a hand crank on the side allows for unlimited use, could be useful for dark areas or the night. Do you take it?")
        while True:
            print("1. Take the Torch")
            print("2. Leave the Torch, How will you see in the dark?.")
            ans6 = input("What do you do? ")

            if ans6 == "1":
                if len(inventory) == 5:
                    item = item_drop()
                    inventory.remove(item)
                inventory.append(7)
                print("You take the Torch and head back to the corridoor")
                break

            elif ans6 == "2":
                print("you leave the Torch and head back to the corridoor.")
                continue
def upstairs():
    print("You decide to go upstairs. The stairs creak as you ascend, and your heart races with each step.")
    while True:
        print("You reach the top, where all the doors are closed. What do you do?")
        print("1. Open the girls door")
        print("2. Open The bathroom door")
        print("3. Open your bedroom door")
        print("4. Open the loft hatch")
        print("5, Go back downstairs")

        ans2 = input("What do you do? ")
    
        if ans2 == "1":
            print("You open the girls door and feel a strange sense of dread. The room is quiet. The pink vibrant walls feeling seamingly dull, their toys and books lay scattered on the floor.\n You take a few steps into the room and check the girls closet hoping to find one of them hiding. No Luck. your family isnt here. You return back to the to the top of the stairs.")
            continue


        elif ans2 == "2":
            bathroom()

        elif ans2 == "3":
            print("You open your bedroom door. Everything seems fine, but you still feel uneasy. Your wife is nowhere to be seen and it doesnt look like anythings changed")
            # Add progression here

        elif ans2 == "4":
            return loft()

        elif ans2 == "5":
            downstairs()        
        else:
            print("Invalid choice. Try again.")
            continue
        continue  # Exit the loop after making a decision

def bathroom():
    if 3 not in inventory:
        print("You open the bathroom door. It looks untouched, but the atmosphere feels thick. theres still water in the bathtub, nothing unusual here. however you notice a rubber duck, bouncing off the walls of the tub. Maybe it could be useful?")
        while True:
            print("Take the duck?")
            print("1, Yes")
            print("2, No")

            ans4 = input()

            if ans4 =="1":
                if len(inventory) == 5:
                    item = item_drop()
                    inventory.remove(item)
                print("You pick up the duck, it quacks softly")
                inventory.append(3)
                break

            elif ans4 =="2":
                print("You leave the duck, it's probably useless")
                break

            else:
                print("Invalid choice. Please enter 1 or 2.")
    else:
        print("You open the bathroom door. It looks untouched, but the atmosphere feels thick. theres still water in the bathtub, nothing unusual here.")

    while 2 not in inventory:
        print("on closer inspection of the bathroom you also happen to notice that the clean plunger is still sat in the corner, perhaps this could be of use?")
        print("Take the clean plunger?")
        print("1, Yes")
        print("2, No")

        ans8 = input()

        if ans8 =="1":
            if len(inventory) == 5:
                item = item_drop()
                inventory.remove(item)
                continue
            print("This'll be inconvienient to carry but it might come in handy.")
            inventory.append(2)
            print("deciding that you had found everything needed from the bathroom you return to the stairs.")
            break

        elif ans8 =="2":
            print("deciding that you had found everything needed from the bathroom you return to the stairs.")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")
def loft():
    print("You open the loft hatch. The stale air and chill run down your spine as you peer inside. the dark cold loft stares back at you, you swear you see something move in the corner, it seems to be getting closer to you. The panick sets in and you turn on your phones flashlight, just to see a face staring back at you,  at first you jump and are prepared to attack before hearing your wifes soft voice.")
    print("your panic begins to become relief as you see your whole family up there. you climb up into the loft and ponder your options, you clould either stay up in the loft and hope for the best, or go out and try and find help, maybe the government have a safe zone.")

    print("1, Stay with your family.")
    print("2, leave with your family and try to find help")
    ans3 = input("What do you do? ")

    if ans3 == "1":
        print("You decide to stay in the loft, hoping that you're safe up there with your family. You huddle together, waiting for the night to pass. you awake suddenly as you hear a crash coming from inside the house, deeming it too risky to go down you lock the hatch and tell your family never to go down there.\n As the days go past, the girls keep complaining that their stomachs hurt and that they are hungry, begging you to please get food, you reasure them that help will be here soon and that itll all be okay.\n you look to your wife to see how she is, and she is just sat in the corner, her once beautiful eyes blankly staring into the ground.\n \n You wake up feeling weak the next day, knowing that you wont live much longer, and you begin to smell something that feels off, you turn to your wife and notice her bony figure,\n she never did eat as much as you but you could tell that she wasnt with you anymore, the pain of starvation was more of an annoyance to you, knowing that your family were dying hurt tons more.\n the girls laid down on the ground occasionally letting out a sniffle. at least it reasured you that they were okay for now. praying that someone would rescue you, all the while reassuring your girls that mum had just gone to a better place and they would all be seeing her soon.\n As the day went on, you knew that you wouldn't survive the night, and so, you huddled close with your girls holding them both close and looking at their bony faces for the last time, and your eyes start to fade, joining your wife and daughters in peace.")
        return True, inventory
    elif ans3 == "2":
        print("You decide to leave the loft and try to find help. You carefully climb back down and help your family down the ladder , beggining to prepare to search for safety.")
        return False, inventory
    else:
        print("Invalid choice. Please enter 1 or 2")

def airport():
    print("You feel the cool cloth of your bedsheets against your skin as you slowly come round, your eyes open and your sight is blurry but you can just about make out your room, you look to your right and see your wife asleep gently snoring.\nYou say your goodbyes and kiss her on the forehead before making your way downstairs.")
    time.sleep(5)
    print("The morning light shining through, the beautiful colours of yellow and orange lighting the living room with a hint of red almost seeping through tainting the room.")
    time.sleep(5)
    system('cls')
    print("You gather your things and get ready to head out the door before remembering you might need your car keys. Yeovil's airport has never been the highest of quality but it does have the benefit of being close to home, the rundown walls and old technology, smells damp and there are signs of water damage.")
    time.sleep(7)
    system('cls')
    print("You sit on one of the rusty old seats and it almost sounds like its screaming for help from the pressure, although you knew it was going to happen, something felt off, you have a bad feeling about something but cant quite pin what it is.\n Deciding its just nerves about the flight you opt to ignore it, keeping your eyes on the display, watching all the flights including your own. You notice that a flight gets cancelled and then another.")
    time.sleep(10)
    system('cls')
    print("A few minutes go by and then your flight gets cancelled, The nerves setting in doesn't help and so you approach the desk and ask whats going on, only to be told that they cant tell you. a gut feeling sinks in and you get the urge to leave.")
    time.sleep(10)
    system('cls')
    print("You choose to ignore the feeling and once again take your seat waiting patiently. the longer you wait the more you see other flights being cancelled.\n \n A lot of people begin to swarm around the front desk shouting questions, deciding youd come back later for the flight in the evening you stand up and grab your suitcase.")
    time.sleep(5)
    print("as you turn your back to the swarm of people you cant help but notice a few of them are attacking each other, this isnt an uncommon thing to happen but they seem to be getting very agressive. as you take your first step onto the carpark outside a man sprints past you knocking you to the ground.")
    time.sleep(12)
    system('cls')
    print("getting back up you see the same person who just ran past turning the corner, his red jumper was the only thing you could notice before he was gone. brushing yourself of, dazed and confused you pick up your suitcase.")
    time.sleep(5)
    print("You notice that a lot of people are hurrying to their cars, scrambling to open their doors, a few of them bleeding. You think there could have been an accident, maybe one of the old roofs collapsed? You get into your car, still confused about whats going on, and start to head home")
    time.sleep(10)
    system('cls')
    print("Fearing for the worst you make your way home, driving past houses that are eerily quiet, determined to get home to your family to make sure they are okay.")
    time.sleep(10)
    system('cls')
    print("Upon reaching the house, you receive a notification. It reads: 'To all citizens, please remain calm and stay inside your houses, lock all your doors and close your windows. This is not a test...'")
    print("The realization of what's going on begins to kick in, and a thought crosses your mind. What if you didn't go get your family? What if they had been attacked? What if they were aggressive?")
    while True:
        print("\n1. Go find your family")
        print("2. Abandon them")
        ans = input("What do you do? ")

        if ans == "1":
            return True
        elif ans == "2":
            print("You decide to abandon your family, reasoning that it's too risky to go after them.")
            return False
        else:
            print("Invalid input, please enter 1 or 2")

def house():
    print("You decide to find your family and drive toward the house, praying that they're safe.")
    return downstairs()

def road_block(family):
    system('cls')
    print("You leave your house and jump in the car.")
    sleep(2)
    if family:
        print("Your daughters are in the back and your wife is next to you in the passenger seat. Everyone is worriedly silent, not sure what to say to make the mood lighter.")
    else:
        print("The car is eerily silent until you see some form of civilization.")
    sleep(2)
    print("There's a road block ahead. People are running everywhere and there's no chance of getting a car through this cha")
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

    print("You walk for a little while longer until something catches your eye, it's silver and shiny")
    sleep(2)
    print("On closer inspection, you realise it's a crowbar. Do you take it?")
    while True:
        sleep(0.5)
        print("1. Take the crowbar")
        print("2. Leave the crowbar \n")
        
        ans = input()
        if ans == "1":
            if len(inventory) == 5:
                item = item_drop()
                inventory.remove(item)
                continue
            sleep(2)
            print("You take the crowbar, it could come in handy.")
            inventory.append(1)
            break
        if ans == "2":
            sleep(2)
            print("You leave the crowbar, it'll be too difficult to carry with you.")
            break
        else:
            sleep(2)
            print("Invalid input")
    print("You continue walking for about 30 minutes until you spot your destination up ahead")
    return inventory

def mil_base(has_family):
    sleep(10)
    x = True
    print("After a long walk along the heedgerows of the fields, you find yourself at a barbed wire fence with a sign reading \"NO ENTRY\". This must be the military base. You follow the fence west, as that must be where the entrance is.\n\nIn the distance, you can see the gate. Something is off. There is not a single person in sight. You get closer and realize that the gate has been forced open. Upon closer inspection, you notice bodies in and around the cars lined up in front of the gate. \nA firefight seems to have broken out between the military and an unknown third party, resulting in the death of a guard sitting in a gatehouse on the right side of the gate.\n\nSearch his body?\n\n1. Search his body.\n2. Continue forward and ignore it.")
    while x:
        ans = input("\n\n")
        
        if ans == "1":
            if len(inventory) == 5:
                item = item_drop()
                inventory.remove(item)
                continue
            print("A fowl stench assaults your nose. From his body, you obtain a keycard. Something bugs you, however: The guard has only died recently. How has his body rotten this badly?\nYou brush it off and move on. As you leave, you feel like you saw the body twitch.")
            inventory.append(8)
            x = False
        
        elif ans == "2":
            print("Even as a top of the line biologist, dead bodies give you the ick. You decide to pass.")
            x = False
        
        else:
            print("Invalid answer. Try again.")
            pass

    print("\nYou walk through yet another open field, towards a group of buildings. While walking, you hear distant gunshots. Whoever was fighting at the gate has clsly made it inside.\nYou reach a statue infront of a building. The plaque on the building reads: \"ORDINANCE STORAGE\".\nSuddenly, an explosion causes you to stagger and hide behind the statue. A hole is blown through a hallway connecting the munitions storage to another building. You see silhouettes of soldiers firing and advancing through the smoke.\n\nA lightbulb fires up in your head. That hole would be the perfect way to enter the building, and hopefully find a bunker of sorts, with enough supplies to last the apocalypse. It is a military base, after all.")
    print("You make a run for the hole in the wall. Once inside, you take a left and run down hallways upon hallways filled with debris and smoke. Eventually, you find a flight of stairs that goes down. The smoke and debris has disappeared.\n\nWhile descending, a booming voice on the intercom invades your ears:\n\"ATTENTION ALL PERSONNEL, AN AIR STRIKE HAS BEEN ORDERED ON THIS BASE IN T-60 MINUTES. EVACTUATION HELICOPTERS HAVE BEEN CALLED TO SECTOR 4. IF YOU DO NOT EVACUATE, YOU WILL BE LEFT BEHIND.\nI REPEAT, AN AIR STRIKE HAS BEEN ORDERED ON THIS BASE IN T-60 MINUTES. EVACTUATION HELICOPTERS HAVE BEEN CALLED TO SECTOR 4. IF YOU DO NOT EVACUATE, YOU WILL BE LEFT BEHIND.\"\n\nYour heart sinks. You need to find this bunker, and fast.\n\nYou make your way down 10 or more flight of stairs, now at the bottom.\n\nYou see 6 or so doors. All but 1 are locked. Opening it reveales another hallway, with 2 metal pocket doors at the end. They seem to be powered by hydraulics.\n\nOne of them is slightly ajar, while the other one is shut. You feel a cold air eminating from the door.")

    x = True


    while x:
        print("\nWhat do you do?")
    
        print("\n1. Try opening the door by yourself.")
        
        if has_family:
            print("\n2. Get your wife to help you open the door.")
        
        elif 1 in inventory:
            print("\n2. Try prying it open with your trusty crowbar.")
        
        ans = input("\n\n")

        if ans == "1":
            print("\nYou try with all your might to open the door, but it just will not budge. Skipping the gym has come back to bite you.")

            if has_family == False and 1 not in inventory:
                print("\nAnd, with no other option, you have no choice but to go back. However, going up the stairs reveals that an explosion has caused rubble to block the stairway. You are now completely isolated from civilization.\nYou eventually die, hungry and alone. Your family would also perish by themselves.\n\nThe game will now close.")
                time.sleep(15)
                quit()
                #dies alone ending
            x = False

        elif has_family and ans == "2":
            print("\nYour wife is surprisingly strong. You both position yourselves and pull the door back. With that obstacle out of the way, you make your way inside.")
            x = False

        elif (not has_family) and ans == "2":
            print("\nUsing leverage and a chunk of steel, you manage to force the door open. With the obstacle out of the way, you head inside.")
            x = False

        else:    
            print("Invalid answer. Try again.")
            pass

    print("The room is very cold. You see 3 chambers, one of which is open, with a warm green light shining inside of it. The other 2 are closed, lit up by a red light. You use your sci-fi knowledge to deduct that they are probably cryo-pods. You do not see any control panels in sight. However, you do see wires running from the cryo pods to another room that you can see into through a glass pane. The glass appears bulletproof, so you doubt you would have any luck breaking through it. You suddenly remember the other door. You go back outside the give the other door a closer look. You notice a keycard reader.")     

    if 8 in inventory:
        print("You suddenly remember the key card you picked up off of the dead guard. You try it on the keycard reader. You hear 2 short beeps, accompanied by a green LED turning on, and the door opens. Inside, you see a control panel with controls to the cryo pods.")
        
        if has_family == True:
            x = True
            print("There are 4 of you and only 1 operational cryopod, so obviously, you enable the other ones. Now you face a different conundrum: There are 3 cryo-pods, so who's going to be left behind?\nYou return to the room, all cryo-pods operational, and explain the situation. Your 2 kids are already in the pods.\nYour wife says she is willing to sacrifice herself. What do you do?")
            
            while x:
                ans = input("\n1. Sacrifice yourself.\n2. Sacrifice your wife.")
                if ans == "1":
                    print("You decide to sacrifice yourself. You would not stand to see yourself throw away the love of your life like it is nothing. You say your goodbyes and wish them good luck. From the control room, you activate the cryo-pods and lock both doors. Now what? You start to think. You should be close to the ordinance building. Maybe you could find a way to escape the military base?\nYou head back through the endless hallways and the 10 flights of stairs. The smoke suffocating the hallways on the first floor is now gone. You head to the end of the hall and find an open door.\nInside, you find kilograms upon kilograms of C4 explosives. You're a thrifty individual, so you easily figure out how you could wire them to detonate. You also spot a bag, which would make it easier to carry all this C4. Might as well go out with a bang.\nYou go through the hallways, looking for a good spot to make your last stand. You loot countless bodies for weapons and ammunition, until you head a gunshot up ahead.\nIt came from an injured bandit putting themselves out in the cafeteria. You found your last stand. You set the C4. In total, it has been roughly 40 minutes since the announcement. The helicopters seem to have left early, probably due to the masses of zombies swarming the heli-pads outside.\nYou notice a lit flare and try to find some that havent been lit, to grab the attention of the zombies. Bingo!\nArmed to the teeth and having set up your explosive coffin, you go outside and light a flare, screaming as loudly as possible. A horde of zombies screams out in unison, slowly devolving into a gargle of grunts and moans.\nYou run back inside and take position behind a counter. The way the cafeteria is layed out, the zombies funnel in through one hallway only. You fight endlessly, taking out hundreds of zombies until you run out of ammo.\nAs you get overrun by zombies and your finger is on the detonator, the air strike hits the military base just in time. The base goes off like a firework. You, along with the other thousands of zombies, are obliterated.\n\n10 years later, your wife and children are found by the MI6, expecting to find you. The zombies, after 10 years, were so rotten, that they were practically walking bones, and thus, collapsed for the last time. Your family is now free, living happily ever after. You now watch over them from the afterlife. Not too bad, actually.\n\nThe game will now close.")
                    time.sleep(15)
                    quit()
                    #sacrifice yourself and save your family ending

                elif ans == "2":
                    print("You take your wife's word and go inside the cryopod. After saying your goodbyes, she activates the cryo-pods and locks both doors. The last image in your mind is of a blurry outside, with your wife being merely a figure on the outside of the condensating glass. You suddenly awake to pressure being let out of your pod. It's the MI6. They have come to retrieve you. After all, you are still an important asset. You catch a glimpse of a skeleton sitting in the corner of the control room. The apocalypse has ended, as all the zombies eventually became so rotten they were mere bones, and thus, the virus went extinct. You organize a funeral for your wife, and go back to your job as a biologist, raising your kids. You sometimes feel bittersweet that your wife did not survive, but at least you have your kids. Life is good again.\n\nThe game will now end.")
                    time.sleep(15)
                    quit()
                    #sacrifice your wife and live with your kids ending

                else:    
                    print("Invalid answer. Try again.")
                    pass
                
        else:
            print("You enter the room, but there's not much to do here. You're alone after all. You can enable the cryo-pods from the inside, so you have no need to enable them from here.\nYou return to the single operational cryo-pod and hop in. Activating it, your conciousness is starting to fade. Your last thoughts are about your family.\n\nYou think back to the house and feel guilt over leaving your family behind, now knowing that you could save them.\n\nYou truly are a monster. Eventually, you are woken up by MI6 agents. Your contacts prove valuable.\nIt has been 10 years, and the apocalypse has blown over. The zombies decomposed to the point of collapse, causing all infected to die off.\n\nYou return to your job as a biologist, but life feels empty, because your family has disappeared. Nobody to come home to. You survived, but at what cost?\n\nThe game will now close.")
            time.sleep(15)
            quit()
            #solo survival ending
    
    else:
        
        if has_family == False:
            print("The door will not open. You return to the single operational cryo-pod and hop in. Activating it, your conciousness is starting to fade. Your last thoughts are about your family.\n\nYou think back to the house and feel guilt over leaving your family behind, now knowing that you could save them.\n\nYou truly are a monster. Eventually, you are woken up by MI6 agents. Your contacts prove valuable.\nIt has been 10 years, and the apocalypse has blown over. The zombies decomposed to the point of collapse, causing all infected to die off.\n\nYou return to your job as a biologist, but life feels empty, because your family has disappeared. Nobody to come home to. You survived, but at what cost?\n\nThe game will now close.")
            time.sleep(15)
            quit()
        print("You do not have a keycard that would open the door. Maybe you should have checked the dead guard's body, back at the entrance.\nYou return back to the cryo-pod room. You face a conundrum: There are 4 of you, and only 1 cryo-pod. After a long debate, you realize that the cryo-pod is spatious enough to fit all 4 of you.\nYou all get into the cryo-pod and activate it, hoping to wake up in a better place. Too bad you did not read the warning on the side of the machine, saying that the machine overloads when more than 1 person get into the pod...\n\nThough, you all ended up in a better place, at least when compared to the real world. The machine exploded and the insides of the chamber were covered by a layer of red.\n\nThe game will now close.")
        time.sleep(15)
        quit()
        #family dies at cryo-pod ending
    

def main():
    title()
    tutorial()
    family = airport()
    if family:
        stay, inventory = house() 
        if stay:
            exit()
    road_block(family)
    inventory = fields(family)
    mil_base(family) 
    
if __name__ == "__main__":
    main()