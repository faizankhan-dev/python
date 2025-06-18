# class emp:
#     def getdata(self,a,b):
#      self.t=a
#      self.r=b
#     def showdata(self):
#            print("the value of a is : ", self.t,self.r)

# e=emp()
# e.getdata(12,13)
# e.showdata()


# CONSTRUCTOR 

class emp:
    def __init__(self,a,b):
     self.t=a
     self.r=b
    def showdata(self):
           print("the value of a is : ", self.t,self.r)

e=emp(12,13)

e.showdata()
     
  