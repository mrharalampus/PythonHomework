class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = None
        self.phone = None

    # Method to set birthdate
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    # Method to set phone number
    def set_phone(self, phone):
        self.phone = phone

    # Method to display person info
    def display(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Birthdate: {self.birthdate}")
        print(f"Phone: {self.phone}")


# Define Employee class inheriting from Person
class Employee(Person):
    def __init__(self, first_name, last_name, company, salary):
        super().__init__(first_name, last_name)  # Inherit first and last name
        self.company = company
        self.salary = salary

    # Method to display employee info
    def display(self):
        super().display()  # Show Person info
        print(f"Company: {self.company}")
        print(f"Salary: {self.salary}")


# --- Test the classes ---

# Create a Person
person1 = Person("George", "Ford")
person1.set_birthdate("1973-05-19")
person1.set_phone("555-1234")

print("PERSON INFO:")
person1.display()

print("\n-------------------\n")

# Create an Employee
employee1 = Employee("Bill", "Jackson", "SeaTechCorp", 55000)
employee1.set_birthdate("1985-08-20")
employee1.set_phone("555-5678")

print("EMPLOYEE INFO:")
employee1.display()