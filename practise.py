# name = input("Enter name:")
# age = int(input("Enter age:"))
# location = input("Enter location:")
# print("hello there my name is",name,"am",age,"of age and i stay at",location)


# input_string = input('Enter elements of a list separated by space ')
# user_list = input_string.split()
# for i in range(len(user_list)):
#     user_list[i] = int(user_list[i])
# print("Sum = ", sum(user_list))

# x = (input('some text : '))
# x = {a for a in x.split(",")}
# print(x)


# number = input("Enter 1st set")#takes input from users
# number2 = input("Enter 2nd set")

# number = {a for a in number.split()} #converts the input into a set and sets the slipt function
# number2 = {b for b in number2.split()}
# print(number)
# print(number2) 

# print(number.intersection(number2))

# words=["table","food","bus","airplane","school","queen"]
# output=[word for word in words if len(word)%2==1]
# print(output)

#words=["table","food","bus","airplane","school","queen"]
# for word in words: 
# print(len(word[0:]))#print length number of each element


# Write a function called convert_add that takes a list of strings as an 
# argument and converts it to integers and sums the list. For example 
# [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.

# def convert_add():
#     numbers = ["1","2","3","4","5"]
#     output =[]
#     for i in numbers:
#         output.append(int(i))
#     print(numbers)
#     print(output)
#     print(sum(output))
# convert_add()

#creating a function that calculates the area of a triangle.
# def area_of_triangle():
#     base = 12
#     height = 7
#     area = 0.5*base*height
#     print(area)
# area_of_triangle()


#methods
# class person:
#     def person_details(self):
#         name = "Loveness"
#         Nationality = "SA"
#         print (f"Hello there my name is{name} and am from{Nationality}")
# P1=person()#create an object
# (P1.person_details())

#  Write a Python class BankAccount with attributes like account_number, 
#   balance, date_of_opening and customer_name, 
#  and methods like deposit, withdraw, and check_balance,customer_details.
#one should be able to check balance,withdraw and  deposit.

class BankAccount:
    #initializing a constructor with attributes
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    #create method deposit
    def deposit(self,amount):
        # self.balance = self.balance + amount
        self.balance += amount
        print(f"{amount} has been deposited on your account")
    #method withdraw
    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Insufficient funds your current balance is{self.balance}")
        else:
            # self.balance = self.balance - amount
            self.balance -= amount
            print(f"withdrawal succeful you have withdrawn {amount} you current balance is {self.balance}")
    #method checkbalance
    def checkbalance(self):
        print(f"current balance is {self.balance}")
    #method customer details
    def customer_details(self):
        print(f"Name:{self.customer_name}")
        print(f"Accountnumber:{self.account_number}")
        print(f"Date of Opening:{self.date_of_opening}")
        print(f"Balance:{self.balance}")
#inputing customer details
customer1=BankAccount()
customer2=BankAccount()
customer3=BankAccount()
customer4=BankAccount()
#calling the methods customer details
customer1.customer_details()
# customer2.customer_details()
#checkbalance
# customer3.checkbalance()
#withdrawing
# customer4.withdraw(30000)
# customer4.withdraw(20000)











 
    
