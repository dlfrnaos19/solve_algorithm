from collections import deque
import sys
# sys.stdin.readline() 쓰지 않으면 시간 초과 뜸
bag_capa, n_goods = map(int, sys.stdin.readline().split())
goods_list = []
total_goods_weight = 0
# 보석 무게와 가격을 리스트에 튜플로 저장
for _ in range(n_goods):
    goods_weight, price = map(int, sys.stdin.readline().split())
    goods_list.append((goods_weight,price))
    total_goods_weight += goods_weight
# 가격을 기준으로 내림차순으로 정렬(제일 비싼 보석이 앞에 오도록)
goods_list.sort(key=lambda x: x[1],reverse=True)
goods_deque = deque(goods_list)
# 가방 무게보다 보석양이 적으면 계산할 필요도 없이 다 담음    
result = 0
if total_goods_weight <= bag_capa:
    for weight, price in goods_list:
        result += weight * price
    print(result)
# 가방 무게 다찰 때 까지 담고자 하는 보석을 차례대로 삭제하면서 가격을 계산
else:
    while bag_capa != 0:
        weight, price = goods_deque.popleft()
        if bag_capa >= weight:
            bag_capa -= weight
            result += weight * price
        else:
            result += bag_capa * price
            bag_capa = 0
    print(result)
