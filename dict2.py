d={}
n=int(input("Enter the no. of data"))
for i in range(n):
    print(f"Enter the {i+1} data")
    k=input("Enter the keys")
    v=input("Enter the values")
    d[k]=v
print(d)
d1={100:"a",200:"b"}
d2={100:"hello",200:"bhopal",300:"faizan"}
d1.update(d2)
print(d1)
d1.pop(100)
print(d1)
d1.popitem()