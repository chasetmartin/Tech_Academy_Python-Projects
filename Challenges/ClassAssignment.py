

class User:
    #define the attributes of the class User
    name = ''
    email = ''
    password = ''
    account = 0
    #using a dunder method to setup User initialization
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account
        
#Initializing an example user
New_user = User("John Doe", "Jdoe@gmail.com", "PassWORD", 12)
#printing the name of example user
print(New_user.name)

#Creatinga child of the user class called 'subscriber'
class Subscriber(User):
    address = ''
    email_list = True
    mail_list = True

#Creating 2nd child of the user class called 'employee'
class Employee(User):
    access_level = 1
    payroll = True
    pay = 16.00
    section = 'all'


    
