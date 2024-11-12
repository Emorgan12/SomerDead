def mil_base_outskirts():
    ans = input("After a long walk along the heedgerows of the fields, you find yourself at a barbed wire fence with a sign reading \"NO ENTRY\". This must be the military base. You follow the fence west, as that must be where the entrance is.\n\nIn the distance, you can see the gate. Something is off. There is not a single person in sight. You get closer and realize that the gate has been forced open. Upon closer inspection, you notice bodies in and around the cars lined up in front of the gate. \nA firefight seems to have broken out between the military and an unknown third party, resulting in the death of a guard sitting in a gatehouse on the right side of the gate.\n\nSearch his body?\n\nY- Yes\nN- No\n\n")

    if ans == "y":
        os.system("cls")
        print("A fowl stench attacks your nose. On his body, you obtain a keycard; but also another question: How is the guard's body emitting this stench if he's only died recently?\nYou brush it off and move on. As you leave, you feel like you saw something move in the corner of your eye.")
        #he obtains the keycard here
    else:
        os.system("cls")
        print("Even as a top of the line biologist, dead bodies give you the ick. You decide to pass.")

    print("You walk through yet another open field, towards a group of buildings.  One of them reads: \"MUNITIONS STORAGE\"")

    
def mil_base():
    pass