price=float(input("Enter the price of the item: "))
tax_rate=float(input("Enter the sales tax rate (as a percentage): "))
tax_amount=price*(tax_rate/100)
total_price=price+tax_amount
print(f"Sales Tax Amount: ${tax_amount:.2f}")
print(f"Total Price: ${total_price:.2f}")
