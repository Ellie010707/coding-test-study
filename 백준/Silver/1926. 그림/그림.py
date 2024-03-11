from collections import deque

n, m = map(int, input().split())

paint = [[ int(x) for x in input().split()] for _ in range(n)]

visited = [[0]*m for _ in range(n)]

def bfs(x, y, paint, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1
    size = 1
    dv = [(0,1), (0,-1), (1,0), (-1,0)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in dv:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == 1 or paint[nx][ny] == 0:
                continue
            else:
                visited[nx][ny] = 1
                size += 1
                queue.append((nx, ny))

    return size

count = 0
max_size = 0
for x in range(n):
    for y in range(m):
        if paint[x][y] == 1 and visited[x][y] == 0:
            max_size = max(bfs(x,y,paint,visited), max_size)
            count += 1


print(count)
print(max_size)