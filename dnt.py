product_price = float(input("Enter the product price: "))
discount_percent = float(input("Enter the discount percent: "))
tax_percent = float(input("Enter the tax percent: "))
discount_amount=(product_price * discount_percent / 100) 
tax_amount=product_price * tax_percent / 100
final_price=product_price - discount_amount + tax_amount
print(f"Product Price: {product_price}")
print(f"Discount Percent: {discount_percent}%")
print(f"Tax Percent: {tax_percent}%")
print(f"Final Price: {final_price}")