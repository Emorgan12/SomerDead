import os
#temporary. a value for this needs to be created when the player decides wether or not he takes the family to the base. delete this when it's made
with_family = True
#also temporary. not sure how the game is supposed to check for the keycard
has_keycard = True
#also also temporary. idk how the game will check if the player has the crowbar
has_crowbar = True

def mil_base_outskirts():
    ans = input("After a long walk along the heedgerows of the fields, you find yourself at a barbed wire fence with a sign reading \"NO ENTRY\". This must be the military base. You follow the fence west, as that must be where the entrance is.\n\nIn the distance, you can see the gate. Something is off. There is not a single person in sight. You get closer and realize that the gate has been forced open. Upon closer inspection, you notice bodies in and around the cars lined up in front of the gate. \nA firefight seems to have broken out between the military and an unknown third party, resulting in the death of a guard sitting in a gatehouse on the right side of the gate.\n\nSearch his body?\n\nY- Yes\nN- No\n\n")

    if ans == "y":
        print("A fowl stench attacks your nose. On his body, you obtain a keycard; but also another question: How is the guard's body emitting this stench if he's only died recently?\nYou brush it off and move on. As you leave, you feel like you saw something move in the corner of your eye.")
        #he obtains the keycard here
    else:
        print("Even as a top of the line biologist, dead bodies give you the ick. You decide to pass.")

    print("You walk through yet another open field, towards a group of buildings. While walking, you hear distant gunshots. Whoever was fighting at the gate has clearly made it inside.\nYou reach a statue infront of a building. The plaque on the building reads: \"MUNITIONS STORAGE\".\nSuddenly, an explosion causes you to stagger and hide behind the statue. A hole is blown through a hallway connecting the munitions storage to another building. You see silhouettes of soldiers firing and advancing through the smoke.\n\nA lightbulb turns on in your head. That hole would be the perfect way to enter the building, and hopefully find a bunker of sorts, with enough supplies to last the apocalypse. It is a military base, after all. \nYou make a run for the hole in the wall. Once inside, you take a left and run down hallways upon hallways filled with debris and smoke. Eventually, you find a flight of stairs that goes down. The smoke and debris has disappeared.\n\nWhile descending, a booming voice on the intercom invades your ears:\n\"ATTENTION ALL PERSONNEL, AN AIR STRIKE HAS BEEN ORDERED ON THIS BASE IN T-60 MINUTES. EVACTUATION HELICOPTERS HAVE BEEN CALLED TO SECTOR 4. IF YOU DO NOT EVACUATE, YOU WILL BE LEFT BEHIND.\nI REPEAT, AN AIR STRIKE HAS BEEN ORDERED ON THIS BASE IN T-60 MINUTES. EVACTUATION HELICOPTERS HAVE BEEN CALLED TO SECTOR 4. IF YOU DO NOT EVACUATE, YOU WILL BE LEFT BEHIND.\"\n\nYour heart sinks. You need to find this bunker, and fast.\n\nYou make your way down 10 or more flight of stairs, now at the bottom.\n\nYou see 6 or so doors. All but 1 are locked. Opening it reveales another hallway, with 2 doors at the end.\n\nOne of them is slightly ajar, while the other one is shut. You notice a keycard reader on the closed door.")

    if has_crowbar:
        print("Try to get the slightly open door unstuck.")
        print("Pry the door open with your crowbar.")
        
        if with_family:
            print("Get your wife to help you pry the door open.")
        
        ans2 = input()
    else:
        if with_family:
            print("Get your wife to help you pry the door open.")
        else:
            print("Try to get the slightly open door unstuck.")

            print("You try with all your might, but you cannot seem to get the door open. All those days you skipped the gym seem to have caught up to you... You survive the explosion, but find that your only way out is blocked by rubble. You eventually die hungry and alone.")
            #ending
    
    


mil_base_outskirts()