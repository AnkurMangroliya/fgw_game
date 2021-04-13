x=56
def abkur():
    x=23

    def harry():
        global x
        x = 34
    harry()
    print(x)
abkur()
print(x)
