# 3:55
from collections import deque

def solution(priorities, location):
    queue = deque()
    
    for i, p in enumerate(priorities):
        queue.append((p, i))
    
    count = 0
    while queue:
        xp, xi = queue.popleft()
        
        is_in = False
        for p, i in queue:
            if p > xp:
                is_in = True
                break
                
        if is_in:
            queue.append((xp, xi))
            continue
        
        count += 1
        if location == xi:     
            return count