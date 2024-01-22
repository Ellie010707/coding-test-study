# 2:32
import copy

def solution(k, dungeons):
    
    maxc = 0
    
    def dfs(k, cnt, lefts):
        nonlocal maxc
        
        maxc = max(maxc, cnt)
        if not lefts: return
            
        for idx, l in enumerate(lefts):
            least, used = l
            if k >= least and k >= used:
                new_lefts = copy.deepcopy(lefts)
                new_lefts.pop(idx)
                dfs(k - used, cnt + 1, new_lefts)
    dfs(k, 0, dungeons)    
    return maxc