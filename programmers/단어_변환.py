def trans(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    cnt = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]: cnt+=1
    if cnt == len(str1)-1: return True
    else: return False

mincnt = 100
def dfs(word, target, words, count):
    global mincnt
    if trans(word, target) or not words:
        mincnt = min(mincnt, count)
        return


    for w in words:
        if trans(word, w):
            words.remove(w)
            dfs(w, target, words, count+1)
        else: continue


def solution(begin, target, words):
    if not target in words: return 0
    else: dfs(begin, target, words, 1)

    return mincnt


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
solution("aab", "aba", ["abb", "aba"])