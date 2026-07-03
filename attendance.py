day_present=int(input("Enter the number of days present: "))
total_days=int(input("Enter the total number of days: "))
attendance_percentage=(day_present/total_days)*100
print("Attendance Percentage: ", attendance_percentage)
attendance_percentage=day_present/total_days*100
bonus_eligible=attendance_percentage>=95
print(f"Attendance Percentage: {attendance_percentage}%")
if bonus_eligible:
    print("Eligible for bonus.")
else:
    print("Not eligible for bonus.")