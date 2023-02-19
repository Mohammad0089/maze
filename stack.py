class myStack():
    def __init__(self):
        self.items = list()
        
    def push(self, item)->None:
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return self.items == []
    
    def size(self)->int:
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

if __name__=="__main__":
    
    dishes = myStack()

    print(dishes)
    dishes.push("A")
    dishes.push("B")
    dishes.push("C")

    print(dishes)
    
    dishes.push("D")
    
    print(dishes)

    

    
