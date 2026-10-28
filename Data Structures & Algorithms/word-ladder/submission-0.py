class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #word list --> graph 
        # how make word list thorugh 2 characters. For each 2 letter pair in graph and build out
        mp = defaultdict(list)
        for word in wordList:   
            for c1 in word:
                small = ''
                for c2 in word:
                    if c1==c2: small+='*'
                    else: small+=c2
                if not mp[small]: mp[small] = []
                
                mp[small].append(word)
            


  
        q = deque([beginWord])
        visited = set()
        count=0
        while q:
        
            word = q.popleft()
            count+=1
            visited.add(word)
            if word == endWord:
                return count
            for i in range(len(word)):
                key = word[:i]+'*'+word[i+1:]

                for nei in mp[key]:
                    if nei in visited:
                        continue
                    q.append(nei)
        return 0




    