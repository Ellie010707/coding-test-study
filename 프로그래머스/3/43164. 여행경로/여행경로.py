#2:50
import copy

def solution(tickets):
    
    answer = []
    
    def dfs(depth, goal, departure, route, lefts):
        nonlocal answer
        
        if depth == goal:
            answer.append(route)
            return
        
        for idx, l in enumerate(lefts):
            if l[0] == departure:
                tmp_route = copy.deepcopy(route)
                tmp_lefts = copy.deepcopy(lefts)
                tmp_lefts.pop(idx)
                dfs(depth+1, goal, l[1], tmp_route+[l[1]], tmp_lefts)
                
        
    
    
    dfs(0, len(tickets),"ICN", ["ICN",], tickets)
    answer.sort()
    return answer[0]