from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here are the contents of {filename}: ")
print(txt.read())

txt.close()
