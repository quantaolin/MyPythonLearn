'''
Created on 2017年12月23日

@author: linqt
'''
flag = 0
while flag < 5:
    print(flag)
    flag+=1
else:
    print("flag bigger than five")
    
strs="hello world!"
for tmp in strs:
    print(tmp)
else:
    print("this is end")

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x, str)]
print(L2)

D1 = {1:"ONE",2:"TWO",3:"THREE"}
L3 = [str(k) + "=" + v for k,v in D1.items()]
print(L3)