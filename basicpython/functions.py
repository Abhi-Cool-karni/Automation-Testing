# Function is a group of of related statements that perform a specific task.
# function declaration

def greetme(name):
    print("Good Afternoon "+name)


# function call
# Parameterized function
# greet with name

greetme("Abhishek Kulkarni")  # Good Afternoon Abhishek Kulkarni


def addIntegers(a, b):
    print(a+b)


addIntegers(2, 3)  # 5


def addIntegers(a, b):
    return(a+b)


print(addIntegers(2, 3), "With return")  # 5