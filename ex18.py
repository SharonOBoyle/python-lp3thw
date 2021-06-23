# this one is like your scripts with argv
# def(ine) a function named print_two
# with *args (similar to argv parameter but for functions)
# :
# indent
# After : all the indented lines will become attached to print_two
# Functions means you can make your own commands and use them if __name__ == '__main__':
# your python scripts
def print_two(*args):
    # unpack the args and assign to the variables on the left
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok,that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
