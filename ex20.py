# import argv (argument variable/vector) from sys module
from sys import argv

# unpack argv and assign it to the variables on the left, in that order
script, input_file = argv

# define a function called print_all that takes one argument f which is a file
# the function opens a text file for reading and prints the contents to the screen
def print_all(f):
    print(">>> print_all: f=", f)
    print(f.read())
    print(">>> print_all: f=", f)

# define a function called rewind that takes one argument f which is a file
# the function moves the read/write pointer to the 0 byte (first byte) position in the file
# i.e. the start of the file
def rewind(f):
    print(">>> rewind: f=", f)
    f.seek(0)
    print(">>> rewind: f=", f)

# define a function called print_a_line which takes two arguments and assigns them to the variables
# line_count and f, in the order specified by the function call
# e.g. if the function is called using "print_a_line(current_line, current_file)" then the value of
# current_line in the function call is assigned to line_count in the function, And the value of
# current_file in the function call is assigned to f in the function
# the function prints two values, the first is the value of line_count and the second is
# the text on the next line in the file
# f.readline() reads a line from the file and moves the read head to right after the \n that ends that line
def print_a_line(line_count, f):
    print(f">>> print_a_line: line_count={line_count}, f={f}")
    print(line_count, f.readline())
    print(f">>> print_a_line: line_count={line_count}, f={f}")

# create a variable named current_file which is a file object for an open text file
current_file = open(input_file)
print(f"{current_file}") # returns "<_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>"
print("Print the first three lines")
# print the first, second and third lines in the file, use '' at the end of each line instead of
# returning the \n at the end of the line
print(current_file.readline(), end='')
print(current_file.readline(), end='')
print(current_file.readline(), end='')

print("Return to the beginning of the file\n")
# call the function rewind, and pass the argument current_file to it
# the function will execute and move the read/write pointer to 0 byte position in the file
rewind(current_file)

print("Next let's print the whole file:\n")

# call the function print_all, and pass the argument current_file to it
# the function will print out the contents of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print 3 lines:")

# create a variable named current_line with value 1
current_line = 1
print(">>> current_line =", current_line)
# call the function print_a_line with two arguments, current_line and current_file
# this passes the value of 1 for current_file and the pointer to the file object of current_file
print_a_line(current_line, current_file)

# increment the value of current_line by 1, so it is now 2
# Note: x = x + y is the same as x += y
current_line += 1
print(">>> current_line =", current_line)
# call the function print_a_line with two arguments, current_line and current_file
# this passes the value of 2 for current_file and the pointer to the file object of current_file
print_a_line(current_line, current_file)

# increment the value of current_line by 1, so it is now 3
current_line += 1
print(">>> current_line =", current_line)
# call the function print_a_line with two arguments, current_line and current_file
# this passes the value of 2 for current_file and the pointer to the file object of current_file
print_a_line(current_line, current_file)
