#3:18
from heapq import heapify, heappush, heappop

def solution(operations):
    queue = []
    
    for operation in operations:
        if operation[0] == "I":
            heappush(queue, int(operation.split()[1]))
        elif len(queue) == 0: continue
        elif operation == "D 1": # 최댓값 삭제
            queue.pop()
        elif operation == "D -1": # 최솟값 삭제
            heappop(queue)
            
    if len(queue) == 0 : return [0,0]
    
    return [max(queue), min(queue)]