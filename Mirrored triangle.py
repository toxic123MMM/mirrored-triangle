print("half pyramid pattern made up of * symbols")
n=int(input("enter a number of rows: "))
ch=input("please enter any character: ")

for i in range(1,n+1):
    for j in range(1,n+1):
        if (j<= n-i):
            print("",end=" ")
        else:
            print('%c'%ch,end=' ')
    print()
