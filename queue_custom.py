from collections import deque

class Queue():
    def __init__(self) -> None:
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
       return  self.items.popleft()
    def peek(self):
        return self.items[0]
    def is_empty(self)->bool:
         return not self.items
    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    myQueue = Queue()
    print(myQueue)
    print(myQueue.is_empty( ))    
    myQueue.enqueue('A')
    myQueue.enqueue('F')
    myQueue.enqueue('H')
    myQueue.dequeue()
    print(myQueue.peek())
    print(myQueue)
    print(myQueue.is_empty( ))  