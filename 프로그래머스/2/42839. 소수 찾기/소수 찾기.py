#10:26
def solution(numbers):
    
    def helper(prefix, lefts):
        yield prefix
        if not lefts: return
        for idx, l in enumerate(lefts):
            yield from helper(prefix + [l], lefts[:idx]+lefts[idx+1:])
    
    numbers = [ x for x in numbers ]
    numbers = [ int("".join(x)) for x in list(helper([], numbers)) if x ]
    numbers = set(numbers)
    
    def isPrime(num):
        for n in range(2, num):
            if num % n == 0:
                return False
        return True
    
    answer = 0
    for num in numbers:
        if num == 0 or num == 1: continue
        if isPrime(num): answer += 1
    return answer