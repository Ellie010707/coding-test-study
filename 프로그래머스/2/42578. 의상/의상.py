from collections import defaultdict


def solution(clothes):
    d = defaultdict(int)
    for v, k in clothes: d[k] += 1

    answer = 1
    for v in d.values(): answer *= (v+1)
    return answer - 1
        