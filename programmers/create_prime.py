import math
from itertools import combinations

def solution(nums):
    
    def is_prime(num):
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    
    count = 0
    for i in combinations(nums,3):
        number = sum(i)
        if is_prime(number):
            count+=1
    
    return count

# 다른 사람의 풀이

# def solution(nums):
#     from itertools import combinations as cb
#     answer = 0
#     for a in cb(nums, 3):
#         cand = sum(a)
#         for j in range(2, cand):
#             if cand%j==0:
#                 break
#         else:
#             answer += 1
#     return answer