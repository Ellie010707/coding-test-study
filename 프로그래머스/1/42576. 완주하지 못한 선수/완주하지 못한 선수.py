from collections import Counter

def solution(participant, completion):

    count = Counter(completion)
    for p in participant: 
        if count[p] <= 0:
            return p
        count[p] -= 1
        