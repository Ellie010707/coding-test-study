from queue import deque
import copy

N, M, V = map(int, input().split())

tmp = [[int(x) for x in input().split()] for _ in range(M)]

def dfs(x):
    visited[x] = 1
    print(x, end=" ")

    if visited.count(0) == 1 or not datas[x]:
        return 
    
    for i in datas[x]:
        if visited[i] == 0:
            dfs(i)
    return

def bfs(x):
    queue = deque([x])

    while queue:
        x = queue.popleft()
        visited[x] = 1
        print(x, end=" ")

        for i in datas[x]:
            if visited[i] == 0 and i not in queue:
                queue.append(i)
    return

datas = [[] for _ in range(N+1)]
for i, j in tmp: 
    datas[i].append(j)
    datas[j].append(i)
for data in datas: data.sort()

visited = [0] * (N + 1)
dfs(V)
print()

visited = [0] * (N + 1)
bfs(V)