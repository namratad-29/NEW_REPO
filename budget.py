budget_amount = int(input("Enter the budget amount: "))
allocated_budget = int(input("Enter the allocated budget: "))
dept_score = float(input("Enter the department performance score: "))
approved=budget_amount <= allocated_budget and dept_score >= 7.0 
print(f"Budget Amount: {budget_amount}")
print(f"Allocated Budget: {allocated_budget}")
print(f"Department Performance Score: {dept_score}")
print("Budget Approved: ", approved)