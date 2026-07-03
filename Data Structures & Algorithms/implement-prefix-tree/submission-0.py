class Node:
    def __init__(self):
        self.children = dict()
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current_node = self.root
        for c in word: 
            if c not in current_node.children:
                current_node.children[c] = Node()
            
            current_node = current_node.children[c]
        
        current_node.end = True





    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.end    
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        
        return True
        