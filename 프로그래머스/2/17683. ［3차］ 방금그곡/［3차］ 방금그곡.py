def get_code(s):
    s = (
        s.replace("C#", "c")
        .replace("D#", "d")
        .replace("F#", "f")
        .replace("G#", "g")
        .replace("A#", "a")
    )
    return s


def get_time(start, end):
    return (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))


def solution(m, musicinfos):
    answer = ""
    m = get_code(m)
    index = 0
    ms = []

    for musicinfo in musicinfos:
        music = musicinfo.split(",")
        time = get_time(music[0], music[1])
        code = get_code(music[3])
        full_code = (
            code * (time // len(code)) + code[: time % len(code)]
        )  # 재생된 시간 만큼의 음악 코드
        if m in full_code:
            ms.append([time, index, music[2]])
            index += 1

    if len(ms) == 1:
        answer = ms[0][2]
    elif len(ms) > 1:
        answer = sorted(ms, key=lambda x: (-x[0], x[1]))[0][2]
    else:
        answer = "(None)"

    return answer