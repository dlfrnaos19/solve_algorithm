def solution(s):
    len_list = []
    phrase = ""
    
    if len(s) == 1:
        return 1
    
    for step in range(1, len(s) //2 + 1):
        count = 1
        char = s[:step]
        for i in range(step, len(s), step):
            if s[i:i+step] == char:
                count += 1
            else:
                if count == 1:
                    count = ""
                phrase += str(count) + char
                char = s[i:i+step]
                count = 1
        if count == 1:
            count = ""
        phrase += str(count) + char
        len_list.append(len(phrase))
        phrase = ""
    return min(len_list)