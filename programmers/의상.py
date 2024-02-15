def solution(clothes):
    closet = {}
    comb = 1

    for c in clothes: closet[c[1]] = []
    for c in clothes:
        closet[c[1]].append(c[0])

    for c in closet: comb *= (len(closet[c])+1)

    return comb-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])