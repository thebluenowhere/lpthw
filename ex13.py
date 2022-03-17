''' 1. Try giving fewer than three arguments to your script. 
        A: Not enough arguments provided. 
    2. Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.
    3. COmbine input with argv to make a script that gets more input from a user. 
    4. Remember that modules give you features. Modules. Modules. 
'''

from sys import argv

'''
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
'''

script, a, b, c = argv
d = input("Enter a food beginning with 'D' please: ") 
print(f"a is: {a} b is: {b} c is: {c}",end=', ')
print(f"d is: {d}")

