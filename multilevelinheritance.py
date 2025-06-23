#THIS IS MULTI LEVEL INHERITANCE
class car:
    def show(self):
        print("base")

class nano(car):
    def display(self):
        print("nano")

class bike(nano):
    def complex(self):
        print("hello")

c=car()
n=nano()
b=bike()
c.show()
n.show()
n.display()
b.complex()
b.display()
b.show()