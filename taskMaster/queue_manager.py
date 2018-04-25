import queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass

    # def get_task_queue(self):
    #     global task_queue
    #     return task_queue
    #
    # def get_result_queue(self):
    #     global result_queue
    #     return result_queue
    @property
    def taskCount(self):
        return self._taskCount

    @taskCount.setter
    def taskCount(self, count):
        self._taskCount = count


    @staticmethod
    def register_task_and_result_id(task_queue_id, result_queue_id):
        QueueManager.register(task_queue_id, callable=lambda: task_queue)
        QueueManager.register(result_queue_id, callable=lambda: result_queue)

    def dispatch_tasks(self, tasks):
        for task in tasks:
            print('Put task %s...' % task)
            self.get_task_queue().put(task)

        # for i in range(taskCount):
        #     r = self.get_result_queue().get(i)
        #     print('Result: %s' % r)
