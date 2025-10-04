#This is a practice on how to write into a text file in python

filename='sources.txt'
with open(filename, mode = 'w') as out_file:
    out_file.write("It is not so simple anymore!")
print(out_file)

