# 3:20
import math
def solution(progresses, speeds):
    tmp = []
    for p, s in zip(progresses, speeds):
        day, ex = divmod((100-p),s)
        if ex != 0: day += 1
        tmp.append(day)
    
    answer = []
    pre = tmp[0]
    cnt = 0
    for t in tmp:
        if t > pre:
            answer.append(cnt)
            pre = t
            cnt = 1
            continue
        cnt += 1
    answer.append(cnt)
    
    return answer