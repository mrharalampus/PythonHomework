import random

list1 = []
list2 = []

for i in range(20):
    list1.append(random.randint(1, 100))
    list2.append(random.randint(1, 100))

print("List 1:", list1)
print("List 2:", list2)

print("Common elements:")

for n in list2:
    if n in list1:
        print(n, end=" ")