'''
Created on 2017年12月23日

@author: linqt
'''
from collections import namedtuple

list=["uber",14123,3.21,'dgaer']
print("ori:" ,list)
print(list[2:4])
list.append('7123')
print("append:" ,list)
print("pop:" ,list.pop())
print("afterpop:" ,list)
list.remove(3.21)
print("afterremove:" ,list)
print("index of 'uber':" ,list.index('uber'))
del list[1]
print("after del:" ,list)
print(list*2)
list.extend(['abc','efg'])
print("afterextend：" ,list)
print("lenght:" ,len(list))

print()
print("for loop of list:")
for var in list:
    print(var)
print()

for i,var in enumerate(list):
    print(i,var)
print()

tunple=("yun",781,'1414',0.98)
print(tunple[3])
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('x=%s,y=%s'% (p.x,p.y))