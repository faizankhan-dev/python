#METHOD OVERRIDING

# class plane:
#     def show(self):
#         print("print")
# class heli(plane):
#     def show(self):
#         super().show()
#         print("heli")

# p=plane()
# p.show()
# h=heli()
# h.show()


class car:
    def show(self):
        print("car")
    def show(self):
        print("bike")

c=car()
c.show()