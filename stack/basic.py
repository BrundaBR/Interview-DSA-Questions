class Stack:
    def __init__(self):
        self.stack=[]
    
    def empty(self):
        if len(self.stack)==0:
            return 0
        else:
            return -1
        
    def push(self,element):
        self.stack.append(element)
        return 0
               
    def pop(self):
        
        if self.empty()==-1:
            self.stack.pop()
            return 0
        else:
            return -1
        
    def top(self):
        x=self.size()-1
        return self.stack[x]
    
    def size(self):
        return len(self.stack)
    
instance=Stack()
print(instance.push(1))
print(instance.push(2))
print(instance.push(3))
