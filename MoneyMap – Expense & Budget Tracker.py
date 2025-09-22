# MoneyMap – Expense & Budget Tracker
# Track, manage, and analyze your expenses and reminders

from collections import deque

# Node for linked list
class Node:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category
        self.next = None

# Linked list to store individual expenses
class LinkedList:
    def __init__(self):
        self.head = None

    def add_expense(self, amount, category):
        new_node = Node(amount, category)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        if not self.head:
            print("No expenses recorded yet.")
            return
        temp = self.head
        total = 0
        print("\n--- All Expenses ---")
        while temp:
            print(f"Amount: {temp.amount}, Category: {temp.category}")
            total += temp.amount
            temp = temp.next
        print(f"Total Expenses: {total}")

    def to_list(self):
        expenses = []
        temp = self.head
        while temp:
            expenses.append((temp.amount, temp.category))
            temp = temp.next
        return expenses

    def search_by_category(self, category):
        found = False
        temp = self.head
        while temp:
            if temp.category.lower() == category.lower():
                print(f"Amount: {temp.amount}, Category: {temp.category}")
                found = True
            temp = temp.next
        if not found:
            print(f"No expenses found for category: {category}")

    def delete_expense(self, amount, category):
        temp = self.head
        prev = None
        while temp:
            if temp.amount == amount and temp.category.lower() == category.lower():
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f"Deleted expense: Amount {amount}, Category {category}")
                return True
            prev = temp
            temp = temp.next
        print(f"Expense not found: Amount {amount}, Category {category}")
        return False

# Hash table to store category-wise totals
class HashTable:
    def __init__(self):
        self.table = {}

    def add_expense(self, category, amount):
        if category in self.table:
            self.table[category] += amount
        else:
            self.table[category] = amount

    def reduce_expense(self, category, amount):
        if category in self.table:
            self.table[category] -= amount
            if self.table[category] <= 0:
                del self.table[category]

    def display(self):
        if not self.table:
            print("No category data available.")
            return
        print("\n--- Category Totals ---")
        for cat, total in self.table.items():
            print(f"{cat}: {total}")

# Queue for reminders
reminders = deque()

def add_reminder(bill):
    reminders.append(bill)
    print(f"Reminder added: {bill}")

def show_reminders():
    if not reminders:
        print("No reminders set.")
        return
    print("\n--- Reminders ---")
    for idx, r in enumerate(reminders, 1):
        print(f"{idx}. {r}")

def delete_reminder(index):
    if 0 < index <= len(reminders):
        removed = reminders[index-1]
        reminders.remove(removed)
        print(f"Deleted reminder: {removed}")
    else:
        print("Invalid reminder index!")

# Bubble sort for expenses
def bubble_sort(expenses_list):
    n = len(expenses_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if expenses_list[j][0] > expenses_list[j + 1][0]:
                expenses_list[j], expenses_list[j + 1] = expenses_list[j + 1], expenses_list[j]
    return expenses_list

# Initialize objects
expenses = LinkedList()
categories = HashTable()

# Main menu
while True:
    print("\n=== MoneyMap – Expense & Budget Tracker ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Category Totals")
    print("4. Add Reminder")
    print("5. View Reminders")
    print("6. View Sorted Expenses")
    print("7. Search Expenses by Category")
    print("8. Delete an Expense")
    print("9. Delete a Reminder")
    print("10. View Total Expenses")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amt = float(input("Enter Amount: "))
            cat = input("Enter Category: ")
            expenses.add_expense(amt, cat)
            categories.add_expense(cat, amt)
            print("Expense added successfully!")
        except ValueError:
            print("Invalid input! Please enter a number for amount.")

    elif choice == "2":
        expenses.display()

    elif choice == "3":
        categories.display()

    elif choice == "4":
        bill = input("Enter Reminder: ")
        add_reminder(bill)

    elif choice == "5":
        show_reminders()

    elif choice == "6":
        exp_list = expenses.to_list()
        if not exp_list:
            print("No expenses to sort.")
        else:
            sorted_exp = bubble_sort(exp_list)
            print("\n--- Expenses Sorted by Amount ---")
            for amt, cat in sorted_exp:
                print(f"Amount: {amt}, Category: {cat}")

    elif choice == "7":
        cat_search = input("Enter category to search: ")
        print(f"\n--- Expenses in category: {cat_search} ---")
        expenses.search_by_category(cat_search)

    elif choice == "8":
        try:
            amt = float(input("Enter amount to delete: "))
            cat = input("Enter category to delete: ")
            deleted = expenses.delete_expense(amt, cat)
            if deleted:
                categories.reduce_expense(cat, amt)
        except ValueError:
            print("Invalid input! Amount must be a number.")

    elif choice == "9":
        show_reminders()
        try:
            idx = int(input("Enter reminder number to delete: "))
            delete_reminder(idx)
        except ValueError:
            print("Invalid input! Enter a valid number.")

    elif choice == "10":
        total = sum(amount for amount, _ in expenses.to_list())
        print(f"\nTotal Expenses: {total}")

    elif choice == "11":
        print("Thank you for using MoneyMap – Expense & Budget Tracker! Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option.")
