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


class AVLNode:
    def __init__(self, data):
        self.data= data
        self.leftChild= None
        self.rightChild= None
        self.height= 0

def preOrderTraversal(rootNode):
    ''' root node -> left child -> right child '''
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    ''' left child -> root node -> right child '''
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    ''' left child -> right child -> root node  '''
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    customqueue= Queue()
    customqueue.enqueue(rootNode)
    while not customqueue.is_empty():
        root= customqueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customqueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customqueue.enqueue(root.value.rightChild)

def searchNode(rootNode, value):
    if rootNode.data == value:
        return 'Found'
    elif value < rootNode.data:
        if rootNode.leftChild.data == value:
            return 'Found'
        else:
            searchNode(rootNode.leftChild, value)
    else:
        if rootNode.rightChild == value:
            return 'Found'
        else:
            searchNode(rootNode.rightChild, value)
 
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightrotate(disBalanceNode):
    newRoot= disBalanceNode.leftChild
    disBalanceNode.leftChild= disBalanceNode.leftChild.rightChild
    newRoot.rightChild= disBalanceNode
    disBalanceNode.height= 1 + max(getHeight(disBalanceNode.leftChild), getHeight(disBalanceNode.rightChild))
    newRoot.height= 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftrotate(disBalanceNode):
    newRoot= disBalanceNode.rightChild
    disBalanceNode.rightChild= disBalanceNode.rightChild.leftChild
    newRoot.leftChild= disBalanceNode
    disBalanceNode.height= 1 + max(getHeight(disBalanceNode.leftChild), getHeight(disBalanceNode.rightChild))
    newRoot.height= 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getbalance(rootNode):
    if not rootNode:
        return
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild= insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild= insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height= 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance= getbalance(rootNode)
    
    # LL condition
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightrotate(rootNode)
    # LR condition
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild= leftrotate(rootNode.leftChild)
        return rightrotate(rootNode)
    # RR condition
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftrotate(rootNode)
    # RL condition
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild= rightrotate(rootNode.rightChild)
        return leftrotate(rootNode)
    return rootNode

def deleteAvlTreee(rootNode):
    rootNode.data= None
    rootNode.leftChild= None
    rootNode.rightChild= None
    return "AVL Tree deleted"

new_AVL= AVLNode(5)
new_AVL= insertNode(new_AVL, 10)
new_AVL= insertNode(new_AVL, 15)
new_AVL= insertNode(new_AVL, 20)
levelOrderTraversal(new_AVL)