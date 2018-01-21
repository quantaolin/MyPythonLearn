'''
Created on 2018年1月21日

@author: linqt
'''
import multiprocessing, time, random, os

def firstProcess():
    print("my pid (%s),father pid (%s)" % (os.getpid(),os.getppid()))

# if __name__=='__main__':
#     firstProcess()
#     for i in range(0,5):
#         p=multiprocessing.Process(target=firstProcess)
#         p.start()

class processClass(multiprocessing.Process):
    def run(self):
        print("my pid (%s),father pid (%s)" % (os.getpid(),os.getppid()))

# if __name__=='__main__':
#     print("my pid (%s),father pid (%s)" % (os.getpid(),os.getppid()))
#     for i in range(0,5):
#         p=processClass()
#         p.start()

def processPoolExample(x):
    for i in range(0,5):
        print(x,"-",i)
        time.sleep(random.random())

# if __name__=='__main__':
#     p = multiprocessing.Pool(3)
#     for i in range(0,5):
#         p.apply_async(processPoolExample, args=("PROCESS"+str(i),))
#     print("main process wait")
#     p.close()
#     p.join()
#     print("all end")

def processGetResult(x):
    print("come in ",x)
    time.sleep(random.random())
    t=random.random()
    print(x," get random:",t)
    return t

if __name__=='__main__':
    p = multiprocessing.Pool(3)
    result=[]
    for i in range(0,5):
        result.append(p.apply_async(processGetResult, args=("PROCESS"+str(i),)))
    p.close()
    p.join()
    for res in result:
        print(res.get())   