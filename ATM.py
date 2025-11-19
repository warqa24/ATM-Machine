# ATM Machine
import tkinter as tk
from tkinter import messagebox

# Initial balance
balance = 1000

def account_verification(account_number):
    if len(account_number) != 6 or not account_number.isdigit():
        raise ValueError ("Invalid account number format. Please enter a 6-digit account number.")

def pin_verification(pin_number):
    if len(pin_number) != 4 or not pin_number.isdigit():
        raise ValueError ("Invalid PIN format. The PIN must be 4 digits.")

def withdraw_handling(amount):
    global balance

    try:
        withdraw_money = float(amount)
        if withdraw_money > balance:
            raise ValueError ("Insufficient balance. Transaction denied")
        balance -= withdraw_money
        return f"£{withdraw_money} successfully withdrawn. New balance is £{balance}"
    except ValueError as e:
        return str(e)

def deposit(amount):
    global balance

    try:
        deposit_money = float(amount)
        balance += deposit_money
        return f"£{deposit_money} amount successfully deposited. Current balance is £{balance}"
    except ValueError:
        return "Invalid amount. Please enter a numeric value"

def submit_action(action):
    account_number = account_entry.get()
    pin_number = pin_entry.get()
    amount = amount_entry.get()

    try:
        account_verification(account_number)
        pin_verification(pin_number)

        if action == "withdraw":
            message = withdraw_handling(amount)
        elif action == "deposit":
            message = deposit(amount)
        elif action == "check balance":
            message = f"Your current balance is £{balance}"
        else:
            message = "Invalid operation"

        messagebox.showinfo("Operation result", message)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    finally:
        amount_entry.delete(0, tk.END)

def exit_program():
    messagebox.showinfo("Exit", "Thank you for using the ATM")
    root.destroy()

# Set up the GUI
root = tk.Tk()
root.title("ATM Simulator")

root.geometry("400x300")

# Account Number
tk.Label(root, text="Account Number").pack()
account_entry = tk.Entry(root)
account_entry.pack()

# PIN
tk.Label(root, text="PIN").pack()
pin_entry = tk.Entry(root, show="*")
pin_entry.pack()

# Amount
tk.Label(text="Amount (£)").pack()
amount_entry = tk.Entry()
amount_entry.pack()

# Create buttons for different operations
withdraw_button = tk.Button(root, text="Withdraw", command=lambda: submit_action("withdraw"))
withdraw_button.pack(pady=5)

deposit_button = tk.Button(root, text="Deposit", command=lambda: submit_action("deposit"))
deposit_button.pack(pady=5)

balance_button = tk.Button(root, text="Check Balance", command=lambda: submit_action("check balance"))
balance_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack()

# Run the main loop
root.mainloop()