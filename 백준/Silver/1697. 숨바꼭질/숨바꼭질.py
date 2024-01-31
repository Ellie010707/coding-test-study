from collections import deque
MAX = 100001

def bfs(x, k):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == k:
            return array[x]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and not array[nx]:
                array[nx] = array[x] + 1
                q.append(nx)


n, k = map(int, input().split())
array = [0] * MAX
print(bfs(n, k))