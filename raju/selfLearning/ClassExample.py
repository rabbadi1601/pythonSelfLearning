class Student:
    classVariable=10
    def __init__(self,*args):
        if len(args)==0:
           self.name="Raju"
           self.lastname="Abbadi"
           self.age=44
        else:
            self.name = args[0]
            self.lastname = args[1]
            self.age = args[2]

    def display(self):
        print("Name:" ,self.name)
        print("LastName : ",self.lastname)
        print("age :",self.age)
    def v1():
        print("ssssss")
'''

s1=Student()
s1.display()
s2=Student("Kushal","abbadi",11)
s2.display()
print(s2.classVariable)
print(s2.name)
'''
Student.v1()