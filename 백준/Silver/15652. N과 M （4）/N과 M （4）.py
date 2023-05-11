N, M = map(int, input().split())

l = []

def dfs(n):
    if len(l) == M:
        print(" ".join(map(str, l)))
        return
    for i in range(1, N+1):
        if i >= n:
            l.append(i)
            dfs(i)
            l.pop()

dfs(1)