from collections import deque

def solution(cacheSize, cities):
    answer = 0
    time = 0
    cities = [c.lower() for c in cities]
    cache = deque()

    if cacheSize == 0: time = len(cities) * 5
    else:
        for city in cities:
            hit = False

            for cc in cache:
                if cc == city: #hit
                    cache.remove(cc)
                    cache.append(city)
                    hit = True
                    time+= 1
                    break

            if not hit: #miss
                if len(cache) >= cacheSize: #full cache
                    cache.popleft()
                cache.append(city)
                time += 5

    print(time)

    return time



solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(3, ["Jeju", "Jeju", "Jeju"])