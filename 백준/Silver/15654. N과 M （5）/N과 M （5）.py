N, M = map(int, input().split())
ll = list(map(int, input().split()))
ll.sort()

l = []

def dfs():
    if len(l) == M:
        print(" ".join(map(str, l)))
        return
    for i in ll:
        if i not in l:
            l.append(i)
            dfs()
            l.pop()

dfs()