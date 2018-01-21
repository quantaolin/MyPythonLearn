'''
Created on 2018年1月7日

@author: linqt
'''
from functools import reduce
from decimal import *
import random
import functools
import datetime
import time
import os

getcontext().prec = 8
def getSum(amountList):
    return reduce(lambda x,y:x+y,map(lambda x:(Decimal(str(x))%Decimal("1")*Decimal("100"))%Decimal("1")/Decimal("100"),amountList))

# print(getSum([5.123,2.123,12.1551231,15.2123]))
#print(reduce(os.path.join,[os.path.abspath('.'),"user","set0","tes1"]))

a = [12321,767,897,124,676,78987,1230]
def getpalindrome(a):
    return list(filter(lambda x: x==int(str(x)[::-1]),a))
# print(getpalindrome(a))

b = [{'orderid':141,'amount':14231.2},{'orderid':12,'amount':522132},{'orderid':151,'amount':1}]
# print(sorted(b,key=lambda x:x.get('orderid')))

def getListFunction(x):
    def t(y):
        for i in range(0,10):
            yield y
            y += x
    return t

fun2 = getListFunction(2)
fun3 = getListFunction(3)
# print(list(fun2(0)))
# print(list(fun3(0)))

def getErrorFunction(x):
    def t(y):
        for i in range(0,10):
            yield y
            y += x[0]
    return t

xt=[2]
efun2 = getErrorFunction(xt)
xt.clear()
xt.append(3)
efun3 = getErrorFunction(xt)
# print(list(efun2(0)))
# print(list(efun3(0)))

def gettime(func):
    @functools.wraps(func)
    def ehance(x):
        begin = datetime.datetime.now()
        print("process begin in:",begin.strftime('%Y-%m-%d %H:%M:%S'))
        re = func(x)
        end = datetime.datetime.now()
        print("process end in:",end.strftime('%Y-%m-%d %H:%M:%S'))
        print("process use time :" ,(end-begin).seconds)
        return re
    return ehance

def gettime2(text):
    def decorator(func):
        @functools.wraps(func)
        def ehance(x):
            begin = datetime.datetime.now()
            print(text," begin in:",begin.strftime('%Y-%m-%d %H:%M:%S'))
            re = func(x)
            end = datetime.datetime.now()
            print(text," end in:",end.strftime('%Y-%m-%d %H:%M:%S'))
            print(text," use time :" ,(end-begin).seconds)
            return re
        return ehance
    return decorator

@gettime
def get2(x):
    print("now in orifunction")
    time.sleep(2)
    return 2*x

@gettime2("mainprocess")
def get3(x):
    print("now in orifunction")
    time.sleep(2)
    return 3*x      


# print(get2(3))
# print(get3(3))

int2=functools.partial(int, base=16)
# print(int2('abc'))
# print(int('abc',base=16))