

class User:
    #define the attributes of the class User
    name = ''
    email = ''
    password = ''
    account = 0
    #using a dunder method to setup User initialization
    def __init__(self, name, email, password, account):
        self.name = name.lower()
        self.email = email.lower()
        self.password = password
        self.account = account
    #creating a login info method for the user
    def loginInfo(self):
        entry_name = input("Please enter your name: ").lower()
        entry_email = input("Enter your email here: ").lower()
        entry_password = input("Your password?: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is not correct.")

#Creatinga child of the user class called 'subscriber'
class Subscriber(User):
    address = ''
    email_list = True
    mail_list = True
    #using the same loginInfo method as user, but with specifics for a subscriber (polymorphism)
    def loginInfo(self):
        entry_name = input("Please enter your name: ").lower()
        entry_email = input("Enter your email here: ").lower()
        entry_password = input("Your password?: ")
        #Here is the new overriding behavior of the child class:
        entry_subscription = input("Would you like to continue subscribing? (Y/N): ").lower()
        if (entry_email == self.email and entry_password == self.password) and entry_subscription == 'y':
            print("Welcome back, {}, and thanks for subscribing!".format(entry_name))
        elif (entry_email == self.email and entry_password == self.password) and entry_subscription == 'n':
            print("Welcome back, {}, we will remove you from the subscriber list".format(entry_name))
        else:
            print("The password or email is not correct.")
            
#Creating 2nd child of the user class called 'employee'
class Employee(User):
    access_level = 1
    payroll = True
    pay = 16.00
    section = 'all'
    secret_code = '12456'
    #using the same loginInfo method as user, but with specifics for a Employee (polymorphism)
    def loginInfo(self):
        entry_name = input("Please enter your name, employee: ").lower()
        entry_email = input("Enter your company email here: ").lower()
        entry_password = input("Your employee password?: ")
        entry_code= input("Enter the secret employee code: ")
        if (entry_email == self.email and entry_password == self.password and entry_code == self.secret_code):
            print("Welcome back, {}, don't forget to fill out your time card!".format(entry_name))
        else:
            print("The password or email or code is not correct.")



if __name__ == "__main__":
    #instantiating a new object from the Employee class:
    New_employee = Employee("Chase Martin", "chase@rocketmail.com", "pword", 1)
    #calling the loginInfo method from the employee class:
    New_employee.loginInfo()
