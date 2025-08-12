# Loan Details
# This file contains the details of a loan, including the amount, interest rate, and duration
# It is used to calculate the monthly payment and total payment over the life of the loan

money_owed = float(input("Enter the amount of the loan: "))
apr = float(input("Enter the interest rate (as a percentage): "))
payment= float(input("Enter the monthly payment amount: "))
months = int(input("Enter the number of months for the loan: "))

montly_rate = apr / 100 / 12
total_payment = payment * months
total_interest = total_payment - money_owed     
print(f"Total payment over {months} months: ${total_payment:.2f}")
print(f"Total interest paid: ${total_interest:.2f}")