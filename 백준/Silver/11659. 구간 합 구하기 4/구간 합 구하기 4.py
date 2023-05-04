n, m = map(int, input().split())
ls = list(map(int, input().split()))

data = []
for i in range(m):
    data.append(list(map(int, input().split())))

suml = [0]
sumi = 0
for l in ls:
    sumi += l
    suml.append(sumi)


for i in range(m):
    print(suml[data[i][1]]-suml[data[i][0]-1])