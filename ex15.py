# import the argument variable module
from sys import argv

# unpack argv so filename can be entered on terminal
script, filename = argv

#use the open function on our filename
txt = open(filename)

print(f"Here's your file {filename}:")
# use the read function on our file
print(txt.read())

print("Type the filename again:")
# repeat or enter a different file
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()