bjp={1,2,3,4}
cong={3,4,6,5}
print(bjp.intersection(cong)) #REPEATABLE OBJECT
print(bjp.union(cong))  #SINGLE SET
s={i for i in range(10)}
print(s)
s2={3,5,6,8,9}
s3={3,5,6,8}
print(s3.difference(s2))
s2=frozenset(s2) # CONVERT INTO MUTABLE TO IMMUTABLE
s2.remove(9)
x=s2.discard(9) #NOTHING RETURN
print(x)
print(s2)