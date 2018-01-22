'''
Created on 2018骞�1鏈�21鏃�

@author: linqt
'''
import multiprocessing, time, random, os
def productProcess(q):
    while True:
        time.sleep(1)
        tmp = random.randint(0,100)
        q.put(tmp)
        print("producter product int=%s,qsize=%s" % (tmp,q.qsize()))
            

def customerProcess(q):
    while True:
        time.sleep(2)
        print("customer get int=%s,qsize=%s" % (q.get(),q.qsize()))



# if __name__=='__main__':
#     q=multiprocessing.Queue(10)
#     p = multiprocessing.Process(target=productProcess, args=(q,))
#     c = multiprocessing.Process(target=customerProcess, args=(q,))
#     p.start()
#     c.start()


def productProcessPipe(p):
    while True:
        time.sleep(1)
        tmp = {"1":"one"}
        p.send(tmp)
        print("producter product int=%s" % tmp)

def customerProcessPipe(p):
    while True:
        print("customer get int=%s" % p.recv())
        

# if __name__=='__main__':
#     p1,p2=multiprocessing.Pipe(False)
#     p = multiprocessing.Process(target=productProcessPipe, args=(p2,))
#     c = multiprocessing.Process(target=customerProcessPipe, args=(p1,))
#     p.start()
#     c.start()

def processMange(name,m):
    tmp=random.randint(0,100)
    print("producter %s product int=%s" % (name,tmp))
    m[name]=tmp
    

# if __name__=='__main__':
#     m=multiprocessing.Manager().dict()
#     for i in range(0,5):
#         process=multiprocessing.Process(target=processMange, args=("Thread-"+str(i),m,))
#         process.start()
#         process.join()
#     print(m)
    