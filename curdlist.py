# x=lambda a,b,c:a if a>b and a>c else (b if b>a and b>c else c)

# print(x(20,24,65))

name=["faizan","","berlin","","rio","","tokyo"]
def mydata(lst):
    if lst=="":
        return False
    else:
        return True
mylist=filter(mydata,name)
print(list(mylist))

x=filter(lambda x:False if x=="" else True,name)
print(list[x])  












