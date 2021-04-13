print("enter you want to length of pettern")
n1=int(input())
print("enter 0 or 1")
n2 = int(input())
n3 = bool(n2)
if n3 == 0:
    while(n3<=n1):
        print("#"*n3,end=" ")
        print("\n",end=" ")
        n3 +=1
elif n3 == 1:
    count = n1
    while(count!=0):
        print("#"*count, end="")
        print("\n", end="")
        count-=1


