n, x = map(int, input().split())
l = list(map(int, input().split()))

maxi = 0
sumi = l[0]
cnti = 0
index = 1


for i in range(1, len(l)):
    sumi += l[i]
    index += 1
    if index == x:
        if sumi > maxi:
            maxi = sumi
            cnti = 1
        elif sumi == maxi:
            cnti += 1
        sumi -= l[i-x+1]
        index -= 1

if maxi == 0:
    print("SAD")
else:
    print(maxi)
    print(cnti)