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
    print("Upon reaching the house you recieve a notification, it reads 'To all citizens, please remain calm and stay inside of your houses, lock all your doors and close your windows, This is not a test. if you encounter someone who is acting off or seemingly agressive please do your best to avoid them.")
    print("the realisation of whats really going on begins to kick in, and a thought crosses your mind, what if you didnt go get your family? what if they had been attacked? what if they were aggressive and tried to harm you?  do you want to take that risk?")
    print("\n")
    print("Look for your family (1)")
    print("Leave them (2)")
    hawk2a = input("What do you do? ")
    if hawk2a == "1":
        return True
    
    elif hawk2a == "2":
        return False



def main():
   

    airport()
    stay = house()
    if stay:
        exit() 
if __name__ == "__main__":
    main()