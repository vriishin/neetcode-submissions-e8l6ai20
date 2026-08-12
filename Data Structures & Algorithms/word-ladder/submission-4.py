class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # word list = graph nodes and you want every node to be every wordLength-1 letter combo with the one letter replaced by a universal letter (*) 
        # 
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] +'*'+word[i+1:]
                graph[key].append(word)
        q = deque([beginWord])
        turns = 1
        # shortest path can be tracked by levels or by passing current turn alongside word
        visited = set()
        print(graph)
        while q:
            print(q)
            for _ in range(len(q)):
                word = q.popleft()
                print(word)
                if word == endWord:
                    return turns
                visited.add(word)

                
                for i in range(len(word)):
                    key = word[:i] + '*' + word[i+1:]
                    print(key)
                    for nei in graph[key]:
                        if nei in visited:
                            continue
                        q.append(nei)
            turns +=1
        return 0
        
                    

