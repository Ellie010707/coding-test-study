from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[ 0 for _ in range(M)] for _ in range(N)]
    
    dv = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def bfs(x, y, N, M):
        nonlocal visited
        
        queue = deque([(x, y, 1)])
        
        while queue:
            x, y, l = queue.popleft()
            
            if x == N-1 and y == M-1: return l
            
            for dx, dy in dv:
                nx = x + dx
                ny = y + dy
                                
                if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] == 1 or maps[nx][ny] == 0: 
                    continue
                
                visited[nx][ny] = 1
                queue.append((nx, ny, l+1))
        return -1
    
    return bfs(0, 0, N, M)