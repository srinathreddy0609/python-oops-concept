class family:
    sure_name="reddy"  #class variable
    
    def __init__(self,name,age,address):

        print(name,self.sure_name,age,address)
    def show(self):
        print("surename is : ",self.sure_name)  #using class variable with help of self

obj=family("srinath",23,None)  # None used if we dont want to give a value 
obj.show()

        