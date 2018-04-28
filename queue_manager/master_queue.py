import queue
from multiprocessing.managers import BaseManager

from queue_manager.constant import GET_TASK_QUEUE_METHOD_NAME, GET_RESULT_QUEUE_METHOD_NAME, GET_TASK_COUNT_METHOD_NAME


class QueueManager(BaseManager):
    # 发送任务的队列:
    __task_queue = queue.Queue()
    # 接收结果的队列:
    __result_queue = queue.Queue()
    def __init__(self,address,authkey,taskCount:int):
        QueueManager.register('get_task_queue', callable=lambda: self.__task_queue)
        QueueManager.register('get_result_queue', callable=lambda: self.__result_queue)
        QueueManager.register('get_task_count', callable=lambda: taskCount)

        super().__init__(address=address,authkey=authkey)

    def dispatch_tasks(self, tasks:list):
        self.start()
        for task in tasks:
            self.get_task_queue().put(task)
            print('Put task %s...' % task)
        count = len(tasks)

        for i in range(count):
            r = self.get_result_queue().get()
            print('Result: %s' % r)
        self.shutdown()