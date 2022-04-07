import os
import requests
import string

# Clean the screen
clear_term = 'cls||clear'
os.system(clear_term)

def check_input(input_string, requirement, limit):
    if requirement == 'number':
        if input_string.isnumeric():
            if int(input_string) in range(1,limit + 1):
                passed = True
            else:
                print('      The number you have entered is unrealistic. Please try again')
                passed = False
        else:
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
    registrations = {slot: None for slot in range(1, num_slots + 1)}
    available_slots = num_slots
    outer_passed = False
    while not outer_passed:
        available_slots = num_slots - len([_ for _ in registrations.values() if _ != None])
        os.system(clear_term)
        print(statements[1])
        print(f"      Available Slots: {available_slots}\n      Filled Slots: {num_slots - available_slots}\n")
        print(statements[2])

        passed = False
        while not passed:
            print(registrations)
            menu_option = input("      Please choose a task: >> ")
            passed = check_input(menu_option,'number',5)
        menu_option = int(menu_option)
        if menu_option == 1:
            registrations = sign_up_menu(registrations)
        elif menu_option == 2:
            registrations = deregister_menu(registrations)
        elif menu_option == 3:
            view_participants()
        elif menu_option == 4:
            save_menu()
        elif menu_option == 5:
            outer_passed = exit_menu(False)
    
def sign_up_menu(registrations):
    os.system(clear_term)
    print(statements[3])
    name_picked = False
    passed = False
    while not passed:
        if not name_picked:
            name = input("      Participant Name: >> ")
            passed = check_input(name,'string',None)
            name_picked = True
            
        if name_picked:    
            desired_slot = input(f"      Desired Starting Slot [1-{len(registrations)}]: >> ")
            passed = check_input(desired_slot,'number',len(registrations))
        if passed:
            desired_slot = int(desired_slot)
            if registrations[desired_slot] != None:
                print(f'      Slot #{desired_slot} is filled. Please try again')
                passed = False
            else:
                registrations[desired_slot] = name.title()
    print(f'      {name.title()} is signed up in starting slot #{desired_slot}')
    return registrations                 
    
def deregister_menu(registrations):
    os.system(clear_term)
    print(statements[4])
    passed = False
    while not passed:
        current_slot = input(f"      Current Slot [1-{len(registrations)}]: >> ")
        name = input("      Participant Name: >> ")
        passed = check_input(current_slot,'number',len(registrations))
        if passed:
            current_slot = int(current_slot)
            if registrations[current_slot] == name.title():
                registrations.update({current_slot: None})
                print('\n      Success:')
                print(f'      {name.title()} has been cancelled from slot {current_slot}.')
                go_again = '\n      Would you like to cancel another participant? (y/n) >> '
                passed = False if input(go_again).lower() == 'y' else True
            else:
                print('\n      Error:')
                print(f'      {name.title()} is not in that starting slot.\n')
                passed = False
                
    return registrations
                
def view_participants():
    os.system(clear_term)
    print(statements[5])
    
def save_menu():
    os.system(clear_term)
    print(statements[6])
    
def exit_menu(unsaved_changes):
    os.system(clear_term)
    print(statements[7])
    if unsaved_changes:
        print("      Any unsaved changes will be lost.")
    confirm = input("      Are you sure you want to exit? [y/n] >> ")
    if confirm.lower() == 'y':
        print(statements[8])
        #raise SystemExit
        return True
    
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
    num_slots = int(num_slots)

main_menu(num_slots)