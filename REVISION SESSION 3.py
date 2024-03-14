#   THIS FILE CONTAINS OOPS REVISION MATERIALS

#   OOPS - OBJECT ORIENTED PROGRAMMING

# GENERALITY TO SPECIFICITY

# OOPS PRINCIPLES
# Class and objects
# Polymorphism
# Abstraction
# Inheritance
# Encapsulation
 
# class is a blueprint


# L = [1,2,3]
# print(type(L))


# class has 2 things in it
# class -> 1.Data or property or attribute
# class -> 2.functions or behaviour


"""
Example - lets say we have a class named DBMS - 1
Data of the above class can be syllabus , courseinstructor , monthstocomplete , classtiming

example 2 - class name is car
data -> color , topspeed , mileage , enginespecs
behaviour -> calculate average speed


Example 

class car:
    color = "blue"
    model = "sports


    def calculate_avg_speed(km,time):
        #some code


Object is an instance of class


example : car->wagonr , sports-> football , animals -> tiger
"""
#-------------------------------------------------------------
"""
syntax to create a object
objectname = classname()


  Example - ATM Machine
  Data - atmpin , balance

class name is always written in pascal case
example - HelloWorld , MyAtm

"""
#--------------------------------------------------------------
"""
(v.v.imp) 1. In python , whenever we need to create variables inside class , we create it inside constructor and we need to use self keyword. 
2. In python , the functions created inside the class are not class functions , they are called methods.

"""
class ATM:
    
    # constructor - basically a function inside the class
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    
    def menu(self):
        user_input = input("""
            Hello , How can i help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Anything else to exit 
        """)

        if user_input == '1':
            # call create pin function
            self.create_pin()
        elif user_input == '2':
            # call change pin function
            self.change_pin()
        elif user_input == '3':
            # call check balance function
            self.check_bal()
        elif user_input == '4':
            # call withdraw function
            self.withdraw()
        else:
            # EXIT
            pass

    def create_pin(self):
        user_pin = input("Enter the pin you want ")
        self.pin = user_pin

        user_bal = input("Enter your balance ")
        self.balance = user_bal

        print("Dear User, Pin has been created successfully ")
        self.menu()

    def change_pin(self):

        pin1 = input("Enter your old pin ")

        if pin1 == self.pin:
            new_pin = input("Dear user, Please enter the new pin ")
            self.pin = new_pin
            print("Pin changed successfully")
            self.menu()
        else:
            print("Please enter the correct old pin")
            self.menu()

    def check_bal(self):
        
        ent_pin = input("Enter your pin ")
        if ent_pin == self.pin:
            print("The available balance is " + self.balance)
            self.menu()
        else:
            print("Dear user, enter the correct pin")
            self.menu()
    
    def withdraw(self):

        pin1 = input("Dear user, please enter your pin")

        if pin1 == self.pin:
            withdraw_amt = input("Enter the amount you want to withdraw")
            self.balance = self.balance - withdraw_amt
            print("Dear user, the available balance is " + self.balance)
        else:
            print("Please enter the correct pin!!!")
            self.menu()

# obj1 = ATM()
# print(type(obj1))

### MAGIC METHODS ( AKA DUNDER METHODS)

"""
    Magic methods are special types of methods
    Everytime it looks like this:

        __name__

    Constructors are magic(dunder) methods too.
    ->      __init__

    The main difference between normal methods and dunder(magic) methods is that we dont need to call dunder methods.
    The code inside dunder methods are automatically called whenever a object of the class is created.
    Using these dunder methods we can create our own data types.


Constructor is a special method used for initializing objects of a class.
The constructor is typically named as `__init__() `
We cannot change the name of constructor.

class Sample:
    def __init__(self,a,b):
        self.a = a
        self.b = b


obj2 = Sample(1,2);

print(obj2.a)
print(obj2.b)


Big Question
Why are constructors needs to be a special function?
why can't it be like the normal methods?

As we know , constructors helps us initialize the objects of a class.So we want some control what the users need to create.

we use constructors for writing configuration codes.

V.V.Imp philosophical example.

If god is the programmer , earth is the class , then what is inside the constructor code assuming we human beings are the objects. 

Then inside constructor , there will be things which god doesnot want human beings to have control.

Answer to the above philosophy is death.(Death will be inside the constructor)

"""
