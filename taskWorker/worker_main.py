from multiprocessing.managers import BaseManager

from taskMaster import queue_manager
# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:

if __name__ == '__main__':
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    QueueManager.register('get_task_count')
    taskManager = QueueManager(address=('192.168.2.75', 5000), authkey=b'123')
    taskManager.connect()
    tasks = taskManager.get_task_queue()
    tasksCount = taskManager.get_task_count()
    for i in range(int(str(tasksCount))):
        r = tasks.get()
        print(r)
