import datetime

FILE_NAME = "expenses.txt"

def add_expense():
    amount = int(input("Enter amount: "))
    category = input("Enter category: ").strip().lower()
    date = datetime.date.today()

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{amount},{category}\n")

    print("Expense added successfully!\n")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses found.\n")
            return

        print("\n--- All Expenses ---")
        for expense in expenses:
            date, amount, category = expense.strip().split(",")
            print(f"Date: {date} | Amount: ₹{amount} | Category: {category}")
        print()

    except FileNotFoundError:
        print("No expense file found.\n")


def total_expense():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                _, amount, _ = line.strip().split(",")
                total += float(amount)

        print(f"\nTotal Expense: ₹{total}\n")

    except FileNotFoundError:
        print("No expense file found.\n")


def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expense")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
