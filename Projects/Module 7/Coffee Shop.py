# Base price and total
base_price = 2.00
total_price = base_price
    
# Parallel Arrays
add_ins = ["whipped cream", "cinnamon", "chocolate sauce", "amaretto", "irish whiskey"]
prices = [0.89, 0.25, 0.59, 1.50, 1.75]

sentinel = "done"

print(f"Welcome! Base coffee is ${base_price:.2f}")
print("Available: Whipped cream, Cinnamon, Chocolate sauce, Amaretto, Irish whiskey")

while True:
    choice = input(f"Enter add-in (or type '{sentinel}'): ").strip().lower()

    if choice == sentinel:  
        break
    
    # Search the names array for the user's input
    found_index = -1
    for i in range(len(add_ins)):
        if add_ins[i] == choice:
            found_index = i
            break
    
    # Check if the item was found
    if found_index != -1:
        item_price = prices[found_index]
        total_price += item_price
        print(f"Added {add_ins[found_index]}. Price: ${item_price:.2f}")
    else:
        print("Sorry, we do not carry that.")

print("-" * 20)
print(f"Total Order Price: ${total_price:.2f}")