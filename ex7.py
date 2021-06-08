# print the sentence to the screen
print("Mary had a little lamb.")
# print the sentence to the screen, substituting 'snow' inside the {}
print("Its fleece was white as {}.".format('snow'))
# print the sentence to the screen
print("And everywhere that Mary went.")
# this printed 10 . characters in succession on the same line i.e. ".........."
print("." * 10) # what'd that do?

# creates a variable named end* and assigns the character value to it
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#debugging by printing the variable value :)
#print(end10)

# prints the words "Cheese Burger" but concatenating the value of each
# specified variable, when you print, instead of a new line use a space
# watch that comma at the end. try removing it to see what happens
# Removing the comma causes an error: SyntaxError: invalid syntax
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
