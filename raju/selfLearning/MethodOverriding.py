class P:
    def property(self):
        print("Testing")
    def marry(self):
        print("Kalpana")
class C(P):
    def marry(self):
        print("Kushal")


if __name__=='__main__':
    c=C()
    c.property()
    c.marry()

