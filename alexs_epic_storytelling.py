import os
import time

inventory = []
has_wife = False


def mil_base_outskirts():

    x = True
    print("After a long walk along the heedgerows of the fields, you find yourself at a barbed wire fence with a sign reading \"NO ENTRY\". This must be the military base. You follow the fence west, as that must be where the entrance is.\n\nIn the distance, you can see the gate. Something is off. There is not a single person in sight. You get closer and realize that the gate has been forced open. Upon closer inspection, you notice bodies in and around the cars lined up in front of the gate. \nA firefight seems to have broken out between the military and an unknown third party, resulting in the death of a guard sitting in a gatehouse on the right side of the gate.\n\nSearch his body?\n\nSearch his body.\nContinue forward and ignore it.")

    while x:
        ans = input("\n\n")
        if ans == "Search his body.":
            print("A fowl stench assaults your nose. From his body, you obtain a keycard. Something bugs you, however: The guard has only died recently. How has his body rotten this badly?\nYou brush it off and move on. As you leave, you feel like you saw the body twitch.")
            inventory.append(9)
            x = False
        elif ans == "Continue forward and ignore it.":
            print("Even as a top of the line biologist, dead bodies give you the ick. You decide to pass.")
            x = False
        else:
            print("Invalid answer. Try again.")
            pass

    print("\nYou walk through yet another open field, towards a group of buildings. While walking, you hear distant gunshots. Whoever was fighting at the gate has clearly made it inside.\nYou reach a statue infront of a building. The plaque on the building reads: \"MUNITIONS STORAGE\".\nSuddenly, an explosion causes you to stagger and hide behind the statue. A hole is blown through a hallway connecting the munitions storage to another building. You see silhouettes of soldiers firing and advancing through the smoke.\n\nA lightbulb fires up in your head. That hole would be the perfect way to enter the building, and hopefully find a bunker of sorts, with enough supplies to last the apocalypse. It is a military base, after all.")
    print("You make a run for the hole in the wall. Once inside, you take a left and run down hallways upon hallways filled with debris and smoke. Eventually, you find a flight of stairs that goes down. The smoke and debris has disappeared.\n\nWhile descending, a booming voice on the intercom invades your ears:\n\"ATTENTION ALL PERSONNEL, AN AIR STRIKE HAS BEEN ORDERED ON THIS BASE IN T-60 MINUTES. EVACTUATION HELICOPTERS HAVE BEEN CALLED TO SECTOR 4. IF YOU DO NOT EVACUATE, YOU WILL BE LEFT BEHIND.\nI REPEAT, AN AIR STRIKE HAS BEEN ORDERED ON THIS BASE IN T-60 MINUTES. EVACTUATION HELICOPTERS HAVE BEEN CALLED TO SECTOR 4. IF YOU DO NOT EVACUATE, YOU WILL BE LEFT BEHIND.\"\n\nYour heart sinks. You need to find this bunker, and fast.\n\nYou make your way down 10 or more flight of stairs, now at the bottom.\n\nYou see 6 or so doors. All but 1 are locked. Opening it reveales another hallway, with 2 metal pocket doors at the end. They seem to be powered by hydraulics.\n\nOne of them is slightly ajar, while the other one is shut. You feel a cold air eminating from the door.")

    x = True

    print("\nWhat do you do?")
    
    print("\nTry opening the door by yourself.")
    if has_wife == True:
        print("\nGet your wife to help you open the door.")
    elif 1 in inventory:
        print("\nTry prying it open with your trusty crowbar.")
    
    ans = input("\n\n")

    while x:
        print("\nWhat do you do?")
    
        print("\nTry opening the door by yourself.")
        if has_wife == True:
            print("\nGet your wife to help you open the door.")
        elif 1 in inventory:
            print("\nTry prying it open with your trusty crowbar.")
        
        ans = input("\n\n")

        if ans == "Try opening the door by yourself.":
            print("\nYou try with all your might to open the door, but it just will not budge. Skipping the gym has come back to bite you.")

            if has_wife == False and 1 not in inventory:
                print("\nAnd, with no other option, you have no choice but to go back. However, going up the stairs reveals that an explosion has caused rubble to block the stairway. You are now completely isolated from civilization.\nYou eventually die, hungry and alone. Your family would also perish by themselves. The game will now close.")
                time.sleep(15)
                quit()
            x = False

        elif ans == "Get your wife to help you open the door.":
            print("\nYour wife is surprisingly strong. You both position yourselves and pull the door back. With that obstacle out of the way, you make your way inside.")
            x = False

        elif ans == "Try prying it open with your trust crowbar.":
            print("\nUsing leverage and a chunk of steel, you manage to force the door open. With the obstacle out of the way, you head inside.")
            x = False

    print("The room is very cold. You see 3 chambers, one of which is open, with a warm green light shining inside of it. The other 2 are closed, lit up by a red light. You use your sci-fi knowledge to deduct that they are probably cryo pods. You do not see any control panels in sight. However, you do see wires running from the cryo pods to another room that you can see into through a glass pane. The glass appears bulletproof, so you doubt you would have any luck breaking through it. You suddenly remember the other door. You go back outside the give the other door a closer look. You notice a keycard reader.")     


    
    
        
    




    
mil_base_outskirts()