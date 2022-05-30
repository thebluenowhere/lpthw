from sys import argv
script, user_name, age = argv
prompt = '... '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of operating system do you use?")
computer = input(prompt)

print(f"""
Alright, you are {age} years old, you said {likes} about liking me. 
You live in {lives}. Not sure where that is. 
And you have {computer} as an operating system. Nice.
""")

