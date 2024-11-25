import json
inventory = [1, 9]
items = open('items.json', 'r')
items = json.load(items)

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
            print("3. Open the toilet door")
            print("4. Go up the stairs")
            ans1 = input("What do you do? ")

            if ans1 == "1":
                print("You open the kitchen door to find it barren. There's a kitchen knife on the counter. Should you take it?")
                print("1. Take the knife")
                print("2. Leave the knife")
                ans2 = input("What do you do? ")

                if ans2 == "1":
                    inventory.append(2)  # Add the knife to inventory
                    print(items[1]["description"])
                    print("You feel the cold steel of the handle as you put it away.")
                elif ans2 == "2":
                    print("You leave the knife and continue searching.")
                else:
                    print("Invalid choice. Try again.")
                    continue

            elif ans1 == "2":
                print("You open the living room door and find it empty, with no signs of your family. The silence is unnerving.")
                # Add progression here

            elif ans1 == "3":
                print("You open the toilet door and find it locked. You wonder if something is hidden inside.")
                # Add progression here

            elif ans1 == "4":
                while True:
                    print("You decide to go upstairs. The stairs creak as you ascend, and your heart races with each step.")
                    print("You reach the top, where all the doors are closed. What do you do?")
                    print("1. Open Amber's door")
                    print("2. Open Chelsea's door")
                    print("3. Open your bedroom door")
                    print("4. Open the loft hatch")

                    ans2 = input("What do you do? ")
                
                    if ans2 == "1":
                        print("You open Amber's door and feel a strange sense of dread. The room is quiet. What do you find?")
                        # Add progression here

                    elif ans2 == "2":
                        print("You open Chelsea's door. It looks untouched, but the atmosphere feels thick. Her toys and books are lying scattered on the floor, nothing unusual here.")
                        continue
                        # Add progression here

                    elif ans2 == "3":
                        print("You open your bedroom door. Everything seems fine, but you still feel uneasy.")
                        # Add progression here

                    elif ans2 == "4":
                        print("You open the loft hatch. The stale air and chill run down your spine as you peer inside.")
                        # Add progression here

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