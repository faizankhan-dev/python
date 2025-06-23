
# HIRARICHAL INHERITANCE

class car:
    def show(self):
        print("base")

class nano1(car):
    def display(self):
        print("nano1")

class nano2(car):
    def complex(self):
        print("nano2")

class nano3(car):
    def funct(self):
        print("nano3")

c=car()
n1=nano1()
n2=nano2()
n3=nano3()
c.show()
n1.display()
n1.show()
n2.complex()
n2.show()
n3.funct()
n3.show()