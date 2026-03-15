total = 0

while True:
    price = float(input("Item price: "))
    total += price
    
    more = input("Have more items? (y/n): ")
    
    if more == "n":
        break

print("TOTAL:", total)