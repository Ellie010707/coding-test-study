
n = int(input())
r = 0
fibb = [0,1]
for i in range(2, n+1):
    fibb.append(fibb[-1]+fibb[-2])

print(fibb[-1])