#THIS IS SINGLE LEVEL INHERITANCE

# class car:
#     def show(self):
#         print("base")

# class nano(car):
#     def display(self):
#         
#         print("nano")

# c=car()
# n=nano()
# c.show()
# n.display()
# n.show()


#THIS IS MULTI LEVEL INHERITANCE
# class car:
#     def show(self):
#         print("base")

# class nano(car):
#     def display(self):
#         print("nano")

# class bike(nano):
#     def complex(self):
#         print("hello")

# c=car()
# n=nano()
# b=bike()
# c.show()
# n.show()
# n.display()
# b.complex()
# b.display()
# b.show()


#MULTIPLE INHERITANCE

# class car:
#     def show(self):
#         print("base")

# class nano:
#     def display(self):
#         print("nano")

# class nano1(car,nano):
#     def complex(self):
#         print("hello")
# c=car()
# n=nano()
# n1=nano1()
# n1.complex()
# n.display()
# c.show()


# HIRARICHAL INHERITANCE

# class car:
#     def show(self):
#         print("base")

# class nano1(car):
#     def display(self):
#         print("nano1")

# class nano2(car):
#     def complex(self):
#         print("nano2")

# class nano3(car):
#     def funct(self):
#         print("nano3")

# c=car()
# n1=nano1()
# n2=nano2()
# n3=nano3()
# c.show()
# n1.display()
# n1.show()
# n2.complex()
# n2.show()
# n3.funct()
# n3.show()


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