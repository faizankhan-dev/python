class complex:
 
    def __init__(self,real1,imag1,real2,imag2):
        self.real1=real1
        self.imag1=imag1
        self.real2=real2
        self.imag2=imag2
    
    def adddisplay(self):
        print("addtion of number =",(self.real1+self.real2) ,"+",(self.imag1+self.imag2),"i")
a=int(input("enter real1"))
b=int(input("enter imag1"))
c=int(input("enter real2"))
d=int(input("enter imag2"))

c1=complex(a,b,c,d)
c1.adddisplay()