class a:
    _a=10    #protected
    __b=20   #private
    def show(self):
        print("value of a is ",self._a)
        print("value of b is ",self.__b)

o=a()
o.show()
print("outside of class ",a._a)
#print("outside of class ",a.__b) gives error because of protected