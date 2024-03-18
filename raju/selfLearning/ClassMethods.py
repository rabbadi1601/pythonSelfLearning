"""
Class Methods:
⚽Inside method implementation if we are using only class variables (static variables), then such type of methods we should declare as class method.
⚽ We can declare class method explicitly by using @classmethod decorator.
⚽ For class method we should provide cls variable at the time of declaration
⚽ We can call classmethod by using classname or object reference variable.
"""

class Animal:
    value1=30
    @classmethod
    def method1(cls,name):
        print("{} name variable and class variable value :{}".format(name,cls.value1))

    @staticmethod
    def add(x, y):
        print('The Sum:', x + y)

Animal.method1("Dog")
Animal.method1("Cat")
Animal.add(4,5)