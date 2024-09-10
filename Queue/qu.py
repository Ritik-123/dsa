
class QueueList:
    def __init__(self):
        self.items= []

    def __str__(self):
        values= [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    
    def enqueue(self, value):
        if value:
            self.items.append(value)
            return 'True'
        return False

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is Empty'
        self.items.pop(0)
        return True
    
    def peek(self):
        if self.isEmpty():
            return 'Queue is Empty'
        return self.items[0]
    
    def delete(self):
        self.items= []
        return True


# queue_obj =QueueList()

#--------enqueue
# queue_obj.enqueue(1)
# queue_obj.enqueue(2)
# queue_obj.enqueue(3)
# print(queue_obj)

#-------- dequeue
# queue_obj.dequeue()
# print(queue_obj)

#-----------------------circular queue------------------------------------

class CircularQueue:
    def __init__(self, maxsize) -> None:
        self.items=  maxsize * [None]
        self.maxsize= maxsize
        self.top= -1
        self.start= -1

    def __str__(self) -> str:
        values= [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxsize:
            return True
        return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    
    def enqueue(self, value):
        if self.isFull():
            return 'Queue is full'
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start= 0
                self.items[self.top] = value
                return True
            
    def dequeue(self):
        if self.isEmpty():
            return 'List is empty'
        first_element= self.items[self.start]
        start= self.start
        if self.start == self.top:
            self.start= -1
            self.top= -1
        elif self.start +1 == self.maxsize:
            self.start= 0
        else:
            self.start += 1
        self.items[start]= None
        return first_element
    
    def peek(self):
        if self.isEmpty():
            return 'List is empty'
        return self.items[self.start]

    def delete(self):
        if self.isEmpty():
            return 'List is empty'
        self.items= self.maxsize * [None]
        self.start= -1
        self.top= -1

# cq_obj= CircularQueue(3)
# print(cq_obj.isEmpty())
# cq_obj.enqueue(2)
# cq_obj.enqueue(4)
# cq_obj.enqueue(6)
# print(cq_obj)

#---------------------queue using Linked List----------------

# class Node:
#     def __init__(self, value= None):
#         self.value= value
#         self.next= None

# class LinkedList:
#     def __init__(self):
#         self.head= None
#         self.tail= None

# class Queue:
#     def __init__(self):
#         self.linkedlist= LinkedList()

#     def __str__(self):
#         values= [str(x) for x in self.linkedlist]
#         return " ".join(values)
    
#     def enqueue(self, value):
#         newNode= Node(value)

#         if self.linkedlist.head == None:
#             self.linkedlist.head= newNode
#             self.linkedlist.tail= newNode
#         else:
#             self.linkedlist.tail.next= newNode
#             self.linkedlist.tail= newNode

#     def isEmpty(self):
#         if self.linkedlist.head == None:
#             return True
#         return False

#     def dequeue(self):
#         if self.isEmpty():
#             return 'Queue is empty'
#         tempnode= self.linkedlist.head
#         if self.linkedlist.head == self.linkedlist.tail:
#             self.linkedlist.head= None
#             self.linkedlist.tail= None
#         else:
#             self.linkedlist.head= self.linkedlist.head.next
#         return tempnode

#     def peek(self):
#         if self.isEmpty():
#             return 'Queue is empty'
#         return self.linkedlist.head

#     def delete(self):
#         self.linkedlist.head= self.linkedlist.tail= None

# ql_obj= Queue()
# print(ql_obj.isEmpty())
# ql_obj.enqueue(10)
# ql_obj.enqueue(20)
# ql_obj.enqueue(30)
# ql_obj.dequeue()
# print(ql_obj.isEmpty)
# print(ql_obj)
# print(ql_obj.delete())
# print(ql_obj)


#------queue using linked list-------

class Node:
    def __init__(self,value):
        self.value= value
        self.next= None

    def __str__(self):
        return str(self.value)
    
class QueueLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None

    def __iter__(self):
        current_node= self.head
        while current_node:
            yield current_node
            current_node= current_node.next

class Queue:
    def __init__(self):
        self.linkedlist= QueueLinkedList()

    def __str__(self):
        values= [str(x) for x in self.linkedlist]
        return " ".join(values)
    
    def enqueue(self, value):
        new_node= Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head= new_node
            self.linkedlist.tail= new_node
        else:
            self.linkedlist.tail.next= new_node
            self.linkedlist.tail= new_node

    def is_empty(self):
        if self.linkedlist.head == None:
            return True
        return False

    def dequeue(self):
        if self.is_empty():
            return "Empty Queue"
        temp_node= self.linkedlist.head
        if self.linkedlist.head == self.linkedlist.tail:
            self.linkedlist.head= self.linkedlist.tail= None
        else:
            self.linkedlist.head= self.linkedlist.head.next
        return temp_node
    
    def peek(self):
        if self.is_empty():
            return "Empty Queue"
        return self.linkedlist.head
    
    def delete(self):
        if self.is_empty():
            return "Empty Queue"
        self.linkedlist.head= self.linkedlist.tail= None
        return True

# qlinklist= Queue()
# qlinklist.enqueue(10)
# qlinklist.enqueue(20)
# qlinklist.enqueue(30)
# print(qlinklist)
# print(qlinklist.dequeue())
# print(qlinklist)
# print(qlinklist.is_empty())


#----------------------Using Collections Module-----------
from collections import deque

custom_queue= deque(maxlen= 4)
# custom_queue= deque()
# custom_queue.append(10)
# custom_queue.append(20)
# custom_queue.append(30)
# custom_queue.append(40)
# print(custom_queue)
# custom_queue.append(50)
# print(custom_queue)
# custom_queue.clear()
# print(custom_queue)


#-----------using q module----------------
# import queue as q
# cust_q= q.Queue(maxsize=3)
# print(cust_q.empty())
# cust_q.put(10)
# cust_q.put(20)
# cust_q.put(30)
# print(cust_q)
# print(cust_q.full())
# cust_q.put(40)
# print(cust_q)

#-----using multiprocessing module--------
from multiprocessing import Queue
"""
Same as above, functions are also used same as above.
"""