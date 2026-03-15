def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


choice = input("Do you want to calculate a factorial? (y/n): ")

if choice == "y":
    n = int(input("Enter a number: "))
    print("Factorial:", factorial(n))
else:
    print("Program ended.")