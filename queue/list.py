EMPTY= 'Queue list is Empty.'

class Queue:
    """
    This Queue is using just List.
    Algo : FIFO(First In First Out)
    """
    def __init__(self, maxsize):
        self.list= []
        self.maxsize= maxsize
        
    def __str__(self):
        if self.is_empty():
            return EMPTY
        values= [str(i) for i in self.list]
        return ' , '.join(values)
        
    def peek(self):
        if self.is_empty():
            return EMPTY
            # return 'Queue List is Empty !.'
        return self.list[0]
    
    def is_empty(self):
        if self.list == []:
            return True
        return False
    
    def is_full(self):
        if len(self.list) == self.maxsize:
            return True
        return False
            
    def enqueue(self, item):
        if self.is_full():
            return 'Queue List is Full !.'
        self.list.append(item)
        return f"After enqueue list is : {self.__str__()}"
    
    def dequeue(self):
        if self.is_empty():
            return EMPTY,self.__str__()
            # return 'Queue List is Empty !.', self.__str__()
        self.list.pop(0)
        return f"After dequeue list is : {self.__str__()}"
    
    def delete(self):
        self.list = []
    
res= Queue(4)
print(res.enqueue(10))
print(res.enqueue(20))
print(res.enqueue(30))
print(res.enqueue(40))
print(res.enqueue(50))
print(res.dequeue())
print(res.is_empty())
print(res.is_full())
print(res.peek())
res.delete()
print(res)
    