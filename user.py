class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 1000
    def make_deposit(self, amount):
        self.account_balance += amount	
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        self.account_balance
        return self

    def transfer_money(self, User2, amount):
        self.account_balance -= amount 
        User2.account_balance += amount
        print(self.account_balance, User2.account_balance)


    


Mitch = User("Mitch", "mitch@mitch.mitch")
Mac = User("Mac", "mac@mac.mac")
Hailey = User("Hailey", "hailey@hailey.hailey")


Mitch.make_deposit(5000).make_deposit(500).make_deposit(600).make_withdrawl(1050)
print(Mitch.account_balance)

Mac.make_deposit(1000).make_deposit(2000).make_withdrawl(500).make_withdrawl(600)
print(Mac.account_balance)

Hailey.make_deposit(10000).make_withdrawl(300).make_withdrawl(500).make_withdrawl(6000)
print(Hailey.account_balance)

Mitch.transfer_money(Mac, 500)