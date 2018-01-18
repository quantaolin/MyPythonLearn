'''
Created on 2018年1月14日

@author: linqt
'''
from enum import Enum, unique

Conter = Enum('Conter',('One','Two','Three','Four'))

print(Conter.One)

@unique
class Example(Enum):
    DOING='00'
    SUCESS='01'
    FAIL='02'

print(Example.DOING)
print(Example.DOING.value)