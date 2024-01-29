N, M = map(int, input().split())

visited = [0] * (N + 1)

def bt(nums, visited):
    if len(nums) == M:
        for num in nums: 
            print(num, end=" ")
        print()
        return
    
    start = nums[-1] if nums else 1
    for idx in range(start, N + 1):
        if visited[idx] == 0:
            visited[idx] = 1
            bt(nums+[idx], visited)
            visited[idx] = 0
            
bt([], visited)