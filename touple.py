tp=('a','b','c','d','e')
print(type(tp))
print(tp[0])

print(tp)
tp1=list(tp)
print(tp1)
tp1.append(12)
tp=tuple(tp1)
print(tp)




ls=[i*3 for i in range(1,11)]
print(ls)