#goal: Allow a user to enter a value that represents the number of working years remaining in the user’s career and another value for the annual amount of money the user can save. Assume that the user earns 3 percent simple interest on savings annually. Program output is a schedule that lists each year number in retirement starting with year 0 and the user’s savings at the start of that year. Assume that the user spends $60,000 per year in retirement and then earns 3 percent interest on the remaining balance. End the list after 30 years or when the user’s balance is 0 or less, whichever comes first.


work_yrs_remaining = int(input("Enter the number of years you have left until retirement: "))
annual_savings = float(input("Enter your annual savings: "))
balance = 0

# Accumulation (Working Years)
print("\nWorking Years Projection:")

# Using formatted strings with padding
print(f"{'Year':<5} | {'Added Savings':<15} | {'Interest Earned':<15} | {'Total Balance':<15}")
print("-" * 57)

for year in range(1, work_yrs_remaining + 1):
    balance += annual_savings
    interest_earned = balance * 0.03  # Calculate the 3% interest
    balance += interest_earned
    
    print(f"{year:<5} | ${annual_savings:<14.2f} | ${interest_earned:<14.2f} | ${balance:<14.2f}")

#Distribution (Retirement Years)
print("\nRetirement Schedule:")
print(f"{'Year':<5} | {'Starting Balance':<17} | {'Withdrawal':<12} | {'Interest Earned':<15} | {'Ending Balance':<15}")
print("-" * 73)

for year in range(1, 31):
    # Stop the loop if the money runs out
    if balance <= 0:
        print(f"\nYear {year}: Balance is $0.00 or less. Retirement funds depleted.")
        break
        
    starting_balance = balance
    withdrawal = 60000
    
    # Subtract the annual spending first
    balance -= withdrawal
    
    # Calculate interest only if there is still money left after the withdrawal
    if balance > 0:
        interest_earned = balance * 0.03
        balance += interest_earned
    else:
        interest_earned = 0
        
    print(f"{year:<5} | ${starting_balance:<16.2f} | ${withdrawal:<11.2f} | ${interest_earned:<14.2f} | ${balance:<14.2f}")

