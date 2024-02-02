from collections import deque

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dv:
            nx = x + dx
            ny = y + dy
        
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))


dv = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    pos = []
    for i in range(K):
        pos.append([int(x) for x in input().split()])
   
    maps = [[0] * M for _ in range(N)]
    for x, y in pos:
        maps[y][x] = 1

    visited = [[0] * M for _ in range(N)]
    count = 0
    for x, y in pos:
        if visited[y][x] == 0:
            bfs(y, x, visited)
            count += 1
    
    print(count)