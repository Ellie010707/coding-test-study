import heapq

def solution(jobs):
    start, now, i = -1, 0, 0
    answer = 0
    
    heap = []
    
    while i < len(jobs):
        for time, job in jobs:
            if start < time <= now:
                heapq.heappush(heap, (job, time))
        
        if len(heap) > 0:
            job_tmp, time_tmp = heapq.heappop(heap)
            start = now
            now += job_tmp 
            answer += (now - time_tmp) 
            i += 1
            continue
        now += 1
        
    return answer // len(jobs)
            
            
            
            
            
            