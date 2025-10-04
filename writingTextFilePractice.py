#This is a practice on how to write into a text file in python

filename='sources.txt'
with open(filename, mode = 'w') as out_file:
    out_file.write("It is not so simple anymore!")
print(out_file)


#another practice
filename = 'sources.txt'

with open(filename, mode='w') as out_file:
    out_file.write("It is not so simple anymore!")

with open(filename, mode='r') as out_file:
    new_text = out_file.read()

print(new_text)

