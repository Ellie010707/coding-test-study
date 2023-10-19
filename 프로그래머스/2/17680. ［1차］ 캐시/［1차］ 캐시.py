def solution(cacheSize, cities):
    answer = 0  # 실행 시간

    cache = []

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.append(cache.pop(cache.index(city)))
        else:
            answer += 5
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(city)

    return answer