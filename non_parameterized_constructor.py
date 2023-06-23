class A:
    def __init__(self):
        self.a=62
        self.b=53
    def show(self):
        # print("value of b is: ",self.a)
        # print("value of a is: ",self.b)
        #if you want to use constructor variable in other methods it should be instance variable so use self
        print("sum of a and b is ",self.a+self.b)
obj=A()
obj.show()
