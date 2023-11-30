Price = 1000000     #Price of house is $1M

Good_Credit = False      #Value for applicant with good credit
Bad_Credit = True      #Value for applicant with bad credit

if Good_Credit:
    down_payment = 0.1 * Price      #If statement for down payment with good credit applied
    print("You've been approved for a lower down payment!")
    print(f"The down payment will be ${down_payment}")
elif Bad_Credit:
    down_payment = 0.2 * Price      #Else statement for applicant with poor credit
    print("Your Credit is a little low")
    print(f"Your down payment will be ${down_payment}")

print("thank you for your application!")        #General thank you statement

