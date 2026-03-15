import random

numbers = []

for i in range(20):
    numbers.append(random.randint(1, 100))

print("List:", numbers)

total = 0

print("Even numbers:")
for n in numbers:
    if n % 2 == 0:
        print(n, end=" ")
        total += n

print("\nTOTAL of even numbers:", total)