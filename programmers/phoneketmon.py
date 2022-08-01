
def solution(nums):
    length = len(nums)
    # 고를 수 있는 최대 개체 수
    n_max = length//2
    # 고를 수 있는 최대 타입 수
    n_type = len(set(nums))
    # nums가 1 이상으로, 1인 경우 리턴
    if length == 1:
        return 1
    # 타입이 다양하므로, 고를 수 있는 만큼 고르면 됨
    if n_max <= n_type:
        return n_max
    # 타입이 별로 없으므로, 타입만큼만 고름
    elif n_max > n_type:
        return n_type

# 프로그래머스 다른 사람 풀이
# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))