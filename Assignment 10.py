#Alex Hanna
#05/22/2021
#CIS 245, Assignment 10
# Program asks user for directory to save file, confirms if it exists then asks for input
# Program also displays info from input to console before writing to new file


import os, json  # import os and json modules


def check_directory():
    #function asks user for directory to save file and checks to see if it exists

    directory = input("Enter the directory:")
    if os.path.isdir(directory):
            print("This directory exists, please continue")
    else:
        print("That directory does not exist, try again")
        check_directory()
        # if directory does not exist, program will asks user to try again


            
def get_input():

    filename = input ("Enter the file name:")

    name= input("Enter your name:").split()
    address= input("Enter your address:").split()
    phone= input ("Enter your phone number:").split()
    #three prompts that split each variable into a list
    user_input = name+address+phone
    #combines all three variables into one variable
    
    
    with open(filename,'w') as f:
        json.dump(user_input,f)
        # writes inputted values into new files
    
    with open (filename,'r') as f:
        print(f"Here is what your new file will contain: {user_input}")

        #displays data user entered


#Both functions are called
check_directory()
get_input()



    



