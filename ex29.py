people = 2
cats = 3
dogs = 1


if people < cats:
    print(">> first if statement (<) ", people, cats)
    print("Too many cats! The world is doomed!")

if people > cats:
    print(">> second if statement (>) ", people, cats)
    print("Not many cats! The world is saved!")

if people < dogs:
    print(">> third if statement (<) ", people, dogs)
    print("The world is drooled on!")

if people > dogs:
    print(">> fourth if statement (>) ", people, dogs)
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print(">> fifth if statement (>=) ", people, dogs)
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print(">> sixth if statement (<=) ", people, dogs)
    print("People are less than or equal to dogs.")


if people == dogs:
    print(">> seventh if statement (==) ", people, dogs)
    print("People are dogs.")


# other Boolean expressions
cats -= 20
dogs -= 10

if people > dogs and people > cats:
    print("There are more people than animals.")

if dogs <= 5 and cats <= 5:
    print("There are very few animals.")

if not(dogs <= 5 and cats <= 5):
    print("There are enough animals.")
