class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #word list --> graph 
        # how make word list thorugh 2 characters. For each 2 letter pair in graph and build out
        mp = defaultdict(list)
        for word in wordList:   
           
            for i in range(len(word)):
                small = word[:i] + '*' + word[i + 1:]
                mp[small].append(word)

            
        print(mp)

  
        q = deque([beginWord])
        visited = set()
        count=1
        while q:
            print(q)
            for _ in range(len(q)):
                word = q.popleft()
                
                visited.add(word)
                if word == endWord:
                    return count
                for i in range(len(word)):
                    key = word[:i]+'*'+word[i+1:]

                    for nei in mp[key]:
                        if nei in visited:
                            continue
                        q.append(nei)
            count+=1
        return 0




    