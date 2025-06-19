
# class car:
#     def __init__(self,modelname,year):
#      self.modelname=modelname
#      self.__year=year #THIS IS PRIVATE DATA. PRIVATE DATA ONLY USED INSIDE THE CLASS.
#     def display(self):
#            print( self.modelname,self.__year)

# e=car("Toyota",2016)

# e.display()
# print(e.modelname)


class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"Destroyed")

pt1=point()
pt2=pt1
pt3=pt1
print(id(pt1),id(pt2),id(pt3)) #Prints the ids of the object

del pt1
# del pt2
# del pt3
     
     