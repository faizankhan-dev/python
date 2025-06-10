s=set()
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
            s.add(data)

    elif(ch==2):
        print("Data are there ")
        print(s)
    elif(ch==3):
        n=int(input("enter the data:"))
        for i in range(n):
            print(f"Enter the {i+1} data :")
            data=(input("enter the data to update:"))
            s.update([data])
           
           
            
       
    elif(ch==4):
        n=int(input("enter the data:"))
        for i in range(n):
            print(f"Enter the {i+1} data :")
            data=(input("enter the data:"))
            s.discard(data)
   
    elif(ch==5):
        print("press 5 ")
        break;
    else:
        print("wrong choice")
        continue
