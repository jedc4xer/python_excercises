import os
import requests

# Clean the screen
clear_term = 'cls||clear'
os.system(clear_term)

def get_statements():
    path = 'https://raw.githubusercontent.com/jedc4xer/python_exercises/main/tournament_statements.txt'
    statements = requests.get(path).text.split(",")
    return statements

statements = get_statements()
print(statements[0])

# Control Access
input("User Name: >> ")
input(" Password: >> ")

# Collect # of Participants
passed = False
while not passed:
    num_slots = input("Enter the number of participants: >> ")
    try:
        num_slots = int(num_slots)
        passed = True
    except:
        print('You must enter a valid number. Please try again')

print(f"There are {num_slots} participant slots ready for signups.")