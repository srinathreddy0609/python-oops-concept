class student:
    num1=int(input("enter number 1  "))
    num2=int(input("enter number 2  "))

    def sum(self):
        print("addition",self.num1+self.num2)
    def sub(self):

        print("subtraction",self.num1-self.num2)

class a(student):
    def mul(self):
        print("multiplication",self.num1*self.num2)
    def div(self):
        print("division",self.num1/self.num2)

obj=a()
obj.mul()
obj.sub()