'''
Created on 2018年1月7日

@author: linqt
'''
from functools import reduce
from decimal import *
getcontext().prec = 8
def getSum(amountList):
    return reduce(lambda x,y:x+y,map(lambda x:(Decimal(str(x))%Decimal("1")*Decimal("100"))%Decimal("1")/Decimal("100"),amountList))

print(getSum([5.123,2.123,12.1551231,15.2123]))
