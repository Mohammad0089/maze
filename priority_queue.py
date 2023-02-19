import heapq

class Priority_queue():
    def __init__(self) -> None:
        self.items = []
    def put(self,item,priority):
        heapq.heappush(self.items,(priority, item))
    def get(self):
        return heapq.heappop(self.items)[1]
    def is_empty(self):
        return not self.items
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    activity = Priority_queue()

    activity.put("studying",3)
    activity.put("eating",2)
    activity.put("sleeping",1)
    activity.put("excersizing",2)
    
    print(activity)
    print(activity.get())
    print(activity.get())
    print(activity.get())
    print(activity)

