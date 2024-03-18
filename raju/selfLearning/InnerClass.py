import gc
class outer:
    def __init__(self):
        print(" outer class constructer")

    def __del__(self):
        print(" outer Clean up")

    class inner:
        def __init__(self):
            print("inner class constructor ")
        def inner_m1(self):
            print(" inner class instance method")

if __name__== '__main__':
    ou = outer()
    in1 = ou.inner()
    in1.inner_m1()
    print(gc.isenabled())


