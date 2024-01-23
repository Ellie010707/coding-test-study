#3:22
def solution(n, lost, reserve):
    arr = [1] * (n + 1)
    
    
    for r in reserve: arr[r] = 2
    for l in lost: arr[l] -= 1
    
    for idx, a in enumerate(arr):
        if a == 0:
            if idx > 1 and arr[idx-1] == 2:
                arr[idx-1] -= 1
                arr[idx] += 1
            elif idx < n and arr[idx+1] == 2:
                arr[idx+1] -= 1
                arr[idx] += 1
    return n - arr[1:].count(0)