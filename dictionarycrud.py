d={}
while(True):
    print(
        '''
        press 1 for create:
        press 2 for read:
        press 3 for update:
        press 4 for delete:
        press 5 for exit:
        '''
    )
    ch=int(input("Enter your choice:"))
    print("add data to the dictionary")
    if(ch==1):
        n=int(input("enter the data:"))
        for i in range(n):
            print(f"enter the {i+1} data:")
            k=input("enter the keys:")
            v=input("enter the values:")
            d[k]=v

    elif(ch==2):
        print("Data are there ")
        print(d)

    elif(ch==3):
        print("update your dictionary")
        print("update data to the dictionary")
        n=int(input("enter the data:"))
        for i in range(n):
            print(f"enter the {i+1} data:")
            k=input("enter the keys:")
            v=input("enter the values:")
            for j in d.keys():
             if(j==k):
              d[k]=v
       
    elif(ch==4):
            
        print("delete your dictionary")
        print("delete data to the dictionary")
        n=int(input("enter the data:"))
        for i in range(n):
            print(f"enter the {i+1} data:")
            k=input("enter the keys:")
            for j in d.keys():
             if(j==k):
              d.pop(k)
   
    elif(ch==5):
        print("press 5 ")
        break;
    else:
        print("wrong choice")
        continue