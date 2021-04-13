n1=int(input("enter your first number"))
n2=int(input("enter your second number"))
print("enter your operation")
print("+,_,*,/")
n3=input()
if n1==45 and n2==3 and n3=='*':
    print("555")
elif n1==56 and n2==9 and n3=='+':
    print("77")
elif n1==56 and n2==6 and n3=='/':
    print("77")
elif n3=='+':
    div=n1+n2
    print(div)
elif n3=='-':
    div=n1-n2
    print(div)
elif n3=='*':
    div=n1*n2
    print(div)
else :
    div=n1/n2
    print(div)