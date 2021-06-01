# create a variable named types_of_people and set it equal to 10
types_of_people = 10
# create a variable x and set it equal to a string containing the variable types_of_people in {}
x = f"There are {types_of_people} types of people."

# create a variable named binary and set it = (equal) to "binary"
binary = "binary"
# create a variable named do_not and set it = (equal) to "don't"
do_not = "don't"
# create a variable named y and set it equal to an f-string which has two variables inside {}
y = f"Those who know {binary} and those who {do_not}."

# print the value of the strings x and y to the screen, replacing the variable names inside {} with the values
print(x)
print(y)

# print the sentence to the screen, replacing the variable name {x} with the string value of x
print(f"I said: {x}")
# print the sentence to the screen, replacing the variable name {y} with the string value of y
print(f"I also said: '{y}'")

# create a variable named hilarious and set it equal to False
hilarious = False
# create a variable joke_evaluation and set it equal to a string with a placeholder for a variable at the end {}
joke_evaluation = "Isn't that joke so funny?! {}"

# print the value of joke_evaluation to the screen, replacing the {} with the value stored in the variable hilarious
print(joke_evaluation.format(hilarious))

# create a variable named w and set it equal to a string
w = "This is the left side of..."
# create a variable named e and set it equal to a string
e = "a string with a right side."

# print the value of w concatenated with the value of e
print(w + e)
