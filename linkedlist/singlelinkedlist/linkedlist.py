class Node2:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        '''
        When we print the object we get our whole Linked List.
        '''
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def appends(self, value):
        '''
        Function add the Node in the last of Linked List.
        '''
        new_node = Node2(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        """_summary_
            Add Node in the starting of Linked List.
        Args:
            value (int): To add the value in a Node and add it into a Linked List.
        """
        new_node = Node2(value)
        if self.length == 0:
            self.head = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def gets(self, target):
        '''
        function takes index value in input and return value.
        '''
        temp_node = self.head
        index = 0
        while temp_node:
            if target == index:
                return temp_node
                # return temp_node.value
            temp_node = temp_node.next
            index += 1
        return 'Not Found.'

    def insert(self, index, value):
        '''
        Insert a Node at Given Index.
        '''
        new_node = Node2(value)
        temp_node = self.gets(index)
        prev_node = self.gets(index-1)
        if index < 0 or index > self.length:
            raise ValueError('Index Value is not Acceptable.\n')
        prev_node.next = new_node
        new_node.next = temp_node
        
    def pop_element(self):
        """
        Delete a last Node in a Linked List.
        """
        temp_node = self.head
        popped_node = self.tail
        while temp_node.next != self.tail:
            temp_node = temp_node.next 
        self.tail = temp_node
        temp_node.next = None
        self.length -= 1
        return f'Popped Node is : {popped_node} .\n'

    def pop_first(self):
        '''
        Delete The first Node in a Linked List.
        '''
        if self.length == 0:
            return f'Linked List is Empty.\n'
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        
    def pop_index(self, index):
        '''
        Delete The Node at Given Index.
        '''
        if index < 0 or index > self.length:
            raise ValueError('Index Value is not Acceptable.\n')
        temp_node = self.gets(index)
        prev_node = self.gets(index-1)
        popped_node = temp_node
        prev_node.next = temp_node.next
        temp_node.next = None
        self.length -= 1
        return f'Popped Node is : {popped_node} .\n'
                
    def search(self, target):
        '''
        function takes value in input and return it's index value.
        '''
        temp_node = self.head
        index = 0
        while temp_node:
            if temp_node.value == target:
                return index
            temp_node = temp_node.next
            index += 1
        return 'Not Found.' 
    
    def delete(self):
        if self.length == 0:
            return 'Node already Empty.\n'
        self.head = None
        self.tail = None
        self.length = 0
        return f'Deleted Succecfully. Head is : {self.head}. Tail is : {self.tail} .\n'
                    
result = LinkedList2()
print(f"result is : {result}\n")
result.appends(10)
result.appends(20)
result.appends(30)
result.appends(40)
print(f'After appending : {result}')
result.prepend(100)
print(f'After prepend : {result}')
result.insert(1,200)
print(f"After insert : {result}\n")
result.pop_element()
print(f'After pop_element : {result}')
result.pop_first()
print(f'After pop_first : {result}')
a = result.search(20)
print(f"20 at index : {a}")
a = result.gets(2)
print(f'At index 2 value is {a}')
print(f'After Pop index : {result.pop_index(1)}')
print(f'result is : {result}')
print(f"length is : {result.length}")
result.delete()
print(f'Node is : {result}')
