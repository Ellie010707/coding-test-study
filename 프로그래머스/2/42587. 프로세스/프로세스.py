# 3:55
from collections import deque

def solution(priorities, location):
    queue = deque()
    
    for i, p in enumerate(priorities):
        queue.append((p, i))
    
    count = 0
    while queue:
        xp, xi = queue.popleft()
        
        if any(xp < p for p, i in queue):
            queue.append((xp, xi))
            continue
        
        count += 1
        if location == xi:     
            return count