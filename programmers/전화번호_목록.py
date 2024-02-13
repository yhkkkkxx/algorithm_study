def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break
    print(answer)
    return answer


solution(["119", "97674223", "1195524421"])
solution(["123", "456", "789"])
solution(["12", "123", "1235", "567", "88"])
solution(["0", "119"])
solution(["11", "21", "3523", "2431", "1191", "2"])