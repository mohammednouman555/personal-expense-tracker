import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import os

# ================= DATABASE SETUP =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "expenses.db")


def connect_db():
    return sqlite3.connect(DB_PATH)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            description TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()


# ================= FUNCTIONS =================

def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()
    description = description_entry.get()
    date = date_entry.get()

    if not amount or not category or not date:
        messagebox.showerror("Error", "Please fill required fields")
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
        (amount, category, description, date)
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Expense Added!")
    clear_fields()
    view_expenses()


def view_expenses():
    for row in tree.get_children():
        tree.delete(row)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        tree.insert("", tk.END, values=row)


def delete_expense():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "Select an expense to delete")
        return

    item = tree.item(selected[0])
    expense_id = item['values'][0]

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Deleted", "Expense deleted successfully")
    view_expenses()


def show_total():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    conn.close()

    total = total if total else 0
    messagebox.showinfo("Total Expense", f"Total = ₹{total}")


def clear_all():
    confirm = messagebox.askyesno("Confirm", "Delete ALL expenses?")
    if confirm:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses")
        conn.commit()
        conn.close()
        view_expenses()


def clear_fields():
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)


# ================= GUI SETUP =================

root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("750x500")

create_table()

# ===== INPUT FRAME =====
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Amount").grid(row=0, column=0)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=0, column=1)

tk.Label(frame, text="Category").grid(row=1, column=0)
category_entry = tk.Entry(frame)
category_entry.grid(row=1, column=1)

tk.Label(frame, text="Description").grid(row=2, column=0)
description_entry = tk.Entry(frame)
description_entry.grid(row=2, column=1)

tk.Label(frame, text="Date (YYYY-MM-DD)").grid(row=3, column=0)
date_entry = tk.Entry(frame)
date_entry.grid(row=3, column=1)

# ===== BUTTONS =====
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Expense", command=add_expense).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete Expense", command=delete_expense).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Show Total", command=show_total).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Clear All", command=clear_all).grid(row=0, column=3, padx=5)

# ===== TABLE =====
columns = ("ID", "Amount", "Category", "Description", "Date")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill=tk.BOTH, expand=True)

# Load data initially
view_expenses()

# Run app
root.mainloop()