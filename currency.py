inr_amount = float(input("Enter the amount in INR: "))
conversion_rate = float(input("Enter the conversion rate to USD: "))
usd_amount = inr_amount / conversion_rate
processing_fee = usd_amount * 0.02
total_usd_amount = usd_amount - processing_fee
print(f"Amount in USD: {usd_amount}")
print(f"Processing Fee: {processing_fee}")
print(f"Total Amount in USD: {total_usd_amount}")   