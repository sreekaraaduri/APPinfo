import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store data
DATA_FILE = "accounts.json"

# Load existing data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

accounts = load_data()

# Create Account
def create_account():
    acc = entry_acc.get()
    bal = entry_amount.get()

    if acc in accounts:
        messagebox.showerror("Error", "Account already exists!")
        return

    try:
        bal = float(bal)
    except:
        messagebox.showerror("Error", "Invalid amount!")
        return

    accounts[acc] = {"balance": bal, "history": [f"Account created with {bal}"]}
    save_data(accounts)
    messagebox.showinfo("Success", "Account created successfully!")

# Deposit
def deposit():
    acc = entry_acc.get()
    amt = entry_amount.get()

    if acc not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    try:
        amt = float(amt)
    except:
        messagebox.showerror("Error", "Invalid amount!")
        return

    accounts[acc]["balance"] += amt
    accounts[acc]["history"].append(f"Deposited {amt}")
    save_data(accounts)

    messagebox.showinfo("Success", f"Deposited {amt}")

# Withdraw
def withdraw():
    acc = entry_acc.get()
    amt = entry_amount.get()

    if acc not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    try:
        amt = float(amt)
    except:
        messagebox.showerror("Error", "Invalid amount!")
        return

    if accounts[acc]["balance"] < amt:
        messagebox.showerror("Error", "Insufficient funds!")
        return

    accounts[acc]["balance"] -= amt
    accounts[acc]["history"].append(f"Withdrew {amt}")
    save_data(accounts)

    messagebox.showinfo("Success", f"Withdrew {amt}")

# Check Balance
def check_balance():
    acc = entry_acc.get()

    if acc not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    bal = accounts[acc]["balance"]
    messagebox.showinfo("Balance", f"Balance: {bal}")

# Transfer
def transfer():
    from_acc = entry_acc.get()
    to_acc = entry_target.get()
    amt = entry_amount.get()

    if from_acc not in accounts or to_acc not in accounts:
        messagebox.showerror("Error", "One or both accounts not found!")
        return

    try:
        amt = float(amt)
    except:
        messagebox.showerror("Error", "Invalid amount!")
        return

    if accounts[from_acc]["balance"] < amt:
        messagebox.showerror("Error", "Insufficient funds!")
        return

    accounts[from_acc]["balance"] -= amt
    accounts[to_acc]["balance"] += amt

    accounts[from_acc]["history"].append(f"Transferred {amt} to {to_acc}")
    accounts[to_acc]["history"].append(f"Received {amt} from {from_acc}")

    save_data(accounts)

    messagebox.showinfo("Success", "Transfer successful!")

# View History
def view_history():
    acc = entry_acc.get()

    if acc not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    history = "\n".join(accounts[acc]["history"])
    messagebox.showinfo("Transaction History", history)


# GUI Setup
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("💳 Bank Account Management System")
root.geometry("500x550")
root.config(bg="#1e1e2f")

# Title
title = tk.Label(
    root,
    text="🏦 Bank System",
    font=("Helvetica", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=15)

# Frame for inputs
frame = tk.Frame(root, bg="#2c2c3e", bd=2, relief="ridge")
frame.pack(pady=10, padx=20, fill="both")

# Labels & Entries
def styled_label(text):
    return tk.Label(frame, text=text, font=("Arial", 12), bg="#2c2c3e", fg="white")

def styled_entry():
    return tk.Entry(frame, font=("Arial", 12), bd=2, relief="groove")

styled_label("Account Number").pack(pady=5)
entry_acc = styled_entry()
entry_acc.pack(pady=5)

styled_label("Target Account").pack(pady=5)
entry_target = styled_entry()
entry_target.pack(pady=5)

styled_label("Amount").pack(pady=5)
entry_amount = styled_entry()
entry_amount.pack(pady=5)

# Button style
def styled_button(text, command, color):
    return tk.Button(
        root,
        text=text,
        command=command,
        font=("Arial", 11, "bold"),
        bg=color,
        fg="white",
        activebackground="#444",
        width=20,
        bd=0,
        pady=5
    )

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=20)

styled_button("Create Account", create_account, "#4CAF50").pack(pady=5)
styled_button("Deposit", deposit, "#2196F3").pack(pady=5)
styled_button("Withdraw", withdraw, "#f44336").pack(pady=5)
styled_button("Check Balance", check_balance, "#9C27B0").pack(pady=5)
styled_button("Transfer", transfer, "#FF9800").pack(pady=5)
styled_button("View History", view_history, "#00BCD4").pack(pady=5)

root.mainloop()