import csv
def write():
    f=open("para.csv",'w',newline='')
    x=csv.writer(f)
    L=[]
    while True:
        s_no=int(input("Enter application number:"))
        first_name=input("Enter First Name:")
        last_name=input("Enter Last Name:")
        salary=int(input("Enter salary:"))
        Data=[s_no,first_name,last_name,salary]
        L.append(Data)
        ch=input("Do you want to continue(Yes/No):")
        if ch in 'nN':
            break
    x.writerows(L)
    f.close()
def read ():
    f=open("para.csv",'r')
    y=csv.reader(f)
    for i in y:
        print(i)
    f.close()
while True:
    print ("Main Menu")
    print("1.Fill Data")
    print("2.Display Data")
    print("3.Exit")
    x=int(input("Enter a choice:"))
    if x==1:
        write()
    elif x==2:
        read()
    elif x==3:
        break
    else:
        print("Wrong Choice")
        
        
    