hours_worked = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))
standard_hours = 8
if hours_worked > standard_hours:
    overtime_hours = hours_worked - standard_hours
    overtime_pay = overtime_hours * hourly_rate * 1.5
else:
    overtime_hours = 0
    overtime_pay = 0
print(f"Hours Worked: {hours_worked}")
print(f"Hourly Rate: {hourly_rate}")    
print(f"Overtime Hours: {overtime_hours}")
print(f"Overtime Pay: {overtime_pay}")