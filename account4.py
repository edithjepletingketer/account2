from datetime import datetime




class Account:
    def __init__(self,first_name,second_name):
        self.first_name=first_name
        self.second_name=second_name
        self.balance=0.00
        self.loan=0.00
        self.deposits=[]
        self.withdrawal=[]


    def greetings(self):
            return"Hello {} {} welcome to the your banking account you balance is{}".format(self.first_name,self.second_name,self.balance)

    def deposit(self,amount):
        time = datetime.now()
        object={"time":time,"amount":amount}
        self.deposits.append(object)
        self.balance=self.balance+amount
        
        return("you have deposited {}".format(amount))


    def show_deposits(self):    
        

        for deposit in self.deposits:
            time=deposit["time"]
            formated_time=time.strftime("%c")
            amount=deposit["amount"]
            print("on {} you deposited {}".format(formated_time,amount))    

    def withdraw(self,amount):
        
        if amount < self.balance:
            time = datetime.now()
            object={"time":time,"amount":amount}
            self.withdrawal.append(object)
            self.balance=self.balance-amount
            

            return("Hello {} {} you have successfully withdrawn  {}".format(self.first_name,self.second_name,amount))
        else:
            return("Hello {} {} you have insufficient balance".format(self.first_name,self.second_name,amount)) 
    def show_withdrawal(self):    
        
        for withdraw in self.withdrawal:
            time=withdraw["time"]
            formated_time=time.strftime("%c")
            amount=withdraw["amount"]
            print("on {} you withdrawed {}".format(formated_time,amount))

    def show_balance(self): 
        balance=self.balance
        return("hello {} {} your balance is {}".format(self.first_name,self.second_name,self.balance))
    def give_loan(self,loan):
        if len(self.deposits)>=5:
            loan< 1/3* sum(self.deposits)
            formated_time=time.strftime
    def give_loan(self,amount):
        loan = amount
        total = 0
        for deposit in self.deposits:
           deposit = deposit["amount"]
           total+=deposit

        if len(self.deposits)>=5 and amount<total/3 and self.loan==0:
           self.loan = self.loan + amount
           print("Dear customer your loan of {} has been approved".format(amount))



    def repay_loan(self,amount):

       payment = amount

       self.loan.extend(amount)

       self.loan = self.loan-amount
       excess_payment = self.deposit.append(deposit)

       loanm = ("Dear customer you have paid kes {} your remaining loan balance is now {}".format(amount,self.loan))
       print(loanm)




    #def giveloan(self,amount):
        
        #if len(self.deposits)>=5 and amount<=1/3*sum(self.deposits) and self.loan==0:
            #self.loan=self.loan+amount
            #return("Hello {} the loan of {} is successful".format(self.first_name,amount))
        #else:
            #return("hello {}, your loan limit is unsuccessful".format(self.first_name))
    #def pay_loan(self,amount):
        #if self.loan==0:
            #print("you have an existing loan")
        #elif amount<self.loan:
            #self.loan=self.loan-amount
            #print("Hello {} {} you have paid sh{} your remaining amount is {}".format(self.first_name,self.second_name,amount,self.loan))
        #elif amount==self.loan:  
            #self.loan=self.loan-amount
            #print("You have fully paid your loan") 
        #elif amount>self.loan:
            #excess=amount-self.loan
            #self.balance=excess+self.balance
            #self.loan=amount-self.loan-excess
            #print("Hello {} congratulations you have finished paying your loan and remained with a balance of {}".format(self.first_name,self.balance))               