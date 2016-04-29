class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
        
Queue = [] #using list as a queue

Queue.insert(0,'shiang') #enqueue of Queue
print(Queue)
Queue.insert(0,333) #enqueue of Queue
print(Queue)
size = len(Queue) #size of Queue
print(size)
Queue.pop() #dequeue of Queue
print(Queue)
