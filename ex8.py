# create a string variable called formatter and assign it the string value {} {} {} {}
formatter = "{} {} {} {}"

# take the formatter string, call it's format function,
# pass the 4 arguments inside the format() to the format function
# result is a new string that has the {} in formatter replaced with the four arguments
# print the result
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
  "Try your",
  "Own text here",
  "Maybe a poem",
  "Or a song about fear"
))
