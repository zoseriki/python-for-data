#You are provided with a text file named 'source.txt'. Store the file's name in a variable called filename. Open the file,
# read its entire content into a variable, and then close it. Before and after closing the file,
# check if it is closed and display the status.
#After confirming that the file is closed, display its content using the stored variable.
#Hint: Use the print() function to display the full content of the text file.

filename = "sources.txt"
file = open(filename, mode = 'r')

text = file.read()
print(file.closed)

file.close()

print(file.closed)
print(text)

#using with open to open and read a text file
filename = 'sources.txt'
file = open(filename, mode='r')
text = file.read()

with open(filename, mode='r') as out_file:
    out_file.read()

print(text)
print(out_file)