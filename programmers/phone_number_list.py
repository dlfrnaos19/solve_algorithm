def solution(phone_book):
    hash_map = set(phone_book)
        
    for num in phone_book:
        temp = ""
        for char in num:
            temp += char
            if temp in hash_map and temp != num:
                return False

    return True

# 다른 사람 풀이
# string에 sort를 적용한 문제 풀이
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True
