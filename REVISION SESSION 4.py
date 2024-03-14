# This file contains all the files created during the revision session of OOPS - python.

"""
    Topics are:
    1. Concept of 'self'
    2. example of fraction class
    3. dunder methods - __str__ , __add__ , __sub__ , __mul__ , __truediv__

"""

#   TOPIC 1 : CONCEPT OF 'SELF'
class Student:

    def __init__(self):
        self.name = ''
        self.RollNo = 0
        self.age = 0
        self.Year = 0
        self.menu()

    
    def menu(self):
        user_input = input("""
            Welcome Student, How can i help you?
            1. To Enter your details please press 1.
            2. To know your details please press 2
            3. To change your details please press 3
            4. To exit , press anything other then the above keys
    """)
        
        if user_input == "1":
            self.create_profile()
        elif user_input == '2':
            self.user_details()
        elif user_input == '3':
            self.change()
        elif user_input == '4':
            pass
    

    def create_profile(self):
        user_name = input("Enter your name")
        user_RollNo = int(input("Enter your roll no"))
        user_age = int(input("Enter your age"))
        user_Year = int(input("Enter your current academic year"))

        self.name = user_name
        self.age = user_age
        self.RollNo = user_RollNo
        self.Year = user_Year


        self.menu()

    
    def user_details(self):

        roll1 = int(input("To see your details enter your roll no "))

        if self.RollNo == roll1:
            print(self.name,self.RollNo,self.age,self.Year)
        else:
            print("Record not found")

        self.menu()

# s1 = Student()

"""
    THE GOLDEN RULE OF OBJECT ORIENTED PROGRAMMING
    ->  The class data members and data methods are only accessible by the class objects.

    There are two things in OOPS , class and object.
    Inside class, there are all the rules and objects follow those rules.
    In rules , we make two things .
        1. we create attributes. like pin in ATM class.
        2. Else we add methods like menu , check balance or withdraw.
"""

# Q1 - FRACTION CLASS
#   numerator , denominator fk

class Fraction:

    # parameterised constructor
    def __init__(self,x,y):
        self.den = y
        self.num = x

    def __str__(self):
        #   The code below is string formatting
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(salman,shahrukh):
        new_num = salman.num*shahrukh.den + salman.den*shahrukh.num
        new_den = salman.den*shahrukh.den

        return '{}/{}'.format(new_num,new_den)

f1 = Fraction(3,4)
print(f1)

f2 = Fraction(3,4)
print(f2)

print(f1+f2)


#   TOPIC 3 : DUNDER METHODS - __add__ (+), __sub__ (-), __mul__ (*), __truediv__ (/)