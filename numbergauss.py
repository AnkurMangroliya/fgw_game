print("your gauss 9 time")
#gauss number=19
n=1
while(n<=9):
    n+=1
    print("enter your number")
    m=int(input())
    if m==19 :
        print("won")
        print("no of  guess he took finish=", n)
        break
    elif m<19 :
        print("choose big number")
    elif m>19 :
        print("choose small number")
    elif n>9 :
        print("game over ")
    print("lest guess=", 10 - n)
    if (n > 9):
        print("game over")
