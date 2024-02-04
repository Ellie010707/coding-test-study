from collections import deque
def solution(people, limit):
    
    people.sort(reverse = True)
    people = deque(people)
    
    answer = 0
    while people:
        if len(people) > 1 and (people[0] + people[-1] <= limit):
            answer += 1
            people.popleft()
            people.pop()
            continue
        people.popleft()
        answer += 1
    
    return answer