'''
Created on 2017年12月27日

@author: linqt
'''
class father():
    def __init__(self):
        print("father init now")
    def pr(self):
        print("this is father")
        print(self)
    @classmethod
    def clazz(cls):
        print("this class method")
        print(cls)

class child(father):
    def __init__(self):
        print("child init now")
    def prc(self):
        print("this is child")
        print(self)
    @staticmethod
    def stat():
        print("this static method")

f=father()
print("----------------")
c=child()
print("----------------")
f.pr()
print("----------------")
c.pr()
print("----------------")
c.prc()
print("----------------")
c.stat()
print("----------------")
c.clazz()
print("----------------")
child.stat()
print("----------------")
child.clazz()