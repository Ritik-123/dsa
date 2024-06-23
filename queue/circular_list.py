EMPTY= ' Circular Queue list is Empty !.'
FULL= ' Circular Queue list is Full !.'
class Queue:
    """
    This is Circular Queue using List.    
    """
    def __init__(self, maxsize):
        self.list= maxsize * [None]
        self.maxsize= maxsize
        self.start= -1
        self.top= -1
        
    def __str__(self):
        if self.is_empty():
            return EMPTY
        values= [str(i) for i in self.list]
        return ' , '.join(values)
        
    def peek(self):
        if self.is_empty():
            return EMPTY
            # return 'Queue List is Empty !.'
        return self.start
    
    def is_empty(self):       
        if self.top == -1:
            return True
        return False 
    
    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.maxsize:
            return True
        return False
            
    def enqueue(self, value):
        if self.is_full():
            return FULL, self.__str__()
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start 
            if self.start and self.top == -1:
                self.list.append(value)
                self.start += 1
            else:
                self.list.append(value)
            self.top += 1
            print(f"Inside Enqueue : {self.start}, {self.top}")
            return f'After enqueue : {self.__str__()}'
    
    def dequeue(self):
        if self.is_empty():
            return EMPTY
        elif self.start == self.top:
            self.start = self.top = -1
        else:
            self.start += 1
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
    