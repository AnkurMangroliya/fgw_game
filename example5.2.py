import datetime

def gettime():
    return datetime.datetime.now()
def take(k):
    c=int(input("enter 1 for food and 2 for excersize"))
    if k==1 :
        if c==1:
            value=input("type here\n")
            with open("harry-ex.txt","a") as f:
                f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfuly writeen")
        elif c==2:
            value = input("type here\n")
            with open("harry-ex.txt", "a") as f:
                f.write(str[str(gettime())] + ":" + value + "\n")
            print("successfuly writeen")
    if k == 2:
        if c == 1:
            value = input("type here\n")
            with open("marry-ex.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfuly writeen")
        elif c == 2:
            value = input("type here\n")
            with open("marry-ex.txt", "a") as f:
                f.write(str[str(gettime())] + ":" + value + "\n")
            print("successfuly writeen")
    if k == 3:
        if c == 1:
            value = input("type here\n")
            with open("maddy-ex.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfuly writeen")
        elif c == 2:
            value = input("type here\n")
            with open("maddy-ex.txt", "a") as f:
                f.write(str[str(gettime())] + ":" + value + "\n")
            print("successfuly writeen")
def retraive(k):
    c=int(input("enter 1 for food and 2 for excersize"))
    if k==1 :
        if c==1:

            with open("harry-ex.txt") as f:
                for i in f:
                    print(i,end="")
        elif c==2:

            with open("harry-ex.txt") as f:
                for i in f:
                    print(i,end="")
    if k == 2:
        if c == 1:
            with open("marry-ex.txt") as f:
                for i in f:
                    print(i,end="")
        elif c == 2:

            with open("marry-ex.txt") as f:
                for i in f:
                    print(i,end="")
    if k == 3:
        if c == 1:

            with open("maddy-ex.txt") as f:
                for i in f:
                    print(i,end="")
        elif c == 2:

            with open("maddy-ex.txt") as f:
                for i in f:
                    print(i,end="")
a = int(input("enter 1 for log and 2 for reatrive"))
if a==1:
    b=int(input("1 for harry 2 for marry 3 for maddy"))
    take(b)
else:
    b=int(input("1 for harry 2 for marry 3 for maddy"))
    retraive(b)

































