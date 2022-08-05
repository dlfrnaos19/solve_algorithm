def solution(phone_book):
    hash_map = {}
    for phone_num in phone_book:
        hash_map[phone_num] = 0
    for phone_num in phone_book:
        temp = ""
        for num in phone_num:
            temp+=num
            if temp in hash_map and temp != phone_num:
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
