'''
Created on 2018年1月14日

@author: linqt
'''
from enum import Enum, unique

@unique
class Example(Enum):
    DOING='00'
    SUCESS='01'
    FAIL='02'

print(Example.DOING)
print(Example.DOING.value)