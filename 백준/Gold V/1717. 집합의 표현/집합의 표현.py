
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

n , m = map(int, input().split())
parents = [x for x in range(n + 1)]


for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
