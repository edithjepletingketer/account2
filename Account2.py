class Account: 
    def __init__(self,first_name,second_name,balance): 
        self.first_name=first_name
        self.second_name=second_name
        self.balance=balance
    
    def welcome(self):
        welcome="Hello {} {} welcome to Account, your balance is {}".format(self.first_name,self.second_name,self.balance)
        return welcome 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        return("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawed: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            return("\n You Withdrawed:", amount) 
        else: 
            return("\n Insufficient balance  ") 
  
    def show_balance(self): 
        return("\n Net Available Balance=",self.balance)