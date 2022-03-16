""" 1. Change all the variables so there's no my_ in front of each one. Make sure to change the name everywhere, not just where you used = to set them. 
    2. Try and write some variables that convert the inches and pounds to centimetres and kilograms. Work out the math in python. 
"""

name = "Michael J. Scott"
age = 32 # not a lie
height = 74 # inches
height_cm = height * 2.54
weight = 294 # lbs
weight_kg = weight * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_cm} inches tall.")
print(f"He's {weight_kg:.2f} pounds heavy.")
print("That's really too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right. 
total = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm:.2f}, and {weight_kg:.2f} I get {total:.2f}.")

