# 1:50

def solution(n, computers):
    visited = [0] * n

    def dfs(depth, cans): 
        nonlocal computers, visited
        
        if visited[depth] == 1: return
        visited[depth] = 1 
        
        for idx, can in enumerate(cans):
            if idx == depth: continue
            if can == 1: 
                dfs(idx, computers[idx])
    
    
    count = 0
    for idx in range(n):
        if visited[idx] == 0:
            count += 1
            dfs(idx, computers[idx])
        
    return count