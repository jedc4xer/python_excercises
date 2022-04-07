import os
import requests
import string

# Clean the screen
clear_term = 'cls||clear'
os.system(clear_term)

def check_input(input_string, requirement, limit):
    if requirement == 'number':
        try:
            input_string = int(input_string)
            if input_string in range(1,limit + 1):
                passed = True
            else:
                print('      The number you have entered is unrealistic. Please try again')
                passed = False
        except:
            print('      You must enter a valid number. Please try again')
            passed = False
    else:
        cleaned_length = len("".join(_ for _ in input_string if _ in string.ascii_letters + " "))
        if cleaned_length == len(input_string):
            passed = True
        else:
            print('      You must enter a valid name. Please try again')
            passed = False
    return passed
        
def get_statements():
    path = 'https://raw.githubusercontent.com/jedc4xer/python_exercises/main/tournament_statements.txt'
    statements = requests.get(path).text.split(",")
    return statements

def main_menu(num_slots):
    os.system(clear_term)
    print(statements[1])
    print(statements[2])
    print(f"      There are {num_slots} participant slots ready for signups.\n")
    
    passed = False
    while not passed:
        menu_option = input("Please choose a task: >> ")
        passed = check_input(menu_option,'number',5)
    if menu_option == 1:
        sign_up_menu()
    elif menu_option == 2:
        deregister_menu()
    elif menu_option == 3:
        view_participants()
    elif menu_option == 4:
        save_menu()
    elif menu_option == 5:
        exit_menu()
    
def sign_up_menu():
    os.system(clear_term)
    print(statements[3])
    
def deregister_menu():
    os.system(clear_term)
    print(statements[4])
    
def view_participants():
    os.system(clear_term)
    print(statements[5])
    
def save_menu():
    os.system(clear_term)
    print(statements[6])
    
def exit_menu():
    os.system(clear_term)
    print(statements[7])
    
statements = get_statements()
print(statements[0])

# Control Access
input("      User Name: >> ")
input("       Password: >> ")
os.system(clear_term)

# Collect # of Participants
passed = False
while not passed:
    num_slots = input("\n      Enter the number of participants: >> ")
    passed = check_input(num_slots,'number',100000000)

main_menu(num_slots)