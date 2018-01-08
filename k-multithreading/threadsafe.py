'''
Created on 2018年1月3日

@author: linqt
'''
import time
import threading
import random
import queue

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

# thread1.start()
# thread2.start()


class Producter(threading.Thread):
    def __init__(self,num,condit):
        super(Producter,self).__init__()
        self.num = num
        self.condit = condit
    def run(self):
        while True:
            self.condit.acquire()
            print("producter starter")
            tmp = random.randint(0, 256)
            print("producter product num = ",tmp)
            self.num.append(tmp)
            self.condit.notify()
            self.condit.release()
            time.sleep(random.random())
       
class Consumer(threading.Thread):
    def __init__(self,num,condit):
        super(Consumer,self).__init__()
        self.num = num
        self.condit = condit
    def run(self):
        while True:
            self.condit.acquire()
            print("consumer starter")
            print("consumer get num = ",self.num.pop())
            self.condit.wait()

a = []
condition = threading.Condition()
threadproduct=Producter(a,condition)
threadconsumer=Consumer(a,condition)

# threadproduct.start()
# threadconsumer.start()

semaphore = threading.Semaphore(2)

class SemaphoreExample(threading.Thread):
    def __init__(self,name):
        super(SemaphoreExample,self).__init__()
        self.name = name
    def run(self):
        with semaphore:
            for i in range(1,6):
                print(self.name,"thread get i =",i)
                time.sleep(random.random())

b=["THREAD-1","THREAD-2","THREAD-3","THREAD-4","THREAD-5"]
# for tmp in b:
#     SemaphoreExample(tmp).start()

class EventExample(threading.Thread):
    def __init__(self,flag,name):
        super(EventExample,self).__init__()
        self.flag=flag
        self.name=name
    def run(self):
        print(self.name,",thread ready")
        self.flag.wait()
        print(self.name,",thread run")
        
eventflag = threading.Event()
# for tmp in b:
#     EventExample(eventflag,tmp).start()
# print("all thread is ready")
# for i in range(0,5):
#     print(5-i)
#     time.sleep(1)
# print("lets go")
# eventflag.set()

class QueueProducter(threading.Thread):
    def __init__(self,q):
        super(QueueProducter,self).__init__()
        self.q=q
    def run(self):
        while True:
            for i in range(0,5):
                innerTmp = random.randint(0,100)
                print("product int =",innerTmp,",i=",i)
                self.q.put(innerTmp)                
            self.q.join()       
class QueueConsumer(threading.Thread):
    def __init__(self,q):
        super(QueueConsumer,self).__init__()
        self.q=q
    def run(self):
        while True:
            time.sleep(1)
            print("consumer get int =",self.q.get())
            self.q.task_done()
            time.sleep(1)
        time.sleep(2)
q = queue.Queue()
QueueProducter(q).start()
QueueConsumer(q).start()