"I am 6'2\" tall." # escape double-quote inside string
'I am 6\'2" tall.' # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t\v* Cat food
\t* Fishies
\t* Catip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

bell_cat = "I'm noisy\a"
backspace_cat = "I go back\b and then forwards"
ff_cat = "Formfeed\f does this\f and this\f and this\f"
uni_cat = "Unicode ??: \N{YIN YANG}"
cr_cat = "\n\n\n\n\nCarriage return does this\r and this\r and again does this\cr"
vert_cat ="Horizontal vertical tab does this\v and this\v and this\v"
uni_cat ="Unicode for fire is: \U0001F525"
music_cat = "Notes \U0001F3B5 and more \U0001F3B6"
complicate_s = '''
Let's slash \\ the line \n and vertical tab to some fire\v
\U0001F525 and again to face the music\v\U0001F3B6
'''
complicate_d = "Let's slash \\ the line \n and vertical tab to some fire\v\U0001F525 and again to face the music\v\U0001F3B6"

#print(bell_cat)
#print(backspace_cat)
#print(ff_cat)
#print(uni_cat)
#print(cr_cat)
#print(vert_cat)
#print(uni_cat)
#print(music_cat)
print(complicate_s)
print(complicate_d)
