# Example Project 2: Bank

## Project overview

Build an application that simulates a simple bank. It should let people manage a set of accounts and move money between them, such as:

- Creating and deleting accounts by ID
- Depositing and withdrawing money
- Transferring money between accounts
- Checking the balance of every account

Banking is a domain where small mistakes matter: a rounding error, a missed fee, or a transfer that only half-happens can leave accounts in an invalid state. Pay close attention to the rules for each operation, and to what should happen when an operation is invalid. This is why we do object-oriented design and hide private data fields behind public-facing accessor (getters) and mutators (setters) like `deposit()`, `withdraw()`, and `transfer()` - we can check and maintain state, reducing potential bugs.

## Initial goal: implement the BankAccount class

The current program has a main function that supports the BankAccount class. The full specification for the class, including deposit limits, overdraft fees, and transfer fees, is in the docstring at the top of `bankaccount/BankAccount.py`, along with a worked example of expected balances. Your first goal is to implement this functionality, both through test-driven development of the BankAccount test suite and BankAccount class, then by completing the `TODO`s in the main loop so that the `deposit`, `withdraw`, `transfer`, and `balance` commands work.

Before writing code, trace through the example in the docstring by hand, and turn each step into a test case. Think especially about edge cases: amounts of exactly $0.00 or $500.00, withdrawals that drop the balance below zero, and transfers from accounts with less than the $5.00 fee.

## BankAccount Specification

Write a Python class called BankAccount that represents a personal bank account:
1.	The class should have a constructor that takes a String representing the account ID as a parameter
2.	The class should have two accessor methods: 
o	get_id: returns the bank account’s ID
o	get_balance: returns the bank accounts current balance
3.	The class should have a method called deposit that adds a dollar amount to the balance, as long as the amount is between $0.00 and $500.00 (inclusive). If the number is outside that range, it raises a ValueError.
4.	The class should have a method called withdraw that removes a dollar amount from the balance. If the number is negative, it throws an ValueError. If the amount remaining in the account after withdrawal is negative, a $25.00 overdraft fee should be charged to the account.
5.	The class should have a method called transfer that moves money from this bank account to another account. The method accepts two parameters: a second BankAccount to accept the money, and a real number for the amount of money to transfer. There is a $5.00 fee for transferring money, so this much must be deducted from the current account’s balance before any transfer. The method should modify the two BankAccount objects such that “this” current object has its balance decreased by the given amount plus the $5 fee, and the other BankAccount object's balance is increased by the given amount. If this account object does not have enough money to make the full transfer, transfer whatever money is left after the $5 fee is deducted. If this account has under $5, then no transfer should occur and neither account's state should be modified. If the amount is less than 0 or more than $500.00, a ValueError should be raised.

Here is some example code using the BankAccount class, with balances shown in comments after each call:

```
    joey = BankAccount("Joey")
    phoebe = BankAccount("Phoebe")
 
    joey.deposit(120.00)      # joey $120, phoebe $0
    
    phoebe.deposit(25.00)       # joey $120, phoebe $25
    
    joey.withdraw(30.00)      # joey $90, phoebe $25
    
    joey.transfer(phoebe, 20.00) # joey $65, phoebe $45
                            # (joey loses $25, phoebe gains $20)
    
    joey.transfer(phoebe, 10.00) # joey $50, phoebe $55
                                # (joey loses $15, phoebe gains $10)
    
    phoebe.transfer(joey, 39.00) # joey $89, phoebe $11
                            # (phoebe loses $44, joey gains $39)
    
    phoebe.transfer(joey, 50.00) # joey $95, phoebe $ 0
                            # (phoebe loses $11, joey gains $ 6)
    
    phoebe.transfer(joey, 1.00)  # joey $95, phoebe $ 0
                            # (no effect; no money in account)
    
    joey.transfer(phoebe, 88.00) # joey $ 2, phoebe $88
                            # (joey loses $93, phoebe gains $88)
   
    joey.transfer(phoebe, 1.00)  # joey $ 2, phoebe $88
                            # (no effect; can't afford fee)

    print(f"{joey.get_id()} has ${joey.get_balance():.2f}")
    print(f"{phoebe.get_id()} has ${phoebe.get_balance():.2f}")
```

The output of this code for a BankAccount class that meets the specification would be:
```
Joey has $2.00
Phoebe has $88.00
```


## Stretch goal: support different kinds of accounts

Go beyond a single kind of account and support others, such as chequing accounts, savings accounts that earn interest, or accounts with different fees and limits. This is an opportunity to practice abstraction, reducing repetitive code, and refactoring. Consider using inheritance and abstract base classes to share common account behavior while allowing each kind of account to provide its own rules. You may have to do individual research here. Alternatively, design the model with private fields that represent the account type and its rules.

You might also keep a transaction history for each account, so that users can see every deposit, withdrawal, transfer, and fee that affected their balance.
