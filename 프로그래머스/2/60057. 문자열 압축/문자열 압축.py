def solution(s):
    answer = len(s)  # 문자열을 1개 단위로 자를 경우의 길이로 초기화

    # 문자열을 자를 단위를 1부터 (문자열 길이 // 2)까지 반복
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]  # 이전에 비교한 문자열
        count = 1  # 반복 횟수

        # 단위 당 문자열 비교
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += (str(count) + prev) if count > 1 else prev
                prev = s[j:j + step]
                count = 1

        compressed += (str(count) + prev) if count > 1 else prev

        # 현재 단위로 압축한 문자열의 길이가 더 짧다면 업데이트
        answer = min(answer, len(compressed))

    return answer