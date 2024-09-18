#Calculate the interest of loan
interest_rate = float(input("What is the interest rate?"))
loan_amount = float(input("What is the loan amount?"))

interest = (loan_amount * interest_rate)/100
print(f"Your total interest is {interest:.2f}")