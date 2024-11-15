import threading
import time
import random

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()  # Lock to handle thread safety for transactions

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print(f"Failed to withdraw ${amount}. Insufficient balance: ${self.balance}")


def perform_transaction(account, transaction_type, amount):
    if transaction_type == 'deposit':
        account.deposit(amount)
    elif transaction_type == 'withdraw':
        account.withdraw(amount)


# Driver Code
account = BankAccount(balance=1000)
threads = []
transaction_types = ['deposit', 'withdraw']

for _ in range(5):  # Create 20 random transactions
    transaction_type = random.choice(transaction_types)
    amount = random.randint(50, 200)
    t = threading.Thread(target=perform_transaction, args=(account, transaction_type, amount))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nAll transactions completed.")
print(f"Final account balance: ${account.balance}")
