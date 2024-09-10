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


class BSTNode:
    def __init__(self, data):
        self.data= data
        self.leftChild= None
        self.rightChild= None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data= nodeValue
    
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild= BSTNode(nodeValue) 
        else:
            insertNode(rootNode.leftChild, nodeValue)

    else:
        if rootNode.rightChild is None:
            rootNode.rightChild= BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "Node inserted Successfully"

def preOrderTraversal(rootNode):
    """
    Root node -> Left subtree -> Right subtree
    """
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    """
    Left subtree -> Root node -> Right subtree
    """
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    """
    Left subtree -> Right Subtree -> Root node
    """
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customqueue= Queue()
    customqueue.enqueue(rootNode)
    while not (customqueue.is_empty()):
        root= customqueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customqueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customqueue.enqueue(root.value.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print('Value found')
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print('Value found')
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print('Value found')
        else:
            searchNode(rootNode.rightChild, nodeValue)

def successor(rightsubtree):
    """
    **successor** 
        -> return the smallest value in rightsubtree.

    Here we pass the right subtree as rootNode.
    """
    current= rightsubtree
    while current.leftChild is not None:
        current= rightsubtree.leftChild
    return current

def deleteNode(rootNode, value):
    if not rootNode:
        return
    if value < rootNode.data:
        rootNode.leftChild= deleteNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild= deleteNode(rootNode.rightChild, value)
    else:
        if rootNode.leftChild is None:
            temp= rootNode.rightChild
            rootNode= None
            return temp
        if rootNode.rightChild is None:
            temp= rootNode.leftChild
            rootNode= None
            return temp
        
        temp= successor(rootNode.rightChild)
        rootNode.data= temp.data
        rootNode.rightChild= deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data= None
    rootNode.leftChild= None
    rootNode.rightChild= None
    return 'BST deleted successfully'

newbst= BSTNode(None)
insertNode(newbst, 70)
insertNode(newbst, 50)
insertNode(newbst, 90)
insertNode(newbst, 30)
insertNode(newbst, 60)
insertNode(newbst, 80)
insertNode(newbst, 100)
insertNode(newbst, 20)
insertNode(newbst, 40)

# preOrderTraversal(newbst)
# inOrderTraversal(newbst)
# postOrderTraversal(newbst)
# levelOrderTraversal(newbst)
# searchNode(newbst, 80)
# deleteNode(newbst, 70)
print(deleteBST(newbst))
levelOrderTraversal(newbst)

# newbst.data
# newbst.leftChild.data
# newbst.rightChild.data