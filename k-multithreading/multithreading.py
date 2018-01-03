'''
Created on 2017年12月27日

@author: linqt
'''
import time
import threading

class myThread(threading.Thread):
    
    def __init__(self,name,sleeptime):
        self.name = name
        self.sleeptime = sleeptime
    def run(self):
        for tmp in range[0,5]:
            print(self.name + ":" + tmp)
            time.sleep(self.sleeptime)