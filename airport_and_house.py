import json
inventory = [1, 9]
items = open('items.json', 'r')
items = json.load(items)
has_family = False

def airport():
    print("You feel the cool cloth of your bedsheets against your skin as you slowly come round, your eyes open and your sight is blurry but you can just about make out your room, you look to your right and see your wife asleep gently snoring.\nYou say your goodbyes and kiss her on the forehead before making your way downstairs. The morning light shining through, the beautiful colours of yellow and orange lighting the living room with a hint of red almost seeping through tainting the room.")
    print("You gather your things and get ready to head out the door before remembering you might need your car keys. Yeovils airport has never been the highest of quality but it does have the benefit of being close to home, the rundown walls and old technology, smells damp and there are signs of water damage.")
    print("\n")
    print("You sit on one of the rusty old seats and it almost sounds like its screaming for help from the pressure, although you knew it was going to happen, something felt off, you have a bad feeling about something but cant quite pin what it is.\n Deciding its just nerves about the flight you opt to ignore it, keeping your eyes on the display, watching all the flights including your own. You notice that a flight gets cancelled and then another.")
    print("A few minutes go by and then your flight gets cancelled, The nerves setting in doesn't help and so you approach the desk and ask whats going on, only to be told that they cant tell you. a gut feeling sinks in and you get the urge to leave.")
    print("You choose to ignore the feeling and once again take your seat waiting patiently. the longer you wait the more you see other flights being cancelled.\n \n A lot of people begin to swarm around the front desk shouting questions, deciding youd come back later for the flight in the evening you stand up and grab your suitcase.")
    print("as you turn your back to the swarm of people you cant help but notice a few of them are attacking each other, this isnt an uncommon thing to happen but they seem to be getting very agressive. as you take your first step onto the carpark outside a man sprints past you knocking you to the ground.")
    print("getting back up you see the same person who just ran past turning the corner, his red jumper was the only thing you could notice before he was gone. brushing yourself of, dazed and confused you pick up your suitcase.")
    print("You notice that a lot of people are hurrying to their cars, scrambling to open their doors, a few of them bleeding. You think there could have been an accident, maybe one of the old roofs collapsed? You get into your car, still confused about whats going on, and start to head home")
    print("\n")
    print("Fearing for the worst you make your way home, driving past houses that are eerily quiet, determined to get home to your family to make sure they are okay.")


