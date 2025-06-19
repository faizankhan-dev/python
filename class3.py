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

# class emp:
#     def __init__(self,a,b):
#      self.t=a
#      self.r=b
#     def showdata(self):
#            print("the value of a is : ", self.t,self.r)

# e=emp(12,13)

# e.showdata()


class car:
    def __init__(self,modelname,year):
     self.modelname=modelname
     self.year=year
    def display(self):
           print( self.modelname,self.year)

e=car("Toyota",2016)

e.display()
     
     
  