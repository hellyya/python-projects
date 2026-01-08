categories = ["food", "bills", "fun"]
expenses = {}

for category in categories:
    try:
        amount= float(input(f"Enter the amount spent on {category}: "))
        expenses[category] = amount
    except ValueError:
        print(f"Invalid input for {category}.")
        expenses[category] = 0.0

print("\nDaily expenses")
for category, amount in expenses.items():
    print(f"{category:15}: ${amount:.2f}")

total= sum(expenses.values())
print("-"*30)
print(f"Total money spent : ${total:.2f}")

if expenses: 
    highest_cat = max(expenses, key=expenses.get)
    print(f"Highest Spending: {highest_cat} (${expenses[highest_cat]:.2f})")