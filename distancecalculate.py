class distance:
    def getdata(self):
        print("ENTER FIRST DISTANCE :")
        self.km1=int(input("Enter the kilmometer1: "))
        self.m1=int(input("Enter the meter1 "))
        self.cm1=int(input("Enter the centimerter1 : "))

        print("ENTER SECOND DISTANCE :")

        self.km2=int(input("Enter the kilmometer2: "))
        self.m2=int(input("Enter the meter2 "))
        self.cm2=int(input("Enter the centimerter2 : "))
        

    def addition(self):
        
        self.a1=self.km1+self.km2
        self.a2=self.m1+self.m2
        self.a3=self.cm1+self.cm2

        if(self.a3>100):
            self.a2=self.a2+1
            self.a3=self.a3-100
        if(self.a2>100):
            self.a1=self.a1+1
            self.a2=self.a2-1000
        
    def showdata(self):
        print("TOTAL DISTANCE  IS ",self.a1 , "km", self.a2, "m" ,self.a3,"cm")
e=distance()
e.getdata()
e.addition()
e.showdata()