"""
    ---------------- File Manager in Python ----------------

    * Create .txt files
    * List and read .txt files
    * Update .txt files
    * Remove or delete .txt files

    * By Névio Costa Magagnin
    * Python Version: 3.8.0
    * PyCharm Community 2020.02 - x64

    ---------------- Modules to Install ----------------

    * Colorama: pip install colorama
    * Python Auto GUI: pip install pyautogui
"""

# Imports
import os
import random
import sys
import string
import colorama
import glob as gb
import pyautogui

from colorama import Fore, Style

colorama.init() # Starts Colorama

# Function that print a message on the screen
def print_message(message, color):
    print(' ')

    if color == 'green' or color == 'g' or color != 'red':
        print(Fore.GREEN + '---------------- ' + message + ' ----------------' + Style.RESET_ALL)
    else:
        print(Fore.RED + '---------------- ' + message + ' ----------------' + Style.RESET_ALL)

# Function that list the current files
def print_current_files(files):
    print('Current Files')
    for item in files:
        print(f' - {item}')

# Function that create or update a file
def create_and_write_file(name, content):
    file = open(name, 'w')
    file.write(content)
    file.close()

# Function that read a file
def read_file(name):
    print('File ' + Fore.GREEN + name + Style.RESET_ALL + ' content')
    print('')

    file = open(name, 'r')
    for row in file:
        row = row.rstrip()
        print(row)
    file.close()

# Function that clear the screen
def clear_screen():
    pyautogui.hotkey('ctrl', 'l')

action = None # Action variable

# Infinity Loop, if the action variable is not 'close', it will run
while action != 'close':

    # GET = list and read the file
    # ADD = add a new file
    # UPDATE = update the file content
    # REMOVE = remove the indicated file
    # CLEAR = clear the screen
    # CLOSE = stop the program

    print('')
    print(Fore.GREEN + '---------------- FILE MANAGER  ----------------' + Style.RESET_ALL) # Title
    print('')
    action = str(input('What do you want to do? (get, add, update, remove, close) ')) # Input that recives the action value

    if action == 'get' or action == 'g' or action == 'Get' or action == 'G':

        returned_files = gb.glob(r'*.txt')

        if returned_files:
            print_current_files(returned_files)
            print('')
            file_to_read = str(input('Which file should be read? ')) + '.txt'

            if file_to_read in returned_files:
                read_file(file_to_read)
            else:
                print_message('File ' + file_to_read + ' does not exists in the folder', 'red')

            action = None
        else:
            print_message('Files .txt does not exists in the folder', 'red')
            action = None

    elif action == 'add' or action == 'a' or action == 'Add' or action == 'A':

        file_name = str(input('Enter the file name: ')) + '.txt'
        file_content = str(input('Enter the file content: '))
        print('')

        if os.path.exists('./' + file_name):

            create_new_file = str(input('The '+ Fore.GREEN + file_name + Style.RESET_ALL +' file already exists, do you want to create a new one? (Yes / No): '))

            if create_new_file == 'Y' or create_new_file == 'Yes' or create_new_file == 'y' or create_new_file == 'yes':

                letters = string.ascii_lowercase
                string_hash = ''.join(random.choice(letters) for i in range(8))
                file_name = string_hash + '_' + file_name

                create_and_write_file(file_name, file_content)
                print_message('File ' + file_name + ' created successfully!', 'green')
                action = None

            else:
                print_message('CLOSED!', 'red')
                action = None

        else:
            create_and_write_file(file_name, file_content)
            print_message('File ' + file_name + ' created successfully!', 'green')
            action = None

    elif action == 'update' or action == 'u' or action == 'Update' or action == 'U':

        returned_files = gb.glob(r'*.txt')

        if returned_files:
            print_current_files(returned_files)
            print('')
            file_to_update = str(input('Which file should be updated? ')) + '.txt'

            if file_to_update in returned_files:

                print('')
                new_file_content = str(input('Enter the new file content: '))
                create_and_write_file(file_to_update, new_file_content)
                read_file(file_to_update)
                print_message('File ' + file_to_update + ' updated successfully!', 'green')

            else:
                print_message('File ' + file_to_update + ' does not exists in the folder', 'red')

            action = None
        else:
            print_message('Files .txt does not exists in the folder', 'red')
            action = None

    elif action == 'remove' or action == 'r' or action == 'Remove' or action == 'R':

        returned_files = gb.glob(r'*.txt')

        if returned_files:

            print_current_files(returned_files)

            print('')
            file_to_remove = str(input('Which file should be removed: ')) + '.txt'

            if file_to_remove in returned_files:
                os.remove('./' + file_to_remove)
                print_message('File ' + file_to_remove + ' removed successfully!', 'green')
                action = None
            else:
                print_message('File '+ file_to_remove +' does not exists in the folder', 'red')
                action = None

        else:
            print_message('Files .txt does not exists in the folder, add a new one to remove...', 'red')
            action = None

    elif action == 'clear':
        clear_screen()
        action = None

# Finish the Program
print_message('CLOSED!', 'red')
sys.exit()
