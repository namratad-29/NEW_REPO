years_of_experience = int(input("Enter the years of experience: "))
performance_rating = float(input("Enter the performance rating (1-10): "))
eligible_for_bonus = years_of_experience > 2 and performance_rating >= 8.0
print(f"Years of Experience: {years_of_experience}")
print(f"Performance Rating: {performance_rating}")
if eligible_for_bonus:
    print("Eligible for bonus.")
else:
    print("Not eligible for bonus.")