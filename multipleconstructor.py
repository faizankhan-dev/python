# class car:
#     def __init__(self):
#         print("this is car")
#     def __init__(self):
#         print("this is  not car")
#     def __init__(self):
#         print("this is my car")
    
# c=car()


# class car:
#     def __init__(self):
#         print("car")
# class maruti(car):
#     def __init__(self):
#         super().__init__()
#         print("maruti")

# m=maruti()



class car:
    def __init__(self):
        print("car")

class truck:
    def __init__(self):
        print("truck")
class maruti(car,truck):
    def __init__(self):
        super().__init__()
        print("maruti")

m=maruti()
    
    