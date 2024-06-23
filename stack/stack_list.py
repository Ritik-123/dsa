class Stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return ' , '.join(values)
    
    def is_empty(self):
        if self.list == []:
            return True
        return False
    
    def push(self, value):
        self.list.append(value)
        return f'value : {value} Inserted Successfully.'
    
    def pop(self):
        if self.is_empty():
            return 'No element to remove from stack.'
        self.list.pop()
        return 'Element removed Successfully.'
    
    def peek(self):
        if self.is_empty():
            return 'Stack is Empty.'
        return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = []
        return True 
    
# res = Stack()
# res.push(10)
# res.push(20)
# res.push(30)
# print(f'Stack is : {res}')
# res.pop()
# print(f'Stack is : {res}')
# b = res.peek()
# print(f'Peek function is {b}')
# a = res.is_empty()
# print(f'Empty func is : {a}')
# c = res.delete()
# print(c)
# print(res)

# Stack with Size Limit.
class CustomStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []
        
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return ' , '.join(values)
    
    def is_empty(self):
        if self.list == []:
            return True
        return False
    
    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        return False
    
    def push(self, value):
        if self.is_full():
            return 'Stack is Full.'
        self.list.append(value)
        return f'Value : {value} Inserted Successfully.'
    
    def pop(self):
        if self.is_empty():
            return 'No element to remove from stack.'
        self.list.pop()
        return 'Element Removed Successfully.'
    
    def peek(self):
        if self.is_empty():
            return 'Stack is Empty.'
        return self.list[len(self.list)- 1]
    
result = CustomStack(4)
result.push(10)
result.push(20)
result.push('30')
result.push('40')
print(f"List is : {result}")
emp=result.is_empty()
print(f"Empty is : {emp}")
pus = result.push('50')
print(f"Push : {pus}")
full = result.is_full()
print(f"Full : {full}")
p = result.pop()
print(f"Pop() : {p}")
print(result)
peek = result.peek()
print(f"Peak : {peek}")