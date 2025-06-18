# class emp:
#     def getdata(self):
#         self.a=int(input("Enter the no. a"))
#     def showdata(self):
#         print("the value of a is ",self.a)
# e=emp()
# e.getdata()
# e.showdata()

# class emp:
#     def getdata(self):
#         self.a1=int(input("Enter the no. a1 :"))
#         self.a2=int(input("Enter the no. a2 :"))

#     def addition(self):
#         self.a3=self.a1+self.a2
        
#     def showdata(self):
#         print("the value of a is ",self.a3)
# e=emp()
# e.getdata()
# e.addition()
# e.showdata()

class complex1:
    def getdata(self):
        self.a1=int(input("Enter the no. c1 real: "))
        self.a2=int(input("Enter the no. c1 imag: "))
        self.a3=int(input("Enter the no. c2 real : "))
        self.a4=int(input("Enter the no. c2 imag : "))

    def addition(self):
        self.a5=self.a1+self.a3
        self.a6=self.a2+self.a4
        
    def showdata(self):
        print("the value of a is ",self.a5, "+",self.a6,"i")
e=complex1()
e.getdata()
e.addition()
e.showdata()
         
    