#Calculate amounts needed to be deposit in the present
#to get a desired future value 

#Suppose you want to deposit an amount of money into a savings
#account and leav it to dra interest for the next 10 years.
#In ten years you would have 10,000 dolars.
#We use the formula: P=F/(1+r)**n 


#Get the desired future value

future_value = float(input("Enter the desired future value: "))

#Get the annual interest rate

rate = float(input("Enter the anual interes rate: "))

#Get the number of years that the money will sit in the account

years = int(input("Enter the number of years the money will grow:" ))

#Calculate the amount that will have to be deposited

present_value = future_value / (1.0 + rate ) ** years

#Display the result of the calculation

print("You will need to deposit: ", present_value)