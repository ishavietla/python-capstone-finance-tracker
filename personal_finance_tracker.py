
def print_welcome():
    print("Welcome to the Personal Finance Tracker!")

def add_expense(data):
#ask user to enter an expense and add it to the data dictionary
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_input = input("Enter amount: ").strip()
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        expense = (description, amount)

        if category in data:
            data[category].append(expense)
        else:
            data[category] = [expense]

        print("Expense added successfully.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_expenses(data):
   #print expenses
    if not data:
        print("No expenses recorded.")
        return

    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for desc, amount in expenses:
            print(f"  - {desc}: ${amount:.2f}")

def view_summary(data):
   #print total amount spent
    if not data:
        print("No expenses recorded.")
        return

    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

def main_menu():
    #display main menu and read user input
    expenses_data = {}

    print_welcome()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_expense(expenses_data)
        elif choice == '2':
            view_expenses(expenses_data)
        elif choice == '3':
            view_summary(expenses_data)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

#run program
if __name__ == "__main__":
    main_menu()
