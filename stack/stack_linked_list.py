class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
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
            if temp_node:
                result += ' -> '
        return result
    
    def push(self, value):
        new_node = Node(value)
        pass
        