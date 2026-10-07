from datetime import datetime

class Account:
    def __init__(self, id, number, holder, type,balance,status):
        self.id = id
        self.number = number 
        self.holder = holder 
        self.type = type
        self.balance = balance
        self.status = status
        self.transactions = []

    def deposit(self, add_balance):
        self.balance = self.balance + add_balance
        print(self.balance)    

        transaction = Transaction(
            "Deposit",
            add_balance,
            destination_account=self
        )
        
        self.transactions.append(transaction)

        print("Balance:", self.balance)

        return transaction

    def withdraw(self, w_balance):
        self.balance = self.balance - w_balance
        print(self.balance)       

        transaction = Transaction(
            "Withdraw", 
            w_balance, 
            destination_account=None
        )

        self.transactions.append(transaction)
        print("Balance: ", self.balance)
        return transaction





    def transfer(self, receiver, t_balance):
        self.balance = self.balance - t_balance
        receiver.balance = receiver.balance + t_balance

        print(f"{self} existing money {self.balance}")
        print(f"{receiver} existing money {receiver.balance}")



        transaction = Transaction(
            "Transfer",
            t_balance,
            source_account=self,
            destination_account=receiver
        )

        self.transactions.append(transaction)
        receiver.transactions.append(transaction)

        print("Sender Balance:", self.balance)
        print("Receiver Balance:", receiver.balance)

        return transaction

    def set_status(self, status):
        if self.status == "Active":
            self.status = status
        elif status == "Inactive":
            self.status = status

        elif status == "Blocked":
            self.status = status

        elif status == "Closed":
            self.status = status

        else:
            print("Invalid status")

        print(self.status)

    def balance_rules(self, w_amount):
        if (self.balance - w_amount) >= 500 :
            self.withdraw(w_amount)
        else:
            print(self.balance - w_amount)

     
                        

             
class SavingAccount(Account):
    def interest(self, int_rate):
        self.balance = self.balance + (self.balance * int_rate/100)
        return self.balance        

    def minimum_balance(self, wi_balance):
        self.balance_rules(wi_balance)


class CurrentAccount(Account):
    def overdraft(self, od_money , wi_amount):
        od_money = 2000
        remaining_balance = (self.balance - wi_amount)
        if remaining_balance >= -od_money:
            print("withdraw..")
            return remaining_balance
        else:
            print("Rejected!..")    
    def service_charge(self):
        pass

class Transaction:
    _next_id = 1

    def __init__(self, type, amount, source_account=None, destination_account=None):
        self.transaction_id = f"T{Transaction._next_id:03d}"
        Transaction._next_id += 1

        self.type = type
        self.amount = amount
        self.source_account = source_account
        self.destination_account = destination_account
        self.timestamp = datetime.now()
        self.status = "Success"

    def show_transaction(self):
        print("Transaction ID:", self.transaction_id)
        print("Type:", self.type)
        print("Amount:", self.amount)
        print("Time:", self.timestamp)
        print("Status:", self.status)




        
class Customer:
    def __init__(self, id, name, phoneNo, email, address):
        self.accounts = []
        self.id = id
        self.name = name
        self.phoneNo = phoneNo
        self.email = email
        self.address = address

    def set_idPass(self, id, password):
            self.id = id 
            self.password = password   


    def auth(self, id, password):
        if self.id ==  id and self.password == password:
            print("You are logging in......")
        elif self.id != id and self.password == password:
            print("Your id is incorrent.")
        elif self.id == id and self.password != password:
            print("Your password is incorrect.")
        else:
            print("Access denied!!!")            
          

    def accs(self,Acc):
        self.accounts.append(Acc)
        
        
        


