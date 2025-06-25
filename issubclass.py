#SUBCLASS

# class C1:
#     def summation(self,a,b):
#         return a+b;
# class C2:
#     def multiplication(self,a,b):
#         return a*b;
# class D1(C1,C2):
#     def divide(self,a,b):
#         return a/b;
# d=D1()
# print(issubclass(D1,C2))
# print(issubclass(D1,C1))
# print(issubclass(C1,C2))
# print(issubclass(C2,D1))


#ININSTANCE

class C1:
    pass
    
class C2:
    pass
   
class D1(C1):
    pass
   
d=D1()
print(isinstance(d,C1))
print(isinstance(d,C2))
print(isinstance(d,D1))