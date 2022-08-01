def solution(record):
    # uuid를 담기 위한 딕셔너리
    uuid_dict = {}
    # 마지막까지 uuid당 닉네임 체크
    for rec in record:
        if len(rec.split()) == 3:
            uuid_dict[rec.split()[1]] = rec.split()[2]
    
    # Enter, Leave만 식별하고, 메세지 생성 후 result에 추가
    result = []
    for rec in record:
        if rec.startswith("Enter"):
            result.append(uuid_dict[rec.split()[1]] + "님이 들어왔습니다.")
        elif rec.startswith("Leave"):
            result.append(uuid_dict[rec.split()[1]] + "님이 나갔습니다.")
        
    return result

# 다른 사람 첫번째 풀이
# def solution(record):
#     answer = []
#     namespace = {}
#     printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
#     for r in record:
#         rr = r.split(' ')
#         if rr[0] in ['Enter', 'Change']:
#             namespace[rr[1]] = rr[2]

#     for r in record:
#         if r.split(' ')[0] != 'Change':
#             answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

#     return answer