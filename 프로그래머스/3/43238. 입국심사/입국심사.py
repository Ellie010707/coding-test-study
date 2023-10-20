def solution(n, times):
    min_time = 1
    max_time = max(times) * n
    
    answer = max_time

    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        total_people = sum([mid_time // time for time in times])

        if total_people < n:
            min_time = mid_time + 1
        else:
            answer = mid_time
            max_time = mid_time - 1

    return answer