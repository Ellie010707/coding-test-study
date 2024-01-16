def solution(answers):
    answer = [0,0,0]
    
    length = len(answers)
    person1 = [1, 2, 3, 4, 5] * (length // 5 + 1)
    person2 = [2, 1, 2, 3, 2, 4, 2, 5] * (length // 8 + 1)
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (length // 10 + 1)
    
    for i, a in enumerate(answers):
        if person1[i%5] == a: answer[0] += 1
        if person2[i%8] == a: answer[1] += 1
        if person3[i%10] == a: answer[2] += 1
    
    return [i+1 for i, a in enumerate(answer) if a == max(answer)]