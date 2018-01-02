'''
Created on 2017年12月26日

@author: linqt
'''
class BussinessException(RuntimeError):
    def __init__(self,retcode,retmsg):
        self.retcode=retcode
        self.retmsg=retmsg
        
try:
    #raise BussinessException(8701,"test")
    print(1+1)
    raise  Exception("test")
except BussinessException as e:
    print(e.retcode,e.retmsg)
except Exception as e:
    print(e.args)
else:
    print("no exception")
finally:
    print("done")