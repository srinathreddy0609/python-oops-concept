class rohan:
    work1="HTML, CCS & JavaScript"
    def front(self):
        print("Front end task is implemented using ",self.work1)

class harry:
    work2="Oracle DB & Java"
    def back(self):
        print("Back end task is implemented using ",self.work2)

class teamlead(rohan,harry):
    def show(self):
        print("dynamic website created...")

t=teamlead()
t.front()
t.back()
t.show()

# class father():
#     def fun1(self):
#         print("this is father class")
# class mother():
#     def fun2(self):
#         print("this is mother class")
# class child(father,mother):
#     def fun3(self):
#         print("this is child class")        
# obj=child()
# obj.fun3()
# obj.fun2()
# obj.fun1()