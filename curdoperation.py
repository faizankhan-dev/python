ls=[]
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
    if(ch==1):
        n=int(input("enter the data:"))
        for i in range(n):
            print(f"Enter the {i+1} data :")
            data=(input("enter the data:"))
            ls.update(data)

    elif(ch==2):
        print("Data are there ")
        print(ls)
    elif(ch==3):
        n=int(input("enter the data:"))
        for i in range(n):
            print(f"Enter the {i+1} data :")
            data=(input("enter the data to update:"))
            x=ls.index(data)
            data1=(input("enter the updated data:"))
            ls[x]=data1
       
    elif(ch==4):
        n=int(input("enter the data:"))
        for i in range(n):
            print(f"Enter the {i+1} data :")
            data=(input("enter the data:"))
            ls.remove(data)
   
    elif(ch==5):
        print("press 5 ")
        break;
    else:
        print("wrong choice")
        continue
