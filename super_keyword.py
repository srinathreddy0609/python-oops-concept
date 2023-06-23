class A:
    def sum(self):
        a=8
        b=3
        print("this is claass A and sum is:")
        print(a+b)
        

    def sub(self):
        a=8
        b=3
        print("this is claass A and sub is:")
        print(a-b)
        


class B(A):
    def sum(self):
        a=3
        b=4
        print("this is class b")
        print(a+b)
        
        super().sum()
        super().sub()      # if we need to access the super class 

# Here both class has same function called "sum" we create an object for class B 
# But what if we want class A properties, we need to create an object for class A
# Instead of creating object to class A we use SUPER KEYWORD

obj=B()
obj.sum()
# obj2=A()
# obj2.sum()
# obj2.sub()


