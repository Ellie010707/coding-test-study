def solution(sizes):
    
    for s in sizes: s.sort(reverse = True)
    w = max([s[0] for s in sizes])
    h = max([s[1] for s in sizes])
    
    return w*h