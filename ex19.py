# define a functin called cheese_and_crackers
# that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print the value of the variables in {} in the sentences
    print(">>> cheese_and_crackers: cheese_count =", cheese_count, ", boxes_of_crackers =", boxes_of_crackers)
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
    print("<<<<\n")

print("We can just give the function numbers directly:")
# call the cheese_and_crackers function and
# specify the value 20 for cheese_count,
# and 30 for boxes_of_crackers
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# create a variable named amount_of_cheese / amount_of_crackers
# and assign the value 10 / 50 to it
amount_of_cheese = 10
amount_of_crackers = 50

# call the cheese_and_crackers function with the values
# of amount_of_cheese and amount_of_crackers assigned to
# cheese_count and boxes_of_crackers respectively
# and run the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# call the function with the result of 10 + 20 i.e. 30,
# and the result of 5 + 6 i.e. 11, assigned to
# cheese_count and boxes_of_crackers respectively,
# then run the function
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# call the function with two arguments, the first argument is
# the result of amount_of_cheese + 100 i.e. 10 + 100 i.e. 110
# and is assigned to cheese_count and the second argument is
# the result of amount_of_crackers + 1000 i.e. 50 +1000 i.e. 1050
# assigned to boxes_of_crackers, then run the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
