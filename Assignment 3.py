#Alex Hanna
#Assignment 3.1
#04/03/2021

company = input("Hello, please enter your company's name:") #welcome and prompts the user to enter their company's name. Value entered is assigned to variable "company"


fiber = int(input("Next, enter the number of feet of fiber optic needed:")) # prompts user to enter number of feet and converts entry into an integer. Value is assigned to variable "fiber"

cost = fiber * 0.87 # calculation that takes value entered into fiber and multiplies it by .87. Value is later assigned to cost

print("The total cost for ",company, "is $",cost)# prints message that displays the company name and total cost.