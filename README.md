---

# 💰 Personal Expense Tracker (GUI)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green)
![Database](https://img.shields.io/badge/Database-SQLite-orange)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

---

## 📌 Overview  
This project is a desktop-based personal expense tracker that helps users manage their daily expenses efficiently. It is built using **Python**, features a **Tkinter GUI**, and uses **SQLite** for persistent data storage.

---

## 🚀 Features  
- ➕ Add expenses (amount, category, description, date)  
- 📋 View all expenses in a table format  
- ❌ Delete selected expense  
- 📊 Calculate total expenses  
- 🗑️ Clear all records with confirmation  
- 💾 Persistent storage using SQLite database  

---

## 🛠️ Technologies Used  
- **Programming Language:** Python  
- **GUI Framework:** Tkinter  
- **Database:** SQLite3  

---

## 📂 Project Structure

personal_expense_tracker/ │ ├── gui_expense_tracker.py   # Main GUI application ├── expenses.db              # SQLite database (auto-created) └── README.md                # Project documentation

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  

- git clone https://github.com/your-username/personal-expense-tracker.git
- cd personal-expense-tracker

---

### 2️⃣ Create Virtual Environment (Optional but Recommended)

- python -m venv venv
- venv\Scripts\activate   # Windows


---

### 3️⃣ Install Dependencies

- pip install tabulate


---

### 4️⃣ Run the Application

- python gui_expense_tracker.py


---

## 🧪 Testing

- ✅ Add expense → Data appears in table

- ❌ Empty fields → Error message shown

- ❌ Delete without selection → Warning displayed

- ✅ Total button → Shows sum of expenses

- ✅ Clear all → Deletes all records after confirmation



---

## 📸 Output

### Displays:

### Expense ID

### Amount

### Category

### Description

### Date

### Total Expense Calculation



---

## 🔮 Future Enhancements

- 📊 Monthly expense charts and analytics

- 🔍 Search and filter functionality

- 📤 Export data to Excel/CSV

- 🔐 User authentication system

- 🌐 Web version using Flask



---

## 👨‍💻 Author

- Mohammed Nouman

- GitHub: https://github.com/mohammednouman555

- LinkedIn: https://www.linkedin.com/in/mohammed-nouman-2a8989343



---

## 📄 License

- This project is open-source and available for learning and educational purposes.

---
