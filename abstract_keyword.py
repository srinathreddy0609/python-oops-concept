from abc import ABC,abstractmethod

class car(ABC):
    def show(self):
        print("every car has 4 wheels")
    #@abstractmethod
    def speed(self):
        print("car catogery")


class car1(car):
    def speed(self):
        print("this is car 1 ")

class car2(car):               #class car2(car1):
    def speed(self):
        print("this is car 2")
        #super().speed()


obj1=car2()
obj1.show()
obj1.speed()

obj2=car1()
obj2.show()
obj2.speed()

obj3=car()
obj3.speed()
