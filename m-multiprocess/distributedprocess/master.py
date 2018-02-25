'''
Created on 2018年2月25日

@author: linqt
'''
import queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()
 
BaseManager.register('get_task_queue', callable=lambda: task_queue)
BaseManager.register('get_result_queue', callable=lambda: result_queue)
 
manager = BaseManager(address=('', 8080), authkey=b'abc')
manager.start()
task = manager.get_task_queue()
result = manager.get_result_queue()
 
for i in range(10):
    task.put(i)
    print('master put i =',i)
print('master put done')
 
for i in range(10):
    print("master get result = ",result.get())
manager.shutdown()
print('master exit.')
