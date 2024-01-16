import copy
answer = 0
def solution(numbers, target):
    def dfs(now, numbers, target):
        global answer
        if len(numbers) == 0:
            if now == target: answer += 1
            return
        
        tmp_numbers = copy.deepcopy(numbers)
        tmp = tmp_numbers.pop(0)
        
        dfs(now + tmp, tmp_numbers, target)
        dfs(now - tmp, tmp_numbers, target)
        
    dfs(0, numbers, target)
    return answer