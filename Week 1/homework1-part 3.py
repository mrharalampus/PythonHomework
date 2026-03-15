a = int(input("Give a: "))
b = int(input("Give b: "))

if a > b:
    print("Must be less than b")
else:
    for i in range(a, b + 1):
        print(i, end=" ")