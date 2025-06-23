#MULTIPLE INHERITANCE

class car:
    def show(self):
        print("base")

class nano:
    def display(self):
        print("nano")

class nano1(car,nano):
    def complex(self):
        print("hello")
c=car()
n=nano()
n1=nano1()
n1.complex()
n.display()
c.show()