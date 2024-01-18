# 3:45
from collections import deque

def solution(begin, target, words):
    answer = []
    visited = [0 for _ in range(len(words))]
    
    def bfs(begin, target, words, visited):
        queue = deque([(begin, 0)])
        
        while queue:
            now, c = queue.popleft()
            
            if now == target: 
                return c
            
            for i in range(len(target)):
                if now[i] == target[i]:
                    continue
                    
                try: tmp_now = now[:i] + now[i+1:]
                except: tmp_now = now[:i]
                
                
                for w, word in enumerate(words):
                    
                    try: tmp_word = word[:i] + word[i+1:]
                    except: tmp_word = word[:i]
                    
                    if tmp_now == tmp_word and visited[w] == 0:
                        visited[w] = 1 
                        queue.append((word, c + 1))
        return 0
            
    
    return bfs(begin, target, words, visited)