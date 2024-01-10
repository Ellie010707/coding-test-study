from collections import Counter

def solution(nums):
    max_i = len(nums)//2
    count = Counter(nums)
    return min(max_i, len(count.keys()))