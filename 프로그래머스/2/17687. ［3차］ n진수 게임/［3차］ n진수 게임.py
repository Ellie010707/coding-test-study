def solution(n, t, m, p):
    answer = ""
    data = "-0"  # 0일때
    dic = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }

    for i in range(n*t*m):
        tmp = ""
        s = i

        while s > 0:  # n진수로 변환
            s, mod = divmod(s, n)
            tmp += dic[mod]
        data += tmp[::-1]

    for i in range(p, t * m + 1, m):
        answer += data[i]

    return answer


print(solution(2, 4, 2, 1))
