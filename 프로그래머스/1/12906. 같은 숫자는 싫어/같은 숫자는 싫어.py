#3:12
def solution(arr):
    answer = []
    pre = -1
    for a in arr:
        if a != pre:
            answer.append(a)
            pre = a
    return answer