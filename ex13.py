"""
from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
"""


from sys import argv

breads, roll, bun = argv

print("The script is called", breads)
print("The first value is", roll)
print("The second value is", bun)
ask = input("What is your favorite bread? ")
print(f"The users favorite bread is {ask}.")
