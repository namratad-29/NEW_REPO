revenue=float(input("Enter the revenue: "))
expenses=float(input("Enter the expenses: "))
profit=revenue-expenses
if revenue>expenses:
    print("Profit: ", profit)
elif expenses>revenue:
    print("Loss: ", expenses-revenue)
else:
    print("No profit, no loss.")