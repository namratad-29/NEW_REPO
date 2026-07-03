current_stock = int(input("Enter the current stock: "))
minimum_threshold = int(input("Enter the minimum threshold: "))
maximum_capacity = int(input("Enter the maximum capacity: "))
if int(current_stock) < int(minimum_threshold):
    print("Stock is below minimum threshold.")  
elif int(current_stock) > int(maximum_capacity):
    print("Stock exceeds maximum capacity.")
else:
    print("Stock is within acceptable range.")
