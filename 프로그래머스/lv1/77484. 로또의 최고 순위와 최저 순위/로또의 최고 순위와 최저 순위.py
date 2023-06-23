def solution(lottos, win_nums):
    answer = []
    rank = { 6:1, 5:2, 4:3, 3:4, 2:5 }
    cnt = 0
    zero = 0
    for l in lottos:
        if l in win_nums:
            cnt += 1
        elif l == 0:
            zero += 1
    
    max_rank = cnt + zero
    if max_rank <= 1:
        answer.append(6)
    else:
        answer.append(rank[max_rank])
    
    if cnt <= 1:
        answer.append(6)
    else:
        answer.append(rank[cnt])
        
    
    return answer