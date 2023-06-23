# Polymorphism : multiple forms or many forms OR same function name but different parameters

# types :
# 1) compile time or early binding or  static poly:
# a)method overloading : same function name but different parameters
# 2)run time:
# a)method overriding : same class name





class A:
    def sum(self,x,y):
        print(x+y)

    def sum(self,a,b,c=0):
        print(a-b+c)

    #def sum(self,a=None,b=None,c=None):
        #print(a+b+c)
ob=A()
#ob.sum('sri','nath', '  reddy')
ob.sum(5,3,1)