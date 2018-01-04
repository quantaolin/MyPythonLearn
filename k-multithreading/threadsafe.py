'''
Created on 2018年1月3日

@author: linqt
'''
import time
import threading

class MyThread(threading.Thread):
    a = "null"
    def __init__(self,name,sleeptime):
        super(MyThread,self).__init__()
        self.name = name
        self.sleeptime = sleeptime
    def run(self):
        threadLock.acquire()
        global a
        a = self.name
        print(self.name + "set a done, a =" + a)
        time.sleep(self.sleeptime)
        print(self.name + "get a, a =" + a)
        threadLock.release()
        
threadLock = threading.RLock()

thread1 = MyThread("thread1",2)
thread2 = MyThread("thread2",1)

thread1.start()
thread2.start()

    