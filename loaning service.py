class account(object):
    account_number = 0 #number of accounts in the bank.
    def __init__(self):
        self.account_number += 1 #the number of accounts made is increased each time an instance of account is created.
        self.account_id = self.account_number #dependent on the total number of account made in the bank. Each account will have a unique id.
        self.balance = 0 #intial balance of every account is 0
        
class borrower(account):
    def account_type(self):
        self.account_type = "borrower" #this is a borrower account, child class of account
        print("This account is a", self.account_type, "account")
    def take_loan(self, bank, amount, total_balance, duration, loan_rate): #function to take loan
        if (total_balance >= amount): #checking if bank has enough money to give the loan
            self.balance += amount #adding loan amount to account
            bank.total_balance -= amount #removing loan amount from bank balance
            interest = amount*((1 + (loan_rate/100))**duration) - amount #calculating compound interest on amount
            print("The loan is valid, the total interest to be paid will be", interest)
            print("The total amount will be", interest + amount)
        else:
            print("The loan amount is more than the current balance available with the bank")

        
    
class lender(account): 
    def account_type(self):
        self.account_type = "lender" #this is a lender account, child class of account
        print("This account is a", self.account_type, "account")
    def deposit(self, bank, amount, total_balance, duration, deposit_rate): #function to put deposit in bank
        bank.total_balance += amount #adding amount to bank balance
        self.balance += amount #adding amount to self account
        interest = amount*((1 + (deposit_rate/100))**duration) - amount #calculating interest on amount in future
        print("This will amount to", interest + amount, "in", duration, "years")

class customer(object):
    def __init__(self, name, age): #taking customer details
        self.name = name
        self.age = age
        self.accounts = [] #creating a list containing all account objects of a particular customer
    def add_account_lender(self):
        self.accounts.append(lender()) #appending a lender account
        print("added lender account")
    def add_account_borrower(self):
        self.accounts.append(borrower()) #appending a borrower account
        print("added borrower account")

class Loaning_system(object):
    customer_number = 0 #number of customers in the bank.
    total_balance = 100000 #net amount of money in the bank (starting with 1 lakh)
    loan_rate = 5 #assuming a fixed loan rate for simplicity
    deposit_rate = 3 #assuming a fixed deposit rate 
    
    customer_db = {} #database of all customers.
    def add_customer(self, name, age):
        self.customer_number += 1 
        self.customer_db[self.customer_number] = customer(name, age) #adding a customer number and customer object as a key value pair to the dictionary
        print("new customer added:", self.customer_db)


        
bank = Loaning_system() #creating an instance of the loaning system
bank.add_customer("mehar", 25) #adding the first customer
bank.add_customer("manya",31) #adding the second customer


bank.customer_db[1].add_account_lender() #adding a lending account for the first customer
bank.customer_db[2].add_account_borrower() #adding a borrowing account for the second customer
bank.customer_db[2].add_account_lender() #adding a lending account for the second customer
print("printing customer 1 details", bank.customer_db[1].name,bank.customer_db[1].age,bank.customer_db[1].accounts) 
print("printing customer 2 details", bank.customer_db[2].name,bank.customer_db[2].age,bank.customer_db[2].accounts)

bank.customer_db[1].accounts[0].deposit(bank, 10000, bank.total_balance, 10, bank.deposit_rate) #customer 1 lending money to the bank
print("Bank balance =", bank.total_balance, "customer 1 balance =", bank.customer_db[1].accounts[0].balance)
bank.customer_db[2].accounts[0].take_loan(bank, 5000, bank.total_balance, 10, bank.loan_rate) #customer 2 taking a loan
print("Bank balance =", bank.total_balance, "customer 2 balance =", bank.customer_db[2].accounts[0].balance)
    
    
