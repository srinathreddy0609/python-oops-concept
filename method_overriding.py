# same name and same parameters 
# use super_keywoard to get parent class methods

class A:
    def sum(self):
        a=8
        b=3
        print(a+b)

class B(A):
    def sum(self):
        a=3
        b=4
        super().sum()
        print(a+b)
        
        
 

obj=B()
obj.sum()
# obj2=A()
# obj2.sum()
# obj2.sub()