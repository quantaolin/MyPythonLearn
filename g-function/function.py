'''
Created on 2017年12月23日

@author: linqt
'''
def fun1(arg1,arg2):
    arg3 = arg1+arg2
    return arg3
print(fun1(2,3))

def fun2(a,b,*c,d,**e):
    print("a=",a,"b=",b,"c=",c,"d =",d,"e=",e)
fun2("1","2","3","4","5",d="6",e="7",f="8",g="9")


fun3 = lambda arg1,arg2: arg1+arg2
print(fun3(1,2))