# class Node:
#     def __init__(self, item=None, next=None):
#         self.item = item
#         self.next = next
#
#
# class SLL:
#     def __init__(self, start=None):
#         self.start = start
#
#     def is_empty(self):
#         return self.start is None
#
#     def insert_at_start(self, data):
#         n = Node(data, self.start)
#         self.start = n
#
#     def insert_at_last(self, data):
#         n = Node(data)
#         if not self.is_empty():
#             temp = self.start
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = n
#         else:
#             self.start = n
#
#     def search(self, data):
#         temp = self.start
#         while temp is not None:
#             if temp.item is data:
#                 return temp
#             temp = temp.next
#         return None
#
#     def insert_after(self, temp, data):
#         if temp is not None:
#             n = Node(data, temp.next)
#             temp.next = n
#
#
#     def print_list(self):
#         temp = self.start
#         while temp is not None:
#             print(temp.item, end=" ")
#             temp = temp.next
#
#
#
# p = SLL()
# p.insert_at_start(20)
# p.insert_at_start(10)
# p.insert_at_last(30)
# p.insert_after(p.search(20), 60)
# if p.search(20) is not None:
#     print("Data have in item ")
# p.print_list()



import time
import threading
from threading import Thread

def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(5)
    print("Thread %i is awake" % i)

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
    print("Current Threads: %i." % threading.active_count())