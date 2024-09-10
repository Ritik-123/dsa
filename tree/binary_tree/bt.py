# from Queue.qu import Queue


#------queue using linked list-------

class Node:
    def __init__(self,value):
        self.value= value
        self.next= None

    def __str__(self):
        return str(self.value)
    
class QueueLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None

    def __iter__(self):
        current_node= self.head
        while current_node:
            yield current_node
            current_node= current_node.next

class Queue:
    def __init__(self):
        self.linkedlist= QueueLinkedList()

    def __str__(self):
        values= [str(x) for x in self.linkedlist]
        return " ".join(values)
    
    def enqueue(self, value):
        new_node= Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head= new_node
            self.linkedlist.tail= new_node
        else:
            self.linkedlist.tail.next= new_node
            self.linkedlist.tail= new_node

    def is_empty(self):
        if self.linkedlist.head == None:
            return True
        return False

    def dequeue(self):
        if self.is_empty():
            return "Empty Queue"
        temp_node= self.linkedlist.head
        if self.linkedlist.head == self.linkedlist.tail:
            self.linkedlist.head= self.linkedlist.tail= None
        else:
            self.linkedlist.head= self.linkedlist.head.next
        return temp_node
    
    def peek(self):
        if self.is_empty():
            return "Empty Queue"
        return self.linkedlist.head
    
    def delete(self):
        if self.is_empty():
            return "Empty Queue"
        self.linkedlist.head= self.linkedlist.tail= None
        return True


class TreeNode:
    def __init__(self, data):
        self.data= data
        self.leftchild= None
        self.rightchild= None

bt_obj= TreeNode('Drinks')
leftchild= TreeNode('Hot')
rightchild= TreeNode('Cold')
bt_obj.leftchild= leftchild
bt_obj.rightchild= rightchild

def preorder_traversal(rootnode):
    if not rootnode:
        return None
    print(rootnode.data)
    preorder_traversal(rootnode.leftchild)
    preorder_traversal(rootnode.rightchild)

# preorder_traversal(bt_obj)

def inorder_traversal(rootnode):
    if not rootnode:
        return None
    inorder_traversal(rootnode.leftchild)
    print(rootnode.data)
    inorder_traversal(rootnode.rightchild)

# inorder_traversal(bt_obj)

def postOrderTraversal(rootnode):
    if not rootnode:
        return None
    postOrderTraversal(rootnode.leftchild)
    postOrderTraversal(rootnode.rightchild)
    print(rootnode.data)

# postOrderTraversal(bt_obj)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return None
    customqueue= Queue()
    customqueue.enqueue(rootNode)
    while not (customqueue.is_empty()):
        root= customqueue.dequeue()
        print(root.value.data)
        if root.value.leftchild is not None:
            customqueue.enqueue(root.value.leftchild)
        
        if root.value.rightchild is not None:
            customqueue.enqueue(root.value.rightchild)

        
newbt= TreeNode('Drinks')
leftchild= TreeNode('Hot')
tea= TreeNode('Tea')
coffee= TreeNode('Coffee')
leftchild.leftchild= tea
leftchild.rightchild= coffee
rightchild= TreeNode('Cold')
newbt.leftchild= leftchild
newbt.rightchild= rightchild

# levelOrderTraversal(newbt)

#---------Search a Node in B.T--------------------

def search_node(rootnode, value):
    if not rootnode:
        return "B.T not exist"
    customqueue= Queue()
    customqueue.enqueue(rootnode)
    while not (customqueue.is_empty()):
        root= customqueue.dequeue()
        if root.value.data == value:
            return "Success"
        if root.value.leftchild is not None:
            customqueue.enqueue(root.value.leftchild)
        
        if root.value.rightchild is not None:
            customqueue.enqueue(root.value.rightchild)
    
    return "Not Found"

# print(search_node(newbt, "Tea"))

#------------- insert a new node in B.T----------

