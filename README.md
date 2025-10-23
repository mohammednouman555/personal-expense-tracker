📘 Personal Expense Tracker

A simple, command-line-based Personal Expense Tracker built with Python and SQLite, designed to record, view, and manage your daily expenses efficiently.

🚀 Features

💰 Add new expenses (amount, category, date, and description)

📊 View all expenses in a neat, tabular format

🔍 View specific expenses by ID or category

❌ Delete expenses by ID or category

🔢 Automatically resequences IDs after deletions

🧹 Clear all expenses with confirmation

💾 Data stored persistently using SQLite

🛠️ Tech Stack

Language: Python 3.x

Database: SQLite

Library Used: tabulate

⚙️ Setup & Installation

Clone the repository:

git clone https://github.com/mohammednouman555/personal_expense_tracker.git
cd personal_expense_tracker


Create a virtual environment:

python -m venv .venv


Activate the environment:

.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the application:

python expense_tracker.py

🧩 How It Works

Main Menu Options

1. Add Expense
2. View All Expenses
3. View Specific Expense
4. View Total
5. Delete Expense
6. Clear All Expenses
7. Exit


Example:

Enter amount: 150
Enter category: Food
Enter date: 2025-10-23
Enter description: Lunch with friends
✅ Expense added successfully!

📸 Sample Output
ID	Amount	Category	Date	Description
1	150.0	Food	2025-10-23	Lunch with friends
2	80.0	Travel	2025-10-23	Auto fare
🧠 Author

Mohammed Nouman
🎓 Computer Science Engineering Student, Deccan College of Engineering and Technology
📧 mohammednouman555@gmail.com

🔗 GitHub
 | LinkedIn

🪪 License

This project is open-source and available under the MIT License.