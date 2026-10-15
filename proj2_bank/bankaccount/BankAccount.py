'''
Write a Python class called BankAccount that represents a personal bank account:
1.	The class should have a constructor that takes a String representing the account ID as a parameter
2.	The class should have two accessor methods: 
o	get_id: returns the bank account’s ID
o	get_balance: returns the bank accounts current balance
3.	The class should have a method called deposit that adds a dollar amount to the balance, as long as the amount is between $0.00 and $500.00 (inclusive). If the number is outside that range, it raises a ValueError.
4.	The class should have a method called withdraw that removes a dollar amount from the balance. If the number is negative, it throws an ValueError. If the amount remaining in the account after withdrawal is negative, a $25.00 overdraft fee should be charged to the account.
5.	The class should have a method called transfer that moves money from this bank account to another account. The method accepts two parameters: a second BankAccount to accept the money, and a real number for the amount of money to transfer. There is a $5.00 fee for transferring money, so this much must be deducted from the current account’s balance before any transfer. The method should modify the two BankAccount objects such that “this” current object has its balance decreased by the given amount plus the $5 fee, and the other BankAccount object's balance is increased by the given amount. If this account object does not have enough money to make the full transfer, transfer whatever money is left after the $5 fee is deducted. If this account has under $5, then no transfer should occur and neither account's state should be modified. If the amount is less than 0 or more than $500.00, a ValueError should be raised.

Here is some example code using the BankAccount class, with balances shown in comments after each call:
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
The output of this code for a BankAccount class that meets the specification would be:
Joey has $2.00
Phoebe has $88.00

'''

class BankAccount():

    def __init__(self, account_id : str):
        """ BankAccount
            TODO: Docstring
        """
        # stub
        raise NotImplementedError()




# Main function for quick informal testing without main program logic
if __name__ == "__main__":
    joey = BankAccount("Joey")
    phoebe = BankAccount("Joey")