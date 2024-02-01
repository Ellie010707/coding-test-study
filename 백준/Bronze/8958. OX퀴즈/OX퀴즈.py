n = int(input())

datas = [[ x for x in input().split("X") if x] for _ in range(n)]

scores = [0] * n
for idx, data in enumerate(datas):
    for d in data:
        for s in range(1, len(d) + 1):
            scores[idx] += s

for s in scores:
    print(s)