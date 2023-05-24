# Hybrid Inheritance -> combination of one or more types of inheritance

class A:
    def __init__(self, a):
        self.a = a
    
    def display(self):
        print("A:", self.a)

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b
    
    def display(self):
        A.display(self)
        print("B:", self.b)

class C(A):
    def __init__(self, a, c):
        A.__init__(self, a)
        self.c = c
    
    def display(self):
        A.display(self)
        print("C:", self.c)

class D(B, C):
    def __init__(self, a, b, c, d):
        B.__init__(self, a, b)
        C.__init__(self, a, c)
        self.d = d
    
    def display(self):
        B.display(self)
        C.display(self)
        print("D:", self.d)

d = D(1, 2, 3, 4)
d.display()