class Node: 
    def __init__(self):
        self.children = dict()
        self.end = False

class Trie: 
    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        
        cur.end = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return cur.end

    def hasPrefix(self, prefix):
        cur = self.root

        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # add words to trie
        # backtrack and find all possible words
        # if word in trie, add to res, 
        # return res
        ROWS, COLS = len(board), len(board[0])
        trie = Trie()
        visited = set()
        for word in words:
            trie.add(word)

        res = set()
        
        def dfs(r, c, subset):
            if min(r,c)<0 or r == ROWS or c == COLS or (r,c) in visited:
                return

            word_so_far = ''.join(subset) + board[r][c]
            if not trie.hasPrefix(word_so_far):
                return

            if trie.search(word_so_far):
                res.add(word_so_far)


            visited.add((r,c))
            neighbors = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            
            for nr, nc in neighbors:
                subset.append(board[r][c])
                dfs(nr, nc, subset)
                subset.pop()

            visited.remove((r,c))
            

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, [])

        return list(res)
            



