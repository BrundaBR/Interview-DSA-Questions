class Queue:
    def __init__(self) -> None:
        self.q=[]
    
    def push(self,element):
        self.q.append(element)
    
    def pop(self):
       print( self.q.pop(0))



instance=Queue()
instance.push(1)
instance.push(2)
instance.push(3)
instance.push(4)
instance.pop()





