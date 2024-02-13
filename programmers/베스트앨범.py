def solution(genres, plays):
    genre = list(set(genres))
    album = {}
    play = {}
    best = []

    for g in genre: album[g] = 0

    for i in range(len(genres)):
        album[genres[i]] += plays[i]
        play[i] = (genres[i], plays[i])

    albumrank = dict(sorted(album.items(), key=lambda x:x[1], reverse=True))

    play = sorted(play, key=lambda x:list(play.values())[x][1], reverse=True)
    print("album:",albumrank, "play",play)

    for a in albumrank:
        cnt = 0
        for p in play:
            if a == genres[p]:
                best.append(p)
                cnt += 1
            if cnt >= 2: break
    print(best)
    return best


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 500, 2500])
solution(["classic", "pop", "classic", "classic", "pop", "jazz"], [500, 600, 150, 800, 2500, 30000])