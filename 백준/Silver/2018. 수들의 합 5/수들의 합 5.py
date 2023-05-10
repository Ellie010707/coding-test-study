
N = int(input())
start, end = 1, 1
cnt = 0
sum = 1

while start < N//2+1:
    if sum < N:
        end += 1
        sum += end
    elif sum > N:
        sum -= start
        start += 1
    else:
        cnt += 1
        end += 1
        sum -= start
        sum += end
        start += 1


print(cnt + 1)