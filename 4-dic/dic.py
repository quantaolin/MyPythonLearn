'''
Created on 2017年12月23日

@author: linqt
'''
dicttmp={'one':1,'two':2,'three':3}
dicttmp['four']=4
print(dicttmp['three'])
print(dicttmp['four'])

for index in dicttmp.keys():
    print(dicttmp[index])

print(dict([('h',1),('m',2),('n',3)]))