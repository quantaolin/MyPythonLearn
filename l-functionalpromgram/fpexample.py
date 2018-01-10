'''
Created on 2018年1月7日

@author: linqt
'''
from functools import reduce
from decimal import *

getcontext().prec = 8
def getSum(amountList):
    return reduce(lambda x,y:x+y,map(lambda x:(Decimal(str(x))%Decimal("1")*Decimal("100"))%Decimal("1")/Decimal("100"),amountList))

# print(getSum([5.123,2.123,12.1551231,15.2123]))

a = [12321,767,897,124,676,78987,1230]
def getpalindrome(a):
    return list(filter(lambda x: x==int(str(x)[::-1]),a))
# print(getpalindrome(a))

b = [{'orderid':141,'amount':14231.2},{'orderid':12,'amount':522132},{'orderid':151,'amount':1}]
# print(sorted(b,key=lambda x:x.get('orderid')))