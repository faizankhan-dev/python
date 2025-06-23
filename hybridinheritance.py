

#HYBRID INHERITANCE

class car:
    def show(self):
        print("base")

class nano1(car):
    def display(self):
        print("nano1")

class nano2(car):
    def complex1(self):
        print("nano2")

class nano3(nano1,nano2):
    def complex2(self):
        print("nano3")

c=car()
n1=nano1()
n2=nano2()
n3=nano3()
c.show()
n1.display()
n1.show()
n2.complex1()
n2.show()
n3.complex2()
n3.complex1()
n3.display()
n3.show()