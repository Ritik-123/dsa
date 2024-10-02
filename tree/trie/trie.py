
class TrieNode:
    def __init__(self):
        self.children= {}
        self.endOfString= False

class Trie:
    def __init__(self):
        self.root= TrieNode()

    def insertString(self, word):
        
        current = self.root
        
        for i in word:
            ch= i
            node= current.children.get(ch)
            if node == None:
                node= TrieNode()
                current.children.update({ch:node})
            current= node
        
        current.endOfString= True
        print('Successfully Inserted.')

    def searchString(self, word):
        
        current= self.root

        for i in word:
            node= current.children.get(i)
            if not node:
                return False
            current= node
        
        if current.endOfString == True:
            return True
        return False

def deleteString(root, word, index):
    ch= word[index]
    currentNode= root.root.children.get(ch)
    canThisNodeBeDeleted= False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False
    
    index = len(word) - 1
    if index:
        if len(currentNode.children) >= 1:
            currentNode.endOfString= False
            return False
        else:
            root.children.pop(ch)
            return True
        
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False
    
    canThisNodeBeDeleted= deleteString(currentNode, word, index + 1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False

newTrie= Trie()
newTrie.insertString('App')
newTrie.insertString('Appl')
deleteString(newTrie,'App', 0)
print(newTrie.searchString('App'))
# newTrie= Trie()
# newTrie.insertString('App')
# newTrie.insertString('Apps')