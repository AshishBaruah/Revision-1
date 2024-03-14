# class Rectangle:
#     def __init__(self,x,y):
#         self.len = x
#         self.bre = y

    
#     def perimeter(self):
#         return self.len+self.bre

#     def area(self):
#         return self.len * self.bre

#     def display(self):
#         print("The length of the rectangle is: ",self.len) 
#         print("The breadth of the rectangle is: ",self.bre) 
#         print("The perimeter of the rectangle is: ",self.perimeter()) 
#         print("The area of the rectangle is: ",self.area()) 



# R1 = Rectangle(10,20)
# R1.display()


class Bank:
    def __init__(self):
        self.accountNumber = 0
        self.name = ''
        self.balance = 0
    
    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self,amt1):
        self.balance += amt1

    def withdraw(self,amt2):
        self.balance -= amt2

    def bankfees(self):
        pass

    def display(self):
        
        print("AccountNumber: ",self.accountNumber)
        print("Name of Customer: ",self.name)
        print("Balance Avaiable: ",self.balance)


"""
BankAccount(121241124,"asdfas",4500)
withdraw(700)
deposit(1000)
display()
"""
acc1 = Bank(2178514584, "Mandy" , 2800)
acc1.display()

print("-------------------------------")
acc1.deposit(1000)
acc1.withdraw(700)
acc1.display()