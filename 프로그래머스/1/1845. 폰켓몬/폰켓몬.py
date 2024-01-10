from collections import Counter

def solution(nums):
    max_i = len(nums)//2
    count = Counter(nums)
    return len(count.keys()) if len(count.keys()) <= max_i else max_i