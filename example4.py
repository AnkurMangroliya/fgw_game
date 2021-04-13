print("enter you want to length of pettern")
n1=int(input())
print("enter 0 or 1")
n2 = int(input())
n3 = bool(n2)
if (n3==True):
    for i in range(1,n1+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif (n3==False):
    for i in range(n1,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()