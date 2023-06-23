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

obj=child()
obj.add()
obj.sub()
obj.mul()
obj.div()