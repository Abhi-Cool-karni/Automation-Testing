# classes are user defined blueprint or prototype.
# sum, addition, constant, multiplication, subtraction
# methods, class variables, instance variables, constructors etc.
# Constructor is one method which is automatically called when you create object for any class.

# class Calculator:
#     num = 100  # class variables

#     # default constructor
#     def __init__(self):
#         print("I am called automatically when object is created")

#     def getData(self):
#         print("I am now executing as a method in class")


# obj = Calculator()  # syntax to create objects in python
# obj.getData()
# print(obj.num)
# obj1 = Calculator()
# obj1.getData()
# print(obj1.num)

# variables are two types class variables, instance variables
# Class variables: variables defined immediately inside the class are called class variables.
# Instance variables: Variables which will defined inside constructor is called instance variables.
# Class variables are constant irrespective of how many objects declared
# Instance variables are differs from each objects created.

# Self keyword is mandatory for calling variables names into method
# Instance and Class variables have whole different purpose
# Constructor name should be __init__

# Instance variables:


class Calculator:
    num = 100  # class variables

    # default constructor
    def __init__(self, a, b):
        self.firstnumber = a  # Instance variables
        self.secoundnumber = b  # Instance variables
        print("Constructor is called automatically when object is created")

    def getData(self):
        print("Function is now executing as a method in class")

    def summation(self):
        return self.firstnumber + self.secoundnumber + self.num


obj = Calculator(2, 3)
obj.getData()
print(obj.summation(), "From object ")

#  When object is created the object will be passed as first argument and will call as self in python standards
obj2 = Calculator(4, 5)
obj2.getData()
print(obj2.summation(), "From another object")
