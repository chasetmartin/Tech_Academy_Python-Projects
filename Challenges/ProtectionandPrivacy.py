
#creating a class to demonstrate protection
class Protect:
    def __init__(self):
        #creating a protected variable, basically a warning to other developers
        self._x = 24

test = Protect()
print(test._x)

#changing the protected variable from outside of the class/method
test._x = 30
print(test._x)

#creating a class to demonstrate privacy
class Privacy:
    def __init__(self):
        #creating a private variable
        self.__y = 44
        #let's also create a protected variable within the same class
        self._z = 20
        #defining a method to print the private variable to the console
    def printy(self):
        print(self.__y)

test2 = Privacy()
# print(test2.__y)
#The print statement above will raise an attribute error because the variable is private. I have to call the method from within the private variable's class:
test2.printy()

#since the z variable is only protected I should be able to call it outside of the class to print to the console:
print(test2._z)



