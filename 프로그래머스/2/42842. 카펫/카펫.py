#2;20

def solution(brown, yellow):
    answer = []
    
    brown = brown // 2
    
    r = brown
    c = 1
    
    while True:
        if (r - 2) * (c - 1) == yellow:
            return [r, c+1]
        
        r -= 1
        c += 1
        
        
    
    return answer