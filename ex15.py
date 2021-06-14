# import the argv module (argument variable/vector) which holds the arguments
# specified when running this script from the command line, from the sys package
from sys import argv
# unpack argv and assign it to the variables on the left, in that order
script, filename = argv

# assign the file called "filename" to a variable called txt
# open a file with the open() function
txt = open(filename)

# display this message on screen
print(f"Here's your file {filename}:")
# call a function named "read" on txt i.e. run the "read" command on it
# and print the results
print(txt.read())
# close the file
txt.close()

# Ask user to input the filename at the prompt
print("Type the filename again:")
# prompt the user and assign the value of what user typed in
#  to a variable named "file_again"
file_again = input("> ")

# assign the file to a variable called "txt_again"
# open a file, and return it as a file object
txt_again = open(file_again)

# read the file and print the output to the screen,
#  by calling the function "read()" on txt_again
# print the contents of the file
print(txt_again.read())
# close the file
txt_again.close()
