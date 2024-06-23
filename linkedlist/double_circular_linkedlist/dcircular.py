class Node:
    def __init__(self,value):
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
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' <-> '
        return result
            
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail 
        else:
            self.tail.next = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail = new_node
            self.head.prev = self.tail
        self.length += 1
        return True
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if self.length == 0 or index == self.length:
            # Insert if node is empty or insert at the last.
            return self.append(value)
        new_node = Node(value)
        if index == 0 and self.length != 0:
            # Insert at begining.
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.head = new_node
        else:    
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            
            new_node.next = temp_node.next
            temp_node.next.prev = new_node
            temp_node.next = new_node
            new_node.prev = temp_node
             
        self.length += 1
            
    def traverse(self):
        if self.length == 0:
            return False
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break

    def rev_traverse(self):
        if self.length == 0:
            return False 
        temp_node = self.tail
        while temp_node:
            print(temp_node.value)
            if temp_node == self.head:
                break
            temp_node = temp_node.prev
    
    def search(self, value):
        if self.length == 0:
            return False
        temp_node = self.head
        while temp_node:
            if temp_node.value == value:
                return temp_node.value
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return False
    
    def delete(self, index):
        if self.length == 0:
            return False
        if index == 0:
            if self.head == self.tail:
                self.head.next = None
                self.head.prev = none
                self.head = None
                self.tail = None
                self.length -= 1
                return True
            else:
                temp_node = self.head
                self.tail.next = self.head.next
                self.head.next.prev = self.tail
                self.head = self.head.next
                temp_node.next = None
                temp_node.prev = None
                
        elif index == self.length:
            temp_node = self.tail
            self.tail.prev.next = self.head
            self.head.prev = self.tail.prev
            self.tail = self.tail.prev
            temp_node.next = None
            temp_node.prev = None
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            temp_node.prev.next = temp_node.next
            temp_node.next.prev = temp_node.prev
            temp_node.next = None
            temp_node.prev = None                                        
        self.length -= 1
        return temp_node
    
    def delete_all(self):
        if not self.head:
            return False
        temp_node = self.head
        while temp_node:
            temp_node.prev = None
            temp_node = temp_node.next
        self.head = None
        self.tail = None
        print('Linkedlist Deleted Successfully.')
        return True
    
res = LinkedList()
res.append(10)
res.append(20)
print(f"Node is : {res}")
res.insert(0,5)
print(res)
res.insert(3,300)
print(res)
res.delete(2)
# a=res.search(20)
# print(a)
# res.insert(2,200)
print(res)
print(f"Head is {res.head.value}")
# res.traverse()
res.delete_all()
print(res)
print(f"Tail is : {res.tail.value}")


# res.rev_traverse()