'''
Created on 2017年12月23日

@author: linqt
'''
def fun1(arg1,arg2):
    arg3 = arg1+arg2
    return arg3
print(fun1(2,3))

fun2 = lambda arg1,arg2: arg1+arg2
print(fun2(1,2))
