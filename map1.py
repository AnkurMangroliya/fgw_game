# def sq(s):
#     return s*s
# lis=[3,6,5,4,3,7,56,34,78]
# square = list(map(sq,lis))
# print(square)
#-------------------------------------------map function--------------------------
#
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# fun=[square,cube]
# for i in range(10):
#     lis = list(map(lambda x:x(i),fun))
#     print(lis)

#--------------------------------------filter function----------------------------
# lis=[1,5,4,3,6,67,35,2,1,45,78,65]
# def is_ger_5(s):
#     return s>5
# gr = list(filter(is_ger_5,lis))
# print(gr)
#--------------------------------------reduce-------------------------------------
from functools import reduce
list1=[1,2,3,4]
num = reduce(lambda x,y:x+y,list1)
print(num)