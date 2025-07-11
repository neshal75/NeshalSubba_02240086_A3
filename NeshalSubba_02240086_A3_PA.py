import tkinter as tk
from tkinter import messagebox

# Custom Exceptions 

class InvalidInputError(Exception):
    """When the user put invalid."""
    pass

class TransferError(Exception):
    """when the transfer of the balance connot be done."""
    pass

#  Bank Account Class 

class BankAccount:
    """this is a bank account for the user transaction."""

    def __init__(self, name, balance=0):
        """Initializing the account with name and balance."""
        self.name = name
        self.balance = balance

    def deposit_money(self, payment):
        """Depositing the money to the account."""
        if payment > 0:
            self.balance += payment
        else:
            raise InvalidInputError("the value of deposite muct be positive.")

    def money_withdraw(self, payment):
        """take out the money form the account."""
        if 0 < payment <= self.balance:
            self.balance -= payment
        else:
            raise TransferError("insufficient money, your account doesnot have money you required.")

    def money_transfer(self, payment, account_of_other):
        """Transfer money to another account."""
        if 0 < payment <= self.balance:
            self.balance -= payment
            account_of_other.balance += payment
        else:
            raise TransferError("wrong input or you have insufficient balance.")

    def top_up_mobile(self, user_phone_number, payment):
        """E- load to the mobile phone number."""
        if len(user_phone_number) == 8 and user_phone_number.isdigit() and payment > 0:
            if self.balance >= payment:
                self.balance -= payment
                print(f" YOUR NUMBER {user_phone_number} IS TOPPED UP WITH {payment} AMOUNT.")
            else:
                raise TransferError("Check your balance please, it is not sufficient.")
        else:
            raise InvalidInputError(" Wrong phone number, check once again.")

    def myamount(self):
        """reflecting the leftover balance."""
        return self.balance

# CLI Input Handler formate

def process_user_input(select, account, other_account):
    """Menu for the user to choose."""
    try:
        if select == '1':
            Your_amount = float(input("Enter your money for deposit: "))
            account.deposit_money(Your_amount)
        elif select == '2':
            Your_amount = float(input("Enter the amount you want to withdraw: "))
            account.money_withdraw(Your_amount)
        elif select == '3':
            print("Your current balance:", account.my_balance())
        elif select == '4':
            friend_account_number = input("Enter the 10-digit friend's account number: ")
            if not (friend_account_number.isdigit() and len(friend_account_number) == 10):
                raise InvalidInputError("Friend's account number must be exactly 10 digits.")
            Your_amount = float(input(" How much is Transfer AMOUNT: "))
            account.money_transfer(Your_amount, other_account)
            print(f"amount sent {Your_amount} to your friend {friend_account_number}")
        elif select == '5':
            phone = input("Please enter your phone number: ")
            Your_amount = float(input("Enter amount: "))
            account.top_up_mobile(phone, Your_amount)
        elif select == '6':
            print("Leaving the program, BYE BYE...")
            return False
        else:
            raise InvalidInputError("Invalid menu choice.")
    except (InvalidInputError, TransferError, ValueError) as e:
        print("IT'S A ERROR, ENTER THE CORRECT INPUT:", e)
    return True

def running_CLI():
    """Run the CLI banking application."""
    your_account = BankAccount("Owner", 5123)
    Another_account = BankAccount("Friend", 100)

    Run = True
    while Run:
        print("\n Menu")
        print("1.To deposite your amount")
        print("2. To take out the money")
        print("3. To check the amount you have")
        print("4. Money transfer")
        print("5. Mobile Top-Up")
        print("6. Exit The Program")
        choice = input("Please select the number from (1-6): ")
        Run = process_user_input(choice, your_account, Another_account)

# GUI Application

class BankGUI:
    """Creating the GUI interface."""

    def __init__(self, master):
        self.master = master
        master.title("BANK")

        self.account = BankAccount("Owner", 5123)

        # Balance Label
        self.balance_label = tk.Label(master, text="Balance: 5123.0", font=('Calibri', 16))
        self.balance_label.pack(pady=10)

        # Amount Entry
        self.amount_label = tk.Label(master, text="Please enter your amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack(pady=5)

        # Phone Number Entry
        self.phone = tk.Label(master, text=" 8-digit Phone Number:")
        self.phone.pack()
        self.phone_entry = tk.Entry(master)
        self.phone_entry.pack(pady=5)

        self.friend = tk.Label(master, text=" Friend's Account Number:")
        self.friend.pack()
        self.entry_of_friend = tk.Entry(master)
        self.entry_of_friend.pack(pady=5)        

        # Buttons
        self.deposite = tk.Button(master, text="Deposit money", command=self.deposit)
        self.deposite.pack(pady=2)

        self.button_for_withdraw = tk.Button(master, text="Withdraw money", command=self.withdraw)
        self.button_for_withdraw.pack(pady=2)

        self.Botton_for_transfer = tk.Button(master, text="Transfer money", command=self.transfer_to_friend)
        self.Botton_for_transfer.pack(pady=2)

        self.button_for_topup = tk.Button(master, text="Mobile Top-Up", command=self.top_up)
        self.button_for_topup.pack(pady=2)

        self.refresh_button = tk.Button(master, text="view your current Balance", command=self.show_amount)
        self.refresh_button.pack(pady=2)

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            self.account.deposit_money(amount)
            self.show_amount()
        except Exception as e:
            messagebox.showerror("it's wrong", str(e))

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            self.account.money_withdraw(amount)
            self.show_amount()
        except Exception as e:
            messagebox.showerror("it;s an error", str(e))


    def transfer_to_friend(self):
        try:
            amount = float(self.amount_entry.get())
            friend_account_number = self.entry_of_friend.get()
            if not (friend_account_number.isdigit() and len(friend_account_number) == 10):
                raise InvalidInputError("Friend's account number must be exactly 10 digits.")
            self.friend_account = BankAccount("Friend", 1000)

            self.account.money_transfer(amount, self.friend_account)
            self.show_amount()
            messagebox.showinfo("Successful", f"Transferred {amount} to account {friend_account_number}")
        except Exception as e:
            messagebox.showerror("FAILED! Cannot transfer money", str(e))    
  

    def top_up(self):
        try:
            phone = self.phone_entry.get()
            amount = float(self.amount_entry.get())
            self.account.top_up_mobile(phone, amount)
            self.show_amount()
            messagebox.showinfo("Done", f"Your top-up successful for {phone}")
        except Exception as e:
            messagebox.showerror("Top-Up does not worked", str(e))

    def show_amount(self):
        self.balance_label.config(text=f"remaining money: {self.account.myamount():.2f}")


def running_GUI():
    """start the GUI"""
    root = tk.Tk()
    app = BankGUI(root)
    root.mainloop()

#  Main Launcher 

if __name__ == "__main__":
    print("Choose app mode:")
    print("1. Command Line Interface (CLI)")
    print("2. Graphical User Interface (GUI)")
    mode = input("Enter 1 or 2: ")

    if mode == '1':
        running_CLI()
    elif mode == '2':
        running_GUI()
    else:
        print("Invalid INPUT.")
