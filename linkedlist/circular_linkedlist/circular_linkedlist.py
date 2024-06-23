class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        if self.length == 0:
            return f'Linked List is Empty. \n'
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return f'Linked List is  : {result} .\n'
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
        # return f'Node {new_node.value} has inserted successfully.'
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
           
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise Exception('Invalid Index Value')
        new_node = Node(value)
        if index == 0 :
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        
    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            
    def search(self, target):
        '''
        takes value and check if it exist in Linked List.
        '''
        temp_node = self.head
        while temp_node:
            if temp_node.value == target:
                return 'Found'
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return False
    
    def get(self, index):
        '''
        takes index value in input and return value at that index.
        '''
        
        if index < -1 or index > self.length:
            return False
        if index == -1:
            return self.tail
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node
    
    def set(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False
        
    def pop_first(self):
        if self.length == 0:
            return False
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        popped_node.next = None
        print(f'popped node next is :{popped_node.next}')
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return False
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev_node = self.head
            while prev_node != self.tail:
                prev_node = prev_node.next
            prev_node.next = self.head
            self.tail = prev_node
        popped_node.next = None
        self.length -= 1
        return popped_node
        
    # def pop_index(self, index):
    #     if self.length == 0:
    #         return False
    #     popped_node = self.get(index)
    #     temp_node = self.get(index-1)
    #     if index == 0 or self.length == 1:
    #         self.head = None
    #         self.tail = None
    #     else:
    #         temp_node.next = popped_node.next
    #     popped_node.next = None    
    #     self.length -= 1 
    #     return popped_node            
    
    def remove(self, index):
        popped_node = self.get(index)
        if index == 0 or self.length == 1:
           return self.pop_first()
        elif index == self.length-1:
            return self.pop()   
        prev_node = self.get(index-1)
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete(self):
        if self.length == 0:
            return 
        self.head = None
        self.tail.next = None
        self.tail = None
        self.length = 0
            
    
obj = CSLinkedList()
obj.append(10)
obj.append(20.05)
obj.append(-30)
print(f"After Appending : {obj}")
# obj.prepend(5)
# print(f"After Prepend : {obj}")
# obj.insert(1, 5)
# print(obj)
# obj.insert(0,4)
# print(obj)
# obj.insert(5,50)
# print(obj, obj.tail.value)
# obj.traverse()
# a=obj.get(4)
# print(a.value)
# a=obj.set(3, 100)
# print(a)
# print(obj)
# b = obj.pop_first()
# print(f'popped node : {b}')
obj.pop(3)
print(obj)