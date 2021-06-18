from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
# repr gives you the representation, the raw python version of in_file
print("infile= ", repr(in_file))
indata = in_file.read()
#indata = open(from_file).read()

#print(f"The input file {from_file} is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, done")

#out_file.close()
#in_file.close()
