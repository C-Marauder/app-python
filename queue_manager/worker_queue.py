import queue
from multiprocessing.managers import BaseManager

from queue_manager.constant import GET_TASK_QUEUE_METHOD_NAME, GET_RESULT_QUEUE_METHOD_NAME, GET_TASK_COUNT_METHOD_NAME


class QueueManager(BaseManager):
    def __init__(self,address,authkey):
        QueueManager.register('get_task_queue')
        QueueManager.register('get_result_queue')
        QueueManager.register('get_task_count')
        super().__init__(address=address,authkey=authkey)
        self.connect()

    def get_task_to_work(self, func):
        tasks = self.get_task_queue()
        tasksCount = self.get_task_count()
        print(tasksCount)
        for i in range(10):
            print(i)
            task = tasks.get()
            print(task)
            func(task)

