'''
Created on 2018年1月7日

@author: linqt
'''
class pi():
    def __enter__(self):
        print("in enter")
        return 3.14
    def __exit__(self, type,value, trace):
        print("in exit")


with pi() as i:
    print(i)