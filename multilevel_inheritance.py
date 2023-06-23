class parent():
    num1=int(input("enter number 1 :"))
    num2=int(input("enter number 2 :"))
    def add(self):
        print("addition is ",self.num1+self.num2)
    def sub(self):
        print("subraction is ",self.num1-self.num2)

class child(parent):
    def mul(self):
        print("multiplication is ",self.num1*self.num2)
    def div(self):
        print("division is ",self.num1/self.num2)

class child2(child):
    def rem(self):
        print("remainder is ",self.num1%self.num2)

obj=child2()
obj.add()
obj.sub()
obj.mul()
obj.div()
obj.rem()

















# class parent():
#     def fun1(self):
#         print("this is parent class")
# class child(parent):
#     def fun2(self):
#         print("this is child class")
# class grandchild(child):
#     def fun3(self):
#         print("this is grandchild class")        
# obj=grandchild()
# obj.fun3()
# obj.fun2()
# obj.fun1()
