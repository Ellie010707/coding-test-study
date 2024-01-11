# 3:38
def solution(s):    
    opens, closes = 0, 0
    
    for pre in s:
        if pre == "(": 
            opens += 1
            continue
        if opens > closes:
            closes += 1
            continue
        return False
    
    if opens == closes:
        return True
    return False