#Alex Hanna
#Assignment 5
#04/16/2021



initial_amount = float(input("Enter the initial investment amount: "))
interest = float(input("Enter the annualized interest rate: "))
# two prompts that converts input into a float
new_amount = initial_amount #value entered as initial amount will be set equal to new_amount
years =0 # year variable initialized


while new_amount <= initial_amount * 2:
    new_amount += new_amount * (interest/100) # while statement that will run calculation until new_amount is double initial_amount
    years += 1 #every time loop runs, years will increase by 1


print("It will take", years,"years to double your initial investment of $",initial_amount)
