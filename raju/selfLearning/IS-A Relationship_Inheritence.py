"""
By Inheritance (IS-A Relationship):
What ever variables, methods and constructors available in the parent class by default available to the child classes and we are not required to rewrite.
Hence the main advantage of inheritance is Code Reusability and we can extend existing functionality with some more extra functionality.
"""

class one():
    def m1(self):
        print("Parent method")
class two(one):
    def m2(self):
        print("child method")

class Raju():
    a=10
    def __init__(self):
        self.b=20
    def method1(self):
        print(" Inside Raju class")

class kushal(Raju):
    c1=30

    def __init__(self):
        super().__init__()
        self.d1=50

    def method2(self):
        print("a :",self.a)
        print("b ",self.b)
        self.method1()

if __name__=='__main__':
    t2=two()
    t2.m2()
    t2.m1()
    t3=kushal()
    t3.method2()
    print(t3.a ,t3.b,t3.c1,t3.d1)