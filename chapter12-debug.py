# Approaches to debug:
# 1. debug flag
# 2. 
choices = {1: "Start", 2: "Edit", 3: "Quit"}
for key, value in choices.items():
    print("Press ", key, " to ", value)

user_input = input("Enter choice: ")

if int(user_input) in choices.keys():
    print("You chose", choices[int(user_input)])
else:
    print("Unknown choice")
