class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result
    
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    
    def traverse(self):
        if self.length == 0:
            return False
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next
    
    def rev_traverse(self):
        if self.length == 0:
            return False
        temp_node = self.tail
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.prev
            
    def search(self, target):
        """
        Function return True if value exist in Linked List.
        """
        if self.length == 0:
            return False
        temp_node = self.head
        temp_index = 0
        while temp_node:
            if temp_node.value == target:
                return temp_index
            temp_node = temp_node.next
            temp_index += 1
        return False
    
    def get(self, index):
        """
        Function return the node at index value.
        """
        if index < 0 or index > self.length:
            return False
        if index < self.length // 2:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
        else:
            temp_node = self.tail
            for _ in range(self.length - 1, index, -1):
                temp_node = temp_node.prev
        # result = f"{temp_node} + {temp_node.value}"
        return temp_node
    
    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert(self, index, value):
        '''
        Insert new node at given index.
        '''
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        if self.length == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        temp_node = self.get(index-1)
        new_node.next = temp_node.next
        temp_node.next = new_node
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        self.length += 1
        
    def pop_first(self):
        if self.length == 0:
            return False
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
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
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node
    
res = LinkedList()
res.append(10)
res.append(20)
res.prepend(5)
# print(res.search(20))
# print(res.get(2))
# res.traverse()
print(f'Node is :{res}')
a=res.remove(3)
print(a)
# res.pop_first()
# res.insert(2, 200)
# res.set(1, 100)
print(res)
# res.pop()
# res.insert(4, 400)
# print(res)
print(f'Head is : {res.head.value}')
print(f'Tail is : {res.tail.value}')
print(f'Length of Node is : {res.length}')
# res.rev_traverse()