'''
Created on 2017年12月27日

@author: linqt
'''
import time
import threading

local_name = threading.local()

def showName():
        print("%s thread done" % local_name.n)
    
class myThread(threading.Thread):
    
    def __init__(self,name,sleeptime):
        super(myThread,self).__init__()
        self.name = name
        self.sleeptime = sleeptime
    def run(self):
        local_name.n = self.name
        for tmp in range(0,5):
            print(self.name + ":" + str(tmp))
            time.sleep(self.sleeptime)
        showName()  
thread1 = myThread("thread1",2)
thread2 = myThread("thread2",4)

thread1.start()
thread2.start()