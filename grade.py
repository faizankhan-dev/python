# a=int(input("Enter the 1st value\n\t"))
# b=int(input("Enter the 2nd value\n\t"))
# c=int(input("Enter the 3rd value\n\t"))

# if(a>b):
#     if(a>c):
#         print("a is max ",a)

# elif  (b>a):
#     if(b>c):
#         print("b is max ",b)    

#     else:
#         print("c is max ",c)

p=float(input("Enter the physics marks\n"))
c=float(input("Enter the chemistry marks\n"))
m=float(input("Enter the maths marks\n"))

total_marks=p+c+m
per=total_marks/3

if(p<0 or c<0 or m<0 or p>100 or c>100 or m>100):
    print("Invalid marks")
elif(p<33 and c>=33 and m>=33) or (p>=33 and c<33 and m>=33) or (p>=33 and c>=33 and m<33):
    if(p<33 and c>=33 and m>=33):
        print("you are fail in physics")
        print(f"phy={p},che={c},math={m}")
        print(f"total={total_marks}")
        print(f"per={per}")
    elif(p>=33 and c<33 and m>=33):
          print("you are fail in chemistry")
          print(f"phy={p},che={c},math={m}")
          print(f"total={total_marks}")
          print(f"per={per}")
    else:
         print("you are fail in maths")
         print(f"phy={p},che={c},math={m}")
         print(f"total={total_marks}")
         print(f"percentagr={per}")

elif(p<33 and c<33 and m>=33) or (p>=33 and c<33 and m<33) or (p<33 and c>=33 and m<33):
     if(p<33 and c<33 and m>=33):
          print("fail in phy and chem")
          print(f"phy={p},che={c},math={m}")
          print(f"total={total_marks}")
          print(f"per={per}")
     elif(p>=33 and c<33 and m<33):
         print("you are chemistry and maths")
         print(f"phy={p},che={c},math={m}")
         print(f"total={total_marks}")
         print(f"percentagr={per}")
     else:
         print("you are physics and maths")
         print(f"phy={p},che={c},math={m}")
         print(f"total={total_marks}")
         print(f"percentagr={per}")
elif(p<33 and c<33 and m<33):   
         print("you are fail in all subject")
         print(f"phy={p},che={c},math={m}")
         print(f"total={total_marks}")
         print(f"percentagr={per}")     

else:
     if(per<=45):
         print("3rd division")  
         print(f"phy={p},che={c},math={m}")
         print(f"total={total_marks}")
         print(f"percentagr={per}")     
     elif(per<60):
         print("2nd division")  
         print(f"phy={p},che={c},math={m}")
         print(f"total={total_marks}")
         print(f"percentagr={per}")     
     else:
         print("1st division")  
         print(f"phy={p},che={c},math={m}")
         print(f"total={total_marks}")
         print(f"percentagr={per}")  
          