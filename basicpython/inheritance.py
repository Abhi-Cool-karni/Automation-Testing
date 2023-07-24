# Inheritance is acquiring properties of parent class

from oops import Calculator


class childImplementation(Calculator):
    num1 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getcompleteData(self):
        return self.num1 + self.num + self.summation()


obj1 = childImplementation()
print(obj1.getcompleteData())
