# create a variable named people with value 40
people = 40
cars = 4
trucks = 15


# if the boolean expression is true, execute the code in the block, otherwise skip it
if cars > people or trucks > people:
    print(">>> if cars > people or trucks > people:", cars, people, trucks)
    print("We should go somewhere")
# execute this condition if the above if boolean expression is false
# if the boolean expression is true, execute the code in the block, otherwise skip it
elif cars < people:
    print(">>> elif cars < people:", cars, people)
    print("We should not take the cars.")
# execute this condition if both the above if and elif boolean expressions are false
else:
    print (""We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars and people != 40 :
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
