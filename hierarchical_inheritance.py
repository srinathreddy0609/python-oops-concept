class parent():
    num1=int(input("enter number 1 :"))
    num2=int(input("enter number 2 :"))

class child(parent):
    def add(self):
        print("addition is ",self.num1+self.num2)
    def sub(self):
        print("subraction is ",self.num1-self.num2)
    def mul(self):
        print("multiplication is ",self.num1*self.num2)

class child2(parent):
    def div(self):
        print("division is ",self.num1/self.num2)
    def rem(self):
        print("remainder is ",self.num1%self.num2)

obj1=child2()
obj1.div()
obj1.rem()
obj2=child()
obj2.add()
obj2.sub()
obj2.mul()




# class parent():
#     def fun1(self):
#         print("this is parent class")
# class child1(parent):
#     def fun2(self):
#         print("this is child1 class")
# class child2(parent):
#     def fun3(self):
#         print("this is child2 class")        
# obj=child2()
# obj.fun3()
# #bj.fun2()
# obj.fun1()
# #we need to create object for fun2
# obj1=child1()
# obj1.fun2()