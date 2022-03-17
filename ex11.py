''' 1. Go online and find out what Pythn's input does.
    2. Can you find other ways to use it? Try some of the samples you find.
    3. Write another "form" like this to ask some other questions. 
'''

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")


''' Another Form '''

query = input("Is this book going to go from 0 to 60 real quick?\n")
if query == "yes".lower().strip():
    print("Sounds about right.")
else:
    print("You'll see, you'll all see!")

