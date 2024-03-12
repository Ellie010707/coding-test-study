N, K = map(int, input().split())

datas = [[int(x) for x in input().split()] for _ in range(N)]

datas.sort(key=lambda x : [x[1], x[2], x[3]], reverse=True)

i = 1
grade = 1
pre_gold, pre_silver, pre_bronze = datas[0][1], datas[0][2], datas[0][3]

for n, gold, silver, bronze in datas:
    if pre_gold != gold or pre_silver != silver or pre_bronze != bronze:
        grade = i
        pre_gold, pre_silver, pre_bronze = gold, silver, bronze
    i += 1
    if n == K:
        print(grade)
        break