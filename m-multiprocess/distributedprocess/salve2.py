'''
Created on 2018年2月25日

@author: linqt
'''
import time,queue,multiprocessing
from multiprocessing.managers import BaseManager

BaseManager.register('get_task_queue')
BaseManager.register('get_result_queue')

m = BaseManager(address=('127.0.0.1', 5000), authkey=b'abc')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()

def delData(name):
    while True:
        try:
            n = task.get()
            print("%s get data:%s",(name,n))
            time.sleep(5)       
            result.put(name+"--"+n)
        except queue.Empty:
            print('task queue is empty.',name)
            break

if __name__=='__main__':
    f = multiprocessing.Process(target=delData, args=("Process-3",))
    t = multiprocessing.Process(target=delData, args=("Process-4",))
    f.start()
    t.start()    