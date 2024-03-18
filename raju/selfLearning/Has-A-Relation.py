"""

By Composition (Has-A Relationship):
 By using Class Name or by creating object we can access members of one class inside another class is nothing but composition (Has-A Relationship).
  The main advantage of Has-A Relationship is Code Reusability.
"""
class one:
    oneClassVariable=20
    def __init__(self):
        self.val1=30
    def m1(self):
        return " Class one method test"
class two:
    def __init__(self):
        self.val2=one()
    def m2(self):
        print(" one class variable value",self.val2.oneClassVariable)
        print(" one class instance variable ",self.val2.val1)
        print(" one class instance method ",self.val2.m1())
        print(" Class two method invoked")


if __name__=='__main__':
    t1=two()
    t1.m2()
