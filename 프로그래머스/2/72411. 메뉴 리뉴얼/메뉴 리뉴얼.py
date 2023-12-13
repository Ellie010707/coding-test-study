def dfs(menu, tmp, order, length, depth, cur): 
    if depth == length:
        tmp = ''.join(sorted(tmp))
        menu[tmp] = menu.get(tmp, 0) + 1
        return
    
    for i in range(cur, len(order)):
        tmp[depth] = order[i]
        dfs(menu, tmp, order, length, depth+1, i+1)
    

def solution(orders, course):
    answer = []
    menu = {}

    for order in orders:
        for length in course:
            tmp = [0] * length
            dfs(menu, tmp, order, length, 0, 0)

    result = [0]*(max(course)+1)

    for k, v in menu.items():
        if len(k) in course:
            if v >= 2 and v >= result[len(k)]:
                result[len(k)] = v
    

    for length in course:
        for k, v in menu.items():
            if len(k) == length and v == result[length]:
                answer.append(k)

    return sorted(answer)