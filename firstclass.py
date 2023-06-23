# class is a blue print for creating an objects
# class does not take memory space
class Phone:
    def make_call(self):
        print("making call with other phone")
    def play_game(self):
        print("playing games")
    def set_color(self,color):
        self.color=color
    def show_color(self):
        print(self.color)
class miphone(Phone):
    name="redmi 4A"
    def make_call(self):
        print("making call with mi phone")

p1=miphone()
p1.make_call()
p1.play_game()
p1.set_color("blue")
p1.show_color()
p2=Phone()
p2.make_call()
print(p1.name)
