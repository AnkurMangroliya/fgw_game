# def funcret(n):
#     if n==0:
#         return print
#     if n==1:
#         return sum
# a = funcret(1)
# print(a)
#
# def executor(func):
#     func("this")
# executor(print)

#main portion
def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec
@dec1
def who_is_ankur():
    print("ankur is a good boy")

# who_is_ankur = dec1(who_is_ankur)
who_is_ankur()