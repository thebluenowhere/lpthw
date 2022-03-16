""" Zed Shaws error was due to a variable mistype on his lines 7/14 (variable named differently)
    1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
        A: Only difference is people transported is int as oppose to float in current python.
    2. Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point. 
    3. Write comments above each of the variable assignments
    4. Make sure you know what = is called and that it's purpose is to give data (numbers, strings, e       tc.) names (cars_driven, passengers)
        A: = is called 'equals'
    5. Remember that _ is an underscore character. 
    6. Try running python3.6 from the Terminal as a calculator and use variable names
"""

# setting variable for how many cars in total
cars = 100
# setting variable for how much space is in a car (in terms of people)
space_in_a_car = 4
# setting variable for how many drivers
drivers = 30
# setting variable for how many passengers
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven 


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

