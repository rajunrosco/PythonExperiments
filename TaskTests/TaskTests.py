import os
import sys
import subprocess
import queue
from threading import Thread


q = queue.Queue()
qp = queue.Queue()

class TimeoutThread(Thread):
    def __init__(self):
        self.stdout = subprocess.PIPE
        self.stderr = subprocess.PIPE
        self.p = None
        self.output = ''
        Thread.__init__(self)

    def run(self):
        print("Start Timeout 10")
        self.p = subprocess.Popen('timeout 2 & echo 2 & timeout 2 & echo 4 & timeout 2 & echo 6 & timeout 2 & echo 8 & timeout 2 & echo 10',
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
        print("process: {}".format(self.p.pid))
        q.put(self.p.pid)
        qp.put(self.p)
        self.output, self.error = self.p.communicate()
        print(self.output)
        #print("End Timeout 10")


MyTimerThread = TimeoutThread()
MyTimerThread.start()


#w = subprocess.Popen(['timeout','3'])

#try:
#    pid = q.get()
#    p = qp.get()
#    output, err = p.communicate()
#    print("Killing process: {}".format(pid))
#    k = subprocess.Popen(['taskkill','/PID', str(pid)], stdout=subprocess.PIPE)
#    kout, kerr = k.communicate()
#    print( kout )
#    print(output)
#except queue.Empty:
#    pass
#p = subprocess.Popen('timeout 2 & echo 2 & timeout 2 & echo 4 & timeout 2 & echo 6 & timeout 2 & echo 8 & timeout 2 & echo 10',shell=True)