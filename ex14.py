# import the argv module, argument variable/vector, that holds the
# arguments you pass to the python script when you run it
from sys import argv

# unpack the argv and assign it to these variables on the left in order
script, user_name, age = argv
# create a variable, prompt, with value as shown
prompt = 'Prompt >>> '

print(f"Hi {user_name}, aged {age}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
# create a variable named likes, display a prompt string to the user
# and assign the value typed by the user to the variable
likes = input(f"{prompt} {user_name} >")

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
