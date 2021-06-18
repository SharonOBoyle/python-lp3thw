# import argv module from sys package
# argv holds the arguments specified on the command line
# when running this script
from sys import argv

# unpack argv and assign it to the variables on the left, in that order
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL=C (^C).")
print("If you do want that, hit RETURN")

# display ? prompt to user and wait for RETURN or ^C
input("?")

print("Opening the file...")
# open the file for writing purposes and assign the file object
# to a variable named target
target = open(filename, 'w')

print("truncating the file.  Goodbye!")
# truncate the file contents i.e. delete them
target.truncate()

print("now I'm going to ask you for three lines.")

# prompt the user for a line and store the result in the specified variable
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# write the lines and new lines to the file in this order
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.write("\nWrite all three lines again in one write:\n")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
target.close()
