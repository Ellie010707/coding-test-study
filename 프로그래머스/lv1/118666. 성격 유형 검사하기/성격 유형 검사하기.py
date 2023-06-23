def solution(survey, choices):
    d = { "R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    for i in range(0, len(survey)):
        if choices[i] < 4:
            key = survey[i][0]
        else:
            key = survey[i][1]
        
        choice = 0
        if choices[i] == 1 or choices[i] == 7:
            choice = 3
        elif choices[i] == 2 or choices[i] == 6:
            choice = 2
        elif choices[i] == 3 or choices[i] == 5:
            choice = 1
        
        d[key] += choice
    
    answer = []
    
    if d["R"] >= d["T"]:
        answer.append("R")
    else:
        answer.append("T")
        
    if d["C"] >= d["F"]:
        answer.append("C")
    else:
        answer.append("F")
        
    if d["J"] >= d["M"]:
        answer.append("J")
    else:
         answer.append("M")
            
    if d["A"] >= d["N"]:
        answer.append("A")
    else:
        answer.append("N")
        
    
    return ''.join(answer)