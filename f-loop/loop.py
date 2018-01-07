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

def triangles(max):
    n,a = 0,[1]
    while n<max:
        yield a
        a.insert(0, 0)
        a.append(0)
        a = [a[i] + a[i + 1] for i in range(0,len(a)-1)]
        n += 1

for i in triangles(5):
    print(i)