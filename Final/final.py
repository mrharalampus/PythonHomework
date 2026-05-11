import csv
import os

FILE_NAME = "orders.csv"


# Create CSV file if it does not exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID",
                "Customer Name",
                "Address",
                "Description",
                "Date",
                "Total Amount",
                "Delivered"
            ])


# Generate next auto-increment ID
def get_next_id():
    with open(FILE_NAME, mode='r') as file:
        reader = list(csv.reader(file))

        if len(reader) <= 1:
            return 1

        last_row = reader[-1]
        return int(last_row[0]) + 1


# Add a new order
def add_order():
    customer_name = input("Customer name: ")
    address = input("Address: ")
    description = input("Description: ")
    date = input("Date (YYYY/MM/DD): ")
    total_amount = input("Total amount: ")

    order_id = get_next_id()

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            order_id,
            customer_name,
            address,
            description,
            date,
            total_amount,
            "No"
        ])

    print(f"Order added successfully with ID {order_id}")


# Mark order as delivered
def mark_delivered():
    order_id = input("Enter order ID: ")

    rows = []

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == order_id:
                row[6] = "Yes"

            rows.append(row)

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Order updated successfully.")


# Count orders by customer
def orders_by_customer():
    customer_name = input("Enter customer name: ")

    count = 0

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[1].lower() == customer_name.lower():
                count += 1

    print(f"{customer_name} has placed {count} order(s).")


# Show pending orders
def pending_orders():
    print("\nPending Orders:\n")

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[6] == "No":
                print(row)


# Main menu
def main():
    initialize_file()

    while True:
        print("\nCoffee Shop Order System")
        print("1. Add order")
        print("2. Order delivered")
        print("3. Customer statistics")
        print("4. Pending orders")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_order()

        elif choice == "2":
            mark_delivered()

        elif choice == "3":
            orders_by_customer()

        elif choice == "4":
            pending_orders()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


main()