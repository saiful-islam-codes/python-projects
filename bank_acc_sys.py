class Account:
    def __init__(self, name, acc_num , balance):
        self.name = name
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, add_balance):
        self.balance = self.balance + add_balance 

    def withdraw(self,  withdraw_balance):
        self.balance = self.balance - withdraw_balance

    def check_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = []

    # def create_Acc(self, name, acc_num, balance):
    #     new_acc = Account(name, acc_num, balance)
    #     self.accounts.append(new_acc)

    def create_acc(self, acc):
        self.accounts.append(acc)

    def find_acc(self, account_num):
        for i in self.accounts:
            if i.acc_num ==  account_num:
                return i 

    def remove_account(self, acc_num):
        for account in self.accounts:
            if account.acc_num == acc_num:
                self.accounts.remove(account)
                print("Account removed successfully.")
                return

        print("Account not found.")


acc1 = Account("Saif", 25353, 5000)
print(acc1.name)
print(acc1.acc_num)
print(acc1.balance)

print(acc1)

manager = Bank()

manager.create_acc(acc1)

acc1.deposit(2000)
print(acc1.check_balance())

acc1.withdraw(1000)
print(acc1.check_balance())

manager.remove_account(25353)

