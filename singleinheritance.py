#THIS IS SINGLE LEVEL INHERITANCE

class car:
    def show(self):
        print("base")

class nano(car):
    def display(self):
        
        print("nano")

c=car()
n=nano()
c.show()
n.display()
n.show()
