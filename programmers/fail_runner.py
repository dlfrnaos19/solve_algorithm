from collections import Counter

def solution(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    result = p_counter - c_counter
    # most_common은 1개 남은 dict 정보를 List tuple로 반환
    # 여기에서 필요한 건 key 정보로, List 한번, tuple 한번 인덱싱
    return result.most_common(1)[0][0]

# 다른 사람 풀이
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer