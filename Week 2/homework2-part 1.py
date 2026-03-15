def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8


choice = input("Convert from (C/F): ")

if choice == "C":
    temp = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(temp)
    print("Temperature in Fahrenheit:", result)

elif choice == "F":
    temp = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(temp)
    print("Temperature in Celsius:", result)

else:
    print("Invalid choice")