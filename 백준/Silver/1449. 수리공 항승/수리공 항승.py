N, L = map(int, input().split())
datas = [int(x) for x in input().split()]
datas.sort()

L -= 1
now_d = datas[0]
count = 1
for d in datas[1:]:
    if (d - now_d) > L:
        now_d = d
        count += 1
        
print(count)
        