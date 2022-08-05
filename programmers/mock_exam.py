def solution(answers):
    first_supoza = [1,2,3,4,5,]
    second_supoza = [2,1,2,3,2,4,2,5,]
    third_supoza = [3,3,1,1,2,2,4,4,5,5,]
    length = len(answers)
    first_sol_list = first_supoza * ((length // len(first_supoza))+1)
    second_sol_list = second_supoza * ((length // len(second_supoza))+1)
    third_sol_list = third_supoza * ((length // len(third_supoza))+1)
    
    first_count = 0
    second_count = 0
    third_count = 0
    for supo_answer1, supo_answer2, supo_answer3, answer in zip(first_sol_list[:length],second_sol_list[:length],third_sol_list[:length], answers):
        if supo_answer1 == answer:
            first_count+=1
        if supo_answer2 == answer:
            second_count+=1
        if supo_answer3 == answer:
            third_count+=1
    
    result = [first_count, second_count, third_count]
    tuple_result = [(1,first_count), (2,second_count), (3, third_count)]
    answer = []
    for num, counter in tuple_result:
        if counter == max(result):
            answer.append(num)
    if len(answer) > 1:
        answer.sort()
    
    return answer

# 다른 사람의 풀이
# 패턴만 적용해서 푼게 인상적이고, 공간절약 훨씬 잘한 듯
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result