class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []
        self.transactions = []
    def customers_list(self, customer):
        self.customers.append(customer)
    def accounts_list(self, account):
        self.accounts.append(account)    
    def transaction_list(self, transaction):
        self.transactions.append(transaction)
    def rmv_c(self, customer_name):
        for customer in self.customers:
            if customer.name == customer_name:
                return self.customers.remove(customer)  
    def rmv_a(self, account_number):
        for account in self.accounts:
            if account.number == account_number:
                return self.accounts.remove(account)   

    def update_cus(self, customer_name, name, id, email, phoneNo, address):
        for c in self.customers:
            if c.name == customer_name:
                c.name = name 
                c.id = id
                c.email = email
                c.phoneNo = phoneNo
                c.address = address
                
    def find_customer(self, customer_name):
        for i in self.customers:
            if i.name == customer_name:
                return i 


    def find_accounts(self, account_number):
        for i in self.accounts:
            if i.number== account_number:
                return i 
           

    def find_transaction(self, transaction_id):
        for i in self.transactions:
            if i.transaction_id == transaction_id:
                return i



    def ServiceCharges(self):
        pass

    def deposit_n(self, account_id, amount):
        for account in self.accounts:
            if account.id == account_id:
                transaction = account.deposit(amount)
                self.transactions.append(transaction)
                return True
        return False    

    def withdraw_n(self, account_id, amount):
        for account in self.accounts:
            if account.id == account_id:
                transaction =account.withdraw(amount)
                self.transactions.append(transaction)
                return True

        return False    



    def transfer_n(self, sender_id, receiver_id, amount):
        sender_account = None
        receiver_account = None

        for account in self.accounts:
            if account.id == sender_id:
                sender_account = account

            if account.id == receiver_id:
                receiver_account = account

        if sender_account is not None and receiver_account is not None:
            transaction = sender_account.transfer(receiver_account, amount)
            self.transactions.append(transaction)
            return True

        return False
    

bank = Bank()

c1 = Customer(1, "Rahim", "01711111111", "rahim@gmail.com", "Dhaka")
c2 = Customer(2, "Karim", "01822222222", "karim@gmail.com", "Dhaka")

bank.customers_list(c1)
bank.customers_list(c2)

c1.set_idPass(101, "1234")
c2.set_idPass(102, "5678")

print("\n--- Authentication ---")

c1.auth(101, "1234")
c1.auth(101, "9999")
c1.auth(999, "1234")
c1.auth(999, "9999")

a1 = SavingAccount(1, "SA1001", c1, "Savings", 5000, "Active")
a2 = CurrentAccount(2, "CA1002", c2, "Current", 3000, "Active")

c1.accs(a1)
c2.accs(a2)

bank.accounts_list(a1)
bank.accounts_list(a2)

print("\n--- Deposit ---")

bank.deposit_n(1, 2000)

print("A1 Balance:", a1.balance)

print("\n--- Withdraw ---")

bank.withdraw_n(1, 1000)

print("A1 Balance:", a1.balance)

print("\n--- Transfer ---")

bank.transfer_n(1, 2, 1500)

print("A1 Balance:", a1.balance)
print("A2 Balance:", a2.balance)

print("\n--- Interest ---")

a1.interest(5)

print("A1 Balance after interest:", a1.balance)

print("\n--- Overdraft ---")

a2.overdraft(2000, 4000)

print("\n--- Status ---")

a1.set_status("Blocked")
a1.set_status("Active")

print("\n--- Find Customer ---")

found_customer = bank.find_customer("Rahim")
print(found_customer.name)

print("\n--- Find Account ---")

found_account = bank.find_accounts("SA1001")
print(found_account.number)

print("\n--- A1 Transactions ---")

for transaction in a1.transactions:
    transaction.show_transaction()

print("\n--- A2 Transactions ---")

for transaction in a2.transactions:
    transaction.show_transaction()

print("\n--- Bank Transactions ---")

for transaction in bank.transactions:
    transaction.show_transaction()

print("\n--- Find Transaction ---")

found_transaction = bank.find_transaction("T001")

if found_transaction:
    found_transaction.show_transaction()