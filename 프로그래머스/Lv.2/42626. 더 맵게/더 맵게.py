import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while True:
        curr = heapq.heappop(scoville)
        if curr < K:
            try:
                count += 1
                heapq.heappush(scoville, curr + (heapq.heappop(scoville) * 2))
            except:
                return -1
        else: break
    
    return count