print("""You see two caves in the distance.
Do you go into cave #1 or cave #2""")

cave = input("> ")

if cave == "1":
    print(">>> in cave #1")
    print("""In the darkness you see two doors.
    Which one do you choose, door #1 or door #2 ?""")

    door = input("> ")

    if door == "1":
        print("You entered door #1")
        print("""You see a beautiful valley.
        In the distance there is a castle to the east and a forest to the west.
        Do you go towards the castle (#1) or the forest (#2)?""")

        towards = input("> ")

        if towards == "1":
            print("""You enjoy the walk to the castle and the king and queen celebrate your arrival.
            They invite you to stay in this paradise with them forever.
            Should you stay (#1) or should you go (#2)?""")

            stay_go = input("> ")

            if stay_go == "1":
                print("You stay with the king and queen and all live happily ever after.  You win!")

            elif stay_go == "2":
                print("""You leave the castle and fall asleep at the side of the road.
                Suddenly you wake up and realise it has all been a beautiful dream.  You win! """)

            else:
                print("Unacceptable answer.  The king and queen get angry and throw you in jail.  You lose!")

    elif door == "2":
        print("You entered door #2")
        print("You have exited the game.  Good bye!")

    else:
        print("Sorry that is not an option. You lose!")

elif cave == "2":
    print(">>> in cave #2")
    print("""It is completely dark and you feel afraid.
    You see a light in the distance and walk towards it carefully.
    As you approach you see that there are actually two lights,
    one towards the left (#1), and the other towards the right (#2).
    Which direction do you choose?""")

    light = input("> ")

    if light == "1":
        print("Walking towards the light on the left guides you safely home.  You win!")

    elif light == "2":
        print("""Walking towards the ligth on the right, the light gets brighter with each step.
        Your eyes are blinded and you faint.
        When you wake up, you realise it has all been a dream.  You win!""")

    else:
        print("""You don't move.  Too late! a trapdoor underneath your feet opens and you fall into the sea below.
        Fortunately, a lifeboat is there to save you and bring you home.  You win!""")
else:
    print("That's probably the wisest choice.  You win!")
