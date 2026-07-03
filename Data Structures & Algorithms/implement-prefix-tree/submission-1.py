class Node: 

    def __init__(self):
        self.children = dict()
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current_node = self.root

        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = Node()
            
            current_node = current_node.children[letter]
        
        current_node.end = True

    def search(self, word: str) -> bool:
        current_node = self.root

        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return False
        
        return current_node.end
    
        

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        i = 0
        for c in prefix: 
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                return False

        return True
        