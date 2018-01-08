print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There is a giant bear here eathing a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door  == "2":
    print("You stare into the endless abyss at Cthulhu's retreat.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    elif insanity == "2":
        print("input is 2 on 2-1")
    elif insanity == "3":
        print("input is 3 on 2-1")
    else:
        print("The insanity rots your eyes into a pool of mustard.")
        print("Good job!")
else:
        print("You stumble around and fall on a knife and die. Good job!")
