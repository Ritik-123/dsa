class Heap:
    def __init__(self, size):
        self.customlist= (size + 1) * [None]
        self.heapSize= 0
        self.maxSize= size + 1

def peekHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]

def sizeOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.customList[i])
    