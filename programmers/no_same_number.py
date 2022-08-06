
def solution(arr):
    answer = []
    num = -1
    for i in arr:
        if i != num:
            num = i
            answer.append(i)
        
    return answer