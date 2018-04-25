import queue
from multiprocessing.managers import BaseManager



class QueueManager(BaseManager):

    def __init__(self, task_queue_id, result_queue_id, port, authkey):
        # 任务队列
        self.__task_queue = queue.Queue()
        # 接收结果队列
        self.__result_queue = queue.Queue()
        # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
        self.register(task_queue_id, callable=lambda: self.__task_queue)
        self.register(result_queue_id, callable=lambda: self.__result_queue)

        super().__init__(address=('', port), authkey=authkey)

    def dispatch_task(self, tasks):
        taskCount = len(tasks)
        for task in tasks:
            print('Put task %s...' % task)
            self.__task_queue.put(task)

        for i in range(taskCount):
            r = self.__result_queue.get(timeout=10)
            print('Result: %s' % r)
