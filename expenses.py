expenses = [10.4,5,7,10,30,20,15,5,10,25]

sum =0

for expense in expenses:
    sum = sum + expense

print("Total expenses $", sum, sep=" ")

for i in range(len(expenses)):
    print("Expense", i+1, ":", expenses[i])