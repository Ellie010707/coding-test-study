import heapq

def solution(jobs):
    n = len(jobs)
    start, now = -1, 0
    heap = []
    answer = 0
    i = 0
    
    while i < n:
        print(start, now)

        for job in jobs:
            if start < job[0] <= now: # 작업의 시작시간이 start와 now 사이이면
                heapq.heappush(heap, (job[1], job[0])) # 작업의 소요시간 순으로 정렬됨
        
        if len(heap) > 0:
            job_time, start_time = heapq.heappop(heap)
            start = now
            now += job_time
            answer += (now - start_time)
            i += 1
            continue

        now += 1
    return answer // n
     