N, M = map(int, input().split())
ll = list(map(int, input().split()))
ll.sort()

l = []

def dfs(n):
    if len(l) == M:
        print(" ".join(map(str, l)))
        return
    for i in ll:
        if i not in l and i >= n:
            l.append(i)
            dfs(i)
            l.pop()

dfs(ll[0])