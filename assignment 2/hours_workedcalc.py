hours_worked = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))

regular_hours_threshold = 40

if hours_worked <= regular_hours_threshold:
    regular_pay = hours_worked * hourly_rate
    overtime_pay = 0  
else:
    regular_pay = regular_hours_threshold * hourly_rate
    overtime_hours = hours_worked - regular_hours_threshold
    overtime_pay = overtime_hours * (1.5 * hourly_rate)


total_pay = regular_pay + overtime_pay

print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Total Pay: ${total_pay:.2f}")