def insert_node(rootnode, newnode):
    if not rootnode:
        return 'B.T not exist'
    customqueue= Queue()
    customqueue.enqueue(rootnode)
    while not (customqueue.is_empty()):
        root= customqueue.dequeue()
        
        if root.value.leftchild is not None:
            customqueue.enqueue(root.value.leftchild)
        else:
            root.value.leftchild= newnode
            return 'Successfully inserted'
        
        if root.value.rightchild is not None:
            customqueue.enqueue(root.value.rightchild)
        else:
            root.value.rightchild= newnode
            return 'successfully inserted'
        
# newnode= TreeNode('Fanta')
# print(insert_node(newbt, newnode))
# levelOrderTraversal(newbt)


# -----------------delete a Node in B.T--------------
def get_deepest_node(rootnode):
    if not rootnode:
        return 
    customqueue= Queue()
    customqueue.enqueue(rootnode)
    while not (customqueue.is_empty()):
        root= customqueue.dequeue()

        if root.value.leftchild is not None:
            customqueue.enqueue(root.value.leftchild)
        
        if root.value.rightchild is not None:
            customqueue.enqueue(root.value.rightchild)
    node= root.value
    return node

def delete_deepest_node(rootnode, dnode):
    if not rootnode:
        return 
    customqueue= Queue()
    customqueue.enqueue(rootnode)
    while not (customqueue.is_empty()):
        root= customqueue.dequeue()

        if root.value is dnode:
            root.value= None
            return 
        
        if root.value.rightchild:
            if root.value.rightchild is dnode:
                root.value.rightchild= None
                return
            else:
                customqueue.enqueue(root.value.rightchild)
        
        if root.value.leftchild:
            if root.value.leftchild is dnode:
                root.value.leftchild= None
            else:
                customqueue.enqueue(root.value.leftchild)
        
def delete_node_bt(rootnode,node):
    if not rootnode:
        return
    customqueue= Queue()
    customqueue.enqueue(rootnode)
    while not (customqueue.is_empty()):
        root= customqueue.dequeue()
        if root.value.data == node:
            deepest_node= get_deepest_node(rootnode)
            root.value.data= deepest_node.data
            delete_deepest_node(rootnode, deepest_node)
            return "Node has been successfully deleted"
        
        if root.value.leftchild is not None:
            customqueue.enqueue(root.value.leftchild)

        if root.value.rightchild is not None:
            customqueue.enqueue(root.value.rightchild)
    return 'Failed to delete'

# print(delete_node_bt(newbt, 'Coffee'))
# levelOrderTraversal(newbt)

def delete_bt(rootnode):
    rootnode.data= None
    rootnode.leftchild= None
    rootnode.rightchild= None
    return "Binary Tree has been successfully deleted"

# print(delete_bt(newbt))
# levelOrderTraversal(newbt)


#---------B.T using Python List-----------
class BinaryTree():
    def __init__(self, size):
        self.customList= size * [None]
        self.lastUsedIndex= 0
        self.maxsize= size

    def __str__(self):
        return self.customList
    
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxsize:
            return 'Binary Tree is full'
        self.customList[self.lastUsedIndex + 1]= value
        self.lastUsedIndex += 1
        return 'Node successfully inserted'
    
    def searchnode(self, value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return 'Found'
        return 'Not Found'
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 'Index out of range'
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return "Intdex out of range"
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 'Index out of range'
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return 'Binary Tree is Empty'
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i]= self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]= None
                self.lastUsedIndex -= 1
                return 'Node has been successfully deleted'
            
    def deleteBT(self):
        self.customList= None
        return 'B.T has been deleted'

newbt= BinaryTree(8)
# print(newbt.insertNode('Drinks'))
newbt.insertNode('Drinks')
newbt.insertNode('Hot')
newbt.insertNode('Cold')
newbt.insertNode('Tea')
newbt.insertNode('Coffee')
newbt.insertNode('Cola')
# print(newbt.searchnode('Cold'))
# newbt.preOrderTraversal(1)
# newbt.inOrderTraversal(1)
# newbt.postOrderTraversal(1)
# print(newbt.deleteNode('Tea'))
print(newbt.deleteBT())
newbt.levelOrderTraversal(1)
