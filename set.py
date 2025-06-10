s={1,23,4,5,6,7,8,8,8,8,8,}
print(type(s))
print(s)
s.add(23) # TO ADD SINGLE VALUE
print(s)
s.add("hello")
print(s)
s.remove(4)
print(s)
s2=s.copy()
s.clear()
print(s)
print(s2)
s2.update([5,6,7,8,69])  #TO ADD MULTIPLE VALUE
print(s2)

