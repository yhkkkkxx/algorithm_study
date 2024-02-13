def solution(s):
    answer = 0
    bracket = ['()','{}','[]'] * (len(s)//2)


    if len(s) %2 == 1:
        return 0
    else:
        for i in range(len(s)): #rotate
            bstr = s

            for b in bracket:
                if bstr.count(b) > 0:
                    bstr = bstr.replace(b, '')
                if bstr == '': break


            s = s[1:]+s[0]
            if bstr == '':
                answer += 1
                continue

        return answer


solution("[](){}")
solution("}]()[{")
solution("[)(]")
solution("}}}")