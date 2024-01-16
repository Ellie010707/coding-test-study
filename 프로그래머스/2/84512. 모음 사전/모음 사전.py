def solution(word):
    d = ['', 'A', 'E', 'I', 'O', 'U']
    cnt = 0
    for i1 in d:
        if not i1: continue        
        for i2 in d:
            if i2 and not i1: break
            for i3 in d:
                if i3 and not i2: break
                for i4 in d:
                    if i4 and not i3: break
                    for i5 in d:
                        if i5 and not i4: break
                        cnt += 1
                        if i1+i2+i3+i4+i5 == word:
                            print(i1+i2+i3+i4+i5)
                            return cnt
                        
                        
                        
    return answer