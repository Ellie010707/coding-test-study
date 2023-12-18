def solution(s):
    s = [ x.split(",") for x in s[2:-2].split("},{")]
    s.sort(key=len)
    
    ss = [int(y) for x in s for y in x]

    answer = list(dict.fromkeys(ss))
        
    return answer