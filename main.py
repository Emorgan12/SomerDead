import os
import time
import json
from time import sleep
import os
from roadblock_fields import road_block, fields
from alexs_epic_storytelling import mil_base_outskirts
from airport_and_house import airport, house


items = open('items.json', 'r')
items = json.load(items)
inventory = []
has_family = False

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


#This function is fully completed. The keycard is obtained in this function. This function checks the inventory for the crowbar. This function checks if the character has his family with him by checking the "has_family" variable.
def mil_base_outskirts():

    x = True
    print("After a long walk along the heedgerows of the fields, you find yourself at a barbed wire fence with a sign reading \"NO ENTRY\". This must be the military base. You follow the fence west, as that must be where the entrance is.\n\nIn the distance, you can see the gate. Something is off. There is not a single person in sight. You get closer and realize that the gate has been forced open. Upon closer inspection, you notice bodies in and around the cars lined up in front of the gate. \nA firefight seems to have broken out between the military and an unknown third party, resulting in the death of a guard sitting in a gatehouse on the right side of the gate.\n\nSearch his body?\n\nSearch his body.\nContinue forward and ignore it.")

    while x:
        ans = input("\n\n")
        
        if ans == "Search his body.":
            print("A fowl stench assaults your nose. From his body, you obtain a keycard. Something bugs you, however: The guard has only died recently. How has his body rotten this badly?\nYou brush it off and move on. As you leave, you feel like you saw the body twitch.")
            inventory.append(8)
            x = False
        
        elif ans == "Continue forward and ignore it.":
            print("Even as a top of the line biologist, dead bodies give you the ick. You decide to pass.")
            x = False
        
        else:
            print("Invalid answer. Try again.")
            pass

    print("\nYou walk through yet another open field, towards a group of buildings. While walking, you hear distant gunshots. Whoever was fighting at the gate has clearly made it inside.\nYou reach a statue infront of a building. The plaque on the building reads: \"ORDINANCE STORAGE\".\nSuddenly, an explosion causes you to stagger and hide behind the statue. A hole is blown through a hallway connecting the munitions storage to another building. You see silhouettes of soldiers firing and advancing through the smoke.\n\nA lightbulb fires up in your head. That hole would be the perfect way to enter the building, and hopefully find a bunker of sorts, with enough supplies to last the apocalypse. It is a military base, after all.")
    print("You make a run for the hole in the wall. Once inside, you take a left and run down hallways upon hallways filled with debris and smoke. Eventually, you find a flight of stairs that goes down. The smoke and debris has disappeared.\n\nWhile descending, a booming voice on the intercom invades your ears:\n\"ATTENTION ALL PERSONNEL, AN AIR STRIKE HAS BEEN ORDERED ON THIS BASE IN T-60 MINUTES. EVACTUATION HELICOPTERS HAVE BEEN CALLED TO SECTOR 4. IF YOU DO NOT EVACUATE, YOU WILL BE LEFT BEHIND.\nI REPEAT, AN AIR STRIKE HAS BEEN ORDERED ON THIS BASE IN T-60 MINUTES. EVACTUATION HELICOPTERS HAVE BEEN CALLED TO SECTOR 4. IF YOU DO NOT EVACUATE, YOU WILL BE LEFT BEHIND.\"\n\nYour heart sinks. You need to find this bunker, and fast.\n\nYou make your way down 10 or more flight of stairs, now at the bottom.\n\nYou see 6 or so doors. All but 1 are locked. Opening it reveales another hallway, with 2 metal pocket doors at the end. They seem to be powered by hydraulics.\n\nOne of them is slightly ajar, while the other one is shut. You feel a cold air eminating from the door.")

    x = True

    print("\nWhat do you do?")
    
    print("\nTry opening the door by yourself.")
    
    if has_family == True:
        print("\nGet your wife to help you open the door.")
    
    elif 0 in inventory:
        print("\nTry prying it open with your trusty crowbar.")
    
    ans = input("\n\n")

    while x:
        print("\nWhat do you do?")
    
        print("\nTry opening the door by yourself.")
        
        if has_family == True:
            print("\nGet your wife to help you open the door.")
        
        elif 1 in inventory:
            print("\nTry prying it open with your trusty crowbar.")
        
        ans = input("\n\n")

        if ans == "Try opening the door by yourself.":
            print("\nYou try with all your might to open the door, but it just will not budge. Skipping the gym has come back to bite you.")

            if has_family == False and 1 not in inventory:
                print("\nAnd, with no other option, you have no choice but to go back. However, going up the stairs reveals that an explosion has caused rubble to block the stairway. You are now completely isolated from civilization.\nYou eventually die, hungry and alone. Your family would also perish by themselves.\n\nThe game will now close.")
                time.sleep(15)
                quit()
                #dies alone ending
            x = False

        elif ans == "Get your wife to help you open the door.":
            print("\nYour wife is surprisingly strong. You both position yourselves and pull the door back. With that obstacle out of the way, you make your way inside.")
            x = False

        elif ans == "Try prying it open with your trust crowbar.":
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
                ans = input("\nSacrifice yourself.\nSacrifice your wife.")
                if ans == "Sacrifice yourself.":
                    print("You decide to sacrifice yourself. You would not stand to see yourself throw away the love of your life like it is nothing. You say your goodbyes and wish them good luck. From the control room, you activate the cryo-pods and lock both doors. Now what? You start to think. You should be close to the ordinance building. Maybe you could find a way to escape the military base?\nYou head back through the endless hallways and the 10 flights of stairs. The smoke suffocating the hallways on the first floor is now gone. You head to the end of the hall and find an open door.\nInside, you find kilograms upon kilograms of C4 explosives. You're a thrifty individual, so you easily figure out how you could wire them to detonate. You also spot a bag, which would make it easier to carry all this C4. Might as well go out with a bang.\nYou go through the hallways, looking for a good spot to make your last stand. You loot countless bodies for weapons and ammunition, until you head a gunshot up ahead.\nIt came from an injured bandit putting themselves out in the cafeteria. You found your last stand. You set the C4. In total, it has been roughly 40 minutes since the announcement. The helicopters seem to have left early, probably due to the masses of zombies swarming the heli-pads outside.\nYou notice a lit flare and try to find some that havent been lit, to grab the attention of the zombies. Bingo!\nArmed to the teeth and having set up your explosive coffin, you go outside and light a flare, screaming as loudly as possible. A horde of zombies screams out in unison, slowly devolving into a gargle of grunts and moans.\nYou run back inside and take position behind a counter. The way the cafeteria is layed out, the zombies funnel in through one hallway only. You fight endlessly, taking out hundreds of zombies until you run out of ammo.\nAs you get overrun by zombies and your finger is on the detonator, the air strike hits the military base just in time. The base goes off like a firework. You, along with the other thousands of zombies, are obliterated.\n\n10 years later, your wife and children are found by the MI6, expecting to find you. The zombies, after 10 years, were so rotten, that they were practically walking bones, and thus, collapsed for the last time. Your family is now free, living happily ever after. You now watch over them from the afterlife. Not too bad, actually.\n\nThe game will now close.")
                    time.sleep(15)
                    quit()
                    #sacrifice yourself and save your family ending

                elif ans == "Sacrifice your wife.":
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
        stay = house() 
    if stay:
        exit()
    road_block(family)
    fields(family)
    mil_base_outskirts(family)
    #mil_base(family)
    
if __name__ == "__main__":
    main()