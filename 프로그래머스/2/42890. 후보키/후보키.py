from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 모든 가능한 조합들
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:  # 유일성 # 셋으로 중복 제거한 길이와 row의 길이가 같을 때(중복이 없다는 뜻)
            put = True

            for x in unique:
                if set(x).issubset(set(i)):  # 최소성 # x.issubset(y) # x가 y의 부분집합인가?
                    put = False
                    break

            if put:
                unique.append(i)

    return len(unique)


