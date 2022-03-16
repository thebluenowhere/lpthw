""" 1. Go through the program and write a comment above each line
    2. Find all the places where a string is put inside a string. 4 places.
    3. Are you sure there are only four places? Maybe Zed is lying.
    4. Explain why adding the two strings w and e with + makes a longer string.
        A: the '+' operator when used with two strings concatenates the strings.
"""

# assigns a variable
types_of_people = 10
# sets an f-string to the variable 'x'
x = f"There are {types_of_people} types of people."

# assigns variables
binary = "binary"
do_not = "don't"
# sets an f-string to the variable 'y'
y = f"Those who know {binary} and those who {do_not}."

# normal printing
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# sets boolean value to variable 
hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# concatenates two strings.
print(w + e)

