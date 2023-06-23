#same function name but different parameters

class a():
    def sum(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)

    def sub(self,a,b):

        self.a=a
        self.b=b
        print(self.a-self.b)

class b(a):
    def sum(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(self.a+self.b+self.c)

    def sub(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(self.a-self.b-self.c)

o=b()
o.sum(10,20,30)
o.sub(40,4,4)
# o1=a()
# o1.sum(10,2)
# o1.sub(40,4)