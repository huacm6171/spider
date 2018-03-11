#coding=utf-8
import threading
import Queue

class Work(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start
    def run(self):
        while True:
            try:
                do, args = self.work_queue.get(block=False)
                do(args)
                self.work_queue.task_done()
            except:
                break
                
    
class WorkManager(object):
    def __init__(self, threadNum = 1):
        self.work_queue = Queue.Queue()
        self.threads = []
        self.__init_thread_pool(threadNum)
    
    def __init_thread_pool(self, thread_num):
        for i in range(thread_num):
            self.threads.append(Work(self.work_queue))
    
    def add_job(self, func, *args):
        self.work_queue.put((func, list(args)))