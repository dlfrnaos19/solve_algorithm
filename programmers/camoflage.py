from collections import defaultdict

def solution(clothes):
    hash_map = defaultdict(list)
    
    for cloth, category in clothes:
        hash_map[category].append(cloth)
        
    for i in hash_map.keys():
        hash_map[i].append(None)
    
    result = 1
    for i in hash_map.values():
        result *= len(i)
    result = result - 1
    return result