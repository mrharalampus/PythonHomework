with open("expenses.txt", "a") as file:
    while True:
        category = input("Category: ")
        amount = input("Amount: ")
        file.write(f"{category},{amount}\n")
        
        if input("Add more? (y/n): ").lower() == "n":
            break

totals = {}
with open("expenses.txt", "r") as file:
    for line in file:
        cat, amt = line.strip().split(",")
        totals[cat] = totals.get(cat, 0) + float(amt)

print("\nTotal expenses per category (highest first):")
for cat, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
    print(f"{cat}: {total}")