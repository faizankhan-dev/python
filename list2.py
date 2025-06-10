l1=list()
print(type(l1))
l1.append(12)
l1.append([12,13,14,15])
print(l1[1][1])
l2=[]
n=int(input("enter the no. of data:"))
for i in range(n):
    print("enter the ",i+1," data")
    data=input("enter the data")
    l2.append(data)
print(l2)


# WAP to show the vowel and consonent in seperate list input taken from user
# v=[]
# c=[]
# n=int(input("enter the no. of character:"))
# for i in range(n):
#      print("enter the ",i+1,"character")
#      data=input("enter the character")
#      data1=data.lower()
#      if(data1=='a' or data1=='e'or data1=='i'or data1=='o' or data1=='u'):
#           v.append(data1)
#      else:
#           c.append(data1)
# print("vowel",v)
# print("consonent",c)

# l1=[]
# l1.extend((12,34,56,78,90) )
# print(l1)

# l1=[12,34,56,78,90]
# x=max(l1)
# print(x)
# y=min(l1)
# print(y)
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.remove(56)
# print(l1)
# z=l1.pop()
# print(z)
# l1.pop()
# print(l1)
# l1.insert(0,75)
# print(l1)
# i=l1.index(34)
# print(i)




