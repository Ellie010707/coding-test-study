def solution(n):
    
    answer = ""
    is_su = True
    while n > 0:
        if is_su: answer += "수"
        else: answer += "박"
        n -=1
        is_su = not is_su
        
    
    return answer