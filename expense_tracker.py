import sqlite3
from tabulate import tabulate

# -----------------------------
# Database Setup
# -----------------------------
def setup_database():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        date TEXT,
        description TEXT
    )''')
    conn.commit()
    conn.close()


# -----------------------------
# Helper: Resequence IDs
# -----------------------------
def resequence_ids():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    # Retrieve all records ordered by old ID
    c.execute("SELECT amount, category, date, description FROM expenses ORDER BY id")
    rows = c.fetchall()

    # Drop and recreate table
    c.execute("DROP TABLE IF EXISTS expenses")
    c.execute('''CREATE TABLE expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        date TEXT,
        description TEXT
    )''')

    # Insert data back sequentially
    for row in rows:
        c.execute("INSERT INTO expenses(amount, category, date, description) VALUES (?, ?, ?, ?)", row)

    conn.commit()
    conn.close()


# -----------------------------
# Add a new expense
# -----------------------------
def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a numeric value.")
        return

    category = input("Enter category (Food, Travel, etc.): ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    description = input("Enter description: ").strip()

    if not category or not date:
        print("❌ Category and Date cannot be empty.")
        return

    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses(amount, category, date, description) VALUES (?, ?, ?, ?)",
              (amount, category, date, description))
    conn.commit()
    conn.close()
    print("✅ Expense added successfully!")


# -----------------------------
# View all expenses
# -----------------------------
def view_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT id, amount, category, date, description FROM expenses")
    rows = c.fetchall()
    conn.close()

    if rows:
        print("\n📊 Expense Records:")
        print(tabulate(rows, headers=["ID", "Amount", "Category", "Date", "Description"], tablefmt="grid"))
    else:
        print("No expenses found.")


# -----------------------------
# View a specific expense by ID or category
# -----------------------------
def view_specific_expense():
    search_type = input("Search by (id/category): ").lower()

    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    if search_type == "id":
        try:
            expense_id = int(input("Enter expense ID: "))
        except ValueError:
            print("❌ Invalid ID.")
            conn.close()
            return
        c.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    elif search_type == "category":
        category = input("Enter category name: ").strip()
        c.execute("SELECT * FROM expenses WHERE LOWER(category) = LOWER(?)", (category,))
    else:
        print("❌ Invalid choice.")
        conn.close()
        return

    rows = c.fetchall()
    conn.close()

    if rows:
        print("\n🔎 Matching Expenses:")
        print(tabulate(rows, headers=["ID", "Amount", "Category", "Date", "Description"], tablefmt="grid"))
    else:
        print("No matching expenses found.")


# -----------------------------
# View total expenses
# -----------------------------
def view_total_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM expenses")
    total = c.fetchone()[0]
    conn.close()
    print(f"\n💰 Total Expenses: {total if total else 0:.2f}")


# -----------------------------
# Delete expense by ID or category
# -----------------------------
def delete_expense():
    delete_type = input("Delete by (id/category): ").lower()

    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    if delete_type == "id":
        try:
            expense_id = int(input("Enter the ID to delete: "))
        except ValueError:
            print("❌ Invalid ID.")
            conn.close()
            return
        c.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
        record = c.fetchone()
        if record:
            c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            conn.commit()
            print(f"✅ Expense with ID {expense_id} deleted successfully!")
        else:
            print("❌ No expense found with that ID.")

    elif delete_type == "category":
        category = input("Enter category to delete all records from: ").strip()
        c.execute("SELECT * FROM expenses WHERE LOWER(category) = LOWER(?)", (category,))
        records = c.fetchall()
        if records:
            confirm = input(f"⚠️ Delete all {len(records)} record(s) in category '{category}'? (yes/no): ").lower()
            if confirm == "yes":
                c.execute("DELETE FROM expenses WHERE LOWER(category) = LOWER(?)", (category,))
                conn.commit()
                print(f"✅ All expenses from category '{category}' deleted successfully!")
            else:
                print("Operation cancelled.")
        else:
            print("❌ No expenses found for that category.")
    else:
        print("❌ Invalid choice.")

    conn.close()
    # After deletion, resequence IDs to maintain order
    resequence_ids()


# -----------------------------
# Clear all expenses
# -----------------------------
def clear_all_expenses():
    confirm = input("⚠️ Are you sure you want to delete ALL expenses? (yes/no): ").lower()
    if confirm == "yes":
        conn = sqlite3.connect('expenses.db')
        c = conn.cursor()
        c.execute("DELETE FROM expenses")
        conn.commit()
        conn.close()
        print("🧹 All expenses cleared successfully!")
    else:
        print("Operation cancelled.")


# -----------------------------
# Main Program
# -----------------------------
def main():
    setup_database()
    print("📘 Welcome to Personal Expense Tracker")
    while True:
        print("\n1. Add Expense\n2. View All Expenses\n3. View Specific Expense\n4. View Total\n5. Delete Expense\n6. Clear All Expenses\n7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_specific_expense()
        elif choice == "4":
            view_total_expenses()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            clear_all_expenses()
        elif choice == "7":
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
