#Alex Hanna
#Assignment 4.1
#04/07/2021

company = input("Hello, please enter your company's name:") #welcome and prompts the user to enter their company's name. Value entered is assigned to variable "company"


fiber = int(input("Next, enter the number of feet of fiber optic needed:")) # prompts user to enter number of feet and converts entry into an integer. Value is assigned to variable "fiber"

if fiber <= 100:
    cost = fiber * 0.87 
elif fiber <= 250:
    cost = fiber * 0.80
elif fiber <= 500:
    cost = fiber * 0.70
elif fiber > 500:
    cost = fiber * 0.50

    #if-elif condition that gives a different price/feet depending on feet of fiber optic entered

print("The total cost for ",company, "is $",cost)# prints message that displays the company name and total cost.