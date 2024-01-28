from collections import deque
dv = [(0,1), (0,-1), (1,0), (-1, 0)]
def bfs(x, y, N):
    queue = deque([(x, y)])
    count = 1
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()

        for dx, dy in dv:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] == 1 or maps[nx][ny] == "0":
                continue
            visited[nx][ny] = 1
            queue.append((nx, ny))
            count += 1
    return count

N = int(input())
maps = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

answer = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == "1" and visited[i][j] == 0:
            answer.append(bfs(i, j, N))

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)