# multiple inheritance is when a child class inherits from more than one parent class  
# python uses MRO ( method resolution order) to determine wich method to call first 
# using super() makes a correct execution order, automatic MRO handling and cleaner code
# the code with super() :
print("with using super() : ")
class A :
    def show(self):
        print("i am from A")

class B(A):
    def show(self):
        super().show() #automatically calls A based on MRO
        print("i am from B")

class C(A):
    def show(self):
        super().show() #automatically calls A based on MRO
        print("i am from C")

class D(B,C):
    def show(self):
        super().show() #automatically follows MRO
        print("i am from D")

d = D()
d.show()
# A is called only once,the MRo determines the correct order automatically avoiding errors
   #############################################################################
# the code without super() makes duplicate execution, manual calls and harder maintenance :

print("without using super() : ")
class W:
    def show(self):
        print("i am from W")

class X(W):
    def show(self):
        W.show(self) #manually calling the parent class
        print("i am from X")

class Y(W):
    def show(self):
        W.show(self) #manually calling the parent class
        print("i am from y")

class Z(X,Y):
    def show(self):
        X.show(self) #calling X manually
        Y.show(self) #calling Y manually
        print("i am from Z")

z = Z()
z.show()

