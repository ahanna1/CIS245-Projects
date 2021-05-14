#Alex Hanna
#Assignment 6
#04/24/21


miles = input("How many miles did you drive?:")
try:
    miles = float(miles)
except:
    print ("You did not enter a number")

#try-except block that will display error message and quit program if
# a number/float is not entered
   

def convert_function(miles): #define function name and passes miles into function
    
    kilometers = miles/0.62137 # converts miles to kilometers
    
    print("You drove", miles, "miles, which equals", kilometers, "kilometers")

convert_function(miles) #function is called with miles passed so it can be displayed in print message