def house():
    print("Upon reaching the house, you receive a notification. It reads: 'To all citizens, please remain calm and stay inside your houses, lock all your doors and close your windows. This is not a test...'")
    print("The realization of what's going on begins to kick in, and a thought crosses your mind. What if you didn't go get your family? What if they had been attacked? What if they were aggressive?")
    print("\n1. Go find your family")
    print("2. Abandon them")
    ans = input("What do you do? ")

    if ans == "1":
        print("You decide to find your family and drive toward the house, praying that they're safe.")
        print("When you arrive, the house is eerily quiet. No sign of your family. You start to look around. There are 3 doors: kitchen, living room, and toilet. Also, stairs lead up.")
        
        while True:
            print("\nWhat do you pick?")
            print("1. Open the kitchen door")
            print("2. Open the living room door")
            print("3. Open the Garage door")
            print("4. Go up the stairs")
            ans1 = input("What do you do? ")

            if ans1 == "1":
                print("You open the kitchen door to find it barren. There's a kitchen knife on the counter. Should you take it?")
                print("1. Take the knife")
                print("2. Leave the knife")
                ans2 = input("What do you do? ")

                if ans2 == "1":
                    inventory.append(1)  # Add the knife to inventory
                    print(items[1]["description"])
                    print("You feel the cold steel of the handle as you put it away.you check around the kitchen, looking under the tables making sure to look in every nook and cranny. They are not here. You return back to the hallway, knife sitting in your pocket")
                elif ans2 == "2":
                    print("You leave the knife and continue searching.you check around the kitchen, looking under the tables making sure to look in every nook and cranny. They are not here. You return back to the hallway")
                else:
                    print("Invalid choice. Try again.")
                    continue

            elif ans1 == "2":
                print("You open the living room door and find it empty, with no signs of your family. The silence is unnerving.")
                # Add progression here

            elif ans1 == "3":
                print("You open the garage door and enter the darkness, you feel the familiar placing of the lightswitch and illuminate the area, the light shining on your workpace.")
                print("you notice that your tools are still here and think to yourself that they could come in handy. You at first see your crowbar, an effective tool but also a deadly weapon if used right, Do you take it?")
                print("1. Take the crowbar")
                print("2. Leave the crowbar")
                ans5 = input("What do you do? ")

                if ans5 == "1":
                    inventory.append(0)
                    print("You take the crowbar and continue searching.")
                    pass

                elif ans5 == "2":
                    print("you leave the crowbar and continue searching.")
                    pass
                
                print("\nYou notice that your rope is still here from when you were planning to make a rope swing for your girls. it was meant to be a christmas present for them. Do you really want to take it? ")
                print("1. Take the Rope")
                print("2. Leave the Rope, maybe you can still make their present.")
                ans7 = input("What do you do? ")

                if ans7 == "1":
                    inventory.append(6)
                    print("You take the Rope and continue searching.")
                    pass

                elif ans7 == "2":
                    print("you leave the Rope and continue searching.")
                    pass

                print("\nAnd finally you see your trusty torch, a hand crank on the side allows for unlimited use, could be useful for dark areas or the night. Do you take it?")
                print("1. Take the Torch")
                print("2. Leave the Torch, How will you see in the dark?.")
                ans6 = input("What do you do? ")

                if ans6 == "1":
                    inventory.append(6)
                    print("You take the Torch and head back to the corridoor")
                    continue

                elif ans6 == "2":
                    print("you leave the Torch and head back to the corridoor.")
                    continue


            elif ans1 == "4":
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
                        while True:
                            print("You open the bathroom door. It looks untouched, but the atmosphere feels thick. theres still water in the bathtub, nothing unusual here. however you notice a rubber duck, bouncing off the walls of the tub. Maybe it could be useful?")
                            print("Take the duck?")
                            print("1, Yes")
                            print("2, No")

                            ans4 = input()

                            if ans4 =="1":
                                inventory.append(3)
                                break

                            elif ans4 =="2":
                                break

                            else:
                                print("Invalid choice. Please enter 1 or 2.")


                        print("on closer inspection of the bathroom you also happen to notice that the clean plunger is still sat in the corner, perhaps this could be of use?")
                        print("Take the clean plunger?")
                        print("1, Yes")
                        print("2, No")

                        ans4 = input()

                        if ans4 =="1":
                            inventory.append(2)
                            print("deciding that you had found everything needed from the bathroom you return to the stairs.")
                            break

                        elif ans4 =="2":
                            print("deciding that you had found everything needed from the bathroom you return to the stairs.")
                            break

                        else:
                            print("Invalid choice. Please enter 1 or 2.")

                        


                        
                        

                    elif ans2 == "3":
                        print("You open your bedroom door. Everything seems fine, but you still feel uneasy. Your wife is nowhere to be seen and it doesnt look like anythings changed")
                        # Add progression here

                    elif ans2 == "4":
                        print("You open the loft hatch. The stale air and chill run down your spine as you peer inside. the dark cold loft stares back at you, you swear you see something move in the corner, it seems to be getting closer to you. The panick sets in and you turn on your phones flashlight, just to see a face staring back at you,  at first you jump and are prepared to attack before hearing your wifes soft voice.")
                        print("your panick begins to become relief as you see your whole family up there. you climb up into the loft and ponder your options, you clould either stay up in the loft and hope for the best, or go out and try and find help, maybe the government have a safe zone.")

                        print("1, Stay with your family.")
                        print("2, try to find help with your family")
                        ans3 = input("What do you do?")

                        if ans3 == "1":
                            print("You decide to stay in the loft, hoping that you're safe up there with your family. You huddle together, waiting for the night to pass. you awake suddenly as you hear a crash coming from inside the house, deeming it too risky to go down you lock the hatch and tell your family never to go down there.\n As the days go past, the girls keep complaining that their stomachs hurt and that they are hungry, begging you to please get food, you reasure them that help will be here soon and that itll all be okay.\n you look to your wife to see how she is, and she is just sat in the corner, her once beautiful eyes blankly staring into the ground.\n \n You wake up feeling weak the next day, knowing that you wont live much longer, and you begin to smell something that feels off, you turn to your wife and notice her bony figure,\n she never did eat as much as you but you could tell that she wasnt with you anymore, the pain of starvation was more of an annoyance to you, knowing that your family were dying hurt tons more.\n the girls led down on the ground occasionally letting out a sniffle. at least it reasured you that they were okay for now. praying that someone would rescue you, all the while reassuring your girls that mum had just gone to a better place and they would all be seeing her soon.\n As the day went on, you knew that you wouldnt survive the night, and so, you huddled close with your girls holding them both close and looking at their bony faces for the last time, and your eyes start to fade, joining your wife and daughters in peace.")
                        elif ans3 == "2":
                            print("You decide to leave the loft and try to find help. You carefully climb back down and help your family down the ladder , beggining to prepare to search for safety.")
                            has_family = True
                        else:
                            print("Invalid choice. Please enter 1 or 2.")

                        # Add progression here

                    elif ans2 == "5":
                        pass        

                    

                    else:
                        print("Invalid choice. Try again.")
                        continue
                    break  # Exit the loop after making a decision

            else:
                print("Invalid input. Please choose a valid option.")
                continue

    elif ans == "2":
        print("You decide to abandon your family, reasoning that it's too risky to go after them.")
        # Add further progression here

    else:
        print("Invalid input. Please enter '1' to find your family or '2' to abandon them.")

# Call the function to start the game
house()