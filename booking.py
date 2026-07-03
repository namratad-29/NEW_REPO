existing_start=float(input("Enter the existing start time (in hours): "))
existing_end=float(input("Enter the existing end time (in hours): "))
new_start=float(input("Enter the new start time (in hours): "))
new_end=float(input("Enter the new end time (in hours): "))
if not (existing_end <= new_start or new_end <= existing_start):
    print("Scheduling conflict detected.")
else:
    print("No scheduling conflict.")