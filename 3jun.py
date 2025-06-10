try:
    age=int(input("Enter your age:"))
    if(age<=0):
        raise ValueError
    elif(age<=18):
        print("not valid for vote")
    
    else:
        print("valid for vote")
except ValueError:
    print("value not valid",ValueError)