def itre(n):
    f=1
    for i in range (n):
        f=f*(i+1)
    return f
n=int(input("enter a number"))
print("factoeial is equal to=",itre(n))

def rec(n):
    if n==1:
        return 1
    else:
        return n * rec(n-1)
print("factorial of  rec=",rec(n))