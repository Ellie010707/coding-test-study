n, k = map(int,input().split())

l = [False] * (n+1)
cnt = 0

for i in range(2, n+1):
    if l[i] == False:
        for j in range(i, n+1, i):
            if l[j] == False:
                l[j] = True
                cnt += 1
                if cnt == k:
                    print(j)