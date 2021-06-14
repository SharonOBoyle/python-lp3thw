# Import the argv module, which is the argument variable which
# holds the arguments you pass to the Python script when you run it
from sys import argv
# read the WYSS section for how to run this
# Unpack the argv and assign it to all these variables, in order
script, first, second, third, fourth = argv

print(f"The script is called: {script}")
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)

fifth = input("Add another argument: ")
print("Your last argument is:", fifth)
