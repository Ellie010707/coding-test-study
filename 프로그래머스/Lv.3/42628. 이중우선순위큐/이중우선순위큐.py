#3:18
from heapq import heapify, heappush, heappop

def solution(operations):
    queue = []
    
    for operation in operations:
        op, num = operation.split()
        
        if op == "I":
            #answer.append(int(num))
            heappush(queue, int(num))
        elif len(queue) == 0: continue
        elif op == "D" and num == "-1": # 최솟값 삭제
            heappop(queue)
            
        elif op == "D" and num == "1": # 최댓값 삭제
            queue = [-q for q in queue]
            heapify(queue)
            heappop(queue)
            queue = [-q for q in queue]
            heapify(queue)
    
    if len(queue) == 0 : return [0,0]
    
    return [max(queue), min(queue)]