# 0422(화)
# 게리 맨더링(골드3)
from itertools import combinations

def solution():
    min_v = float('inf')    # 최솟값의 차이 찾을 변수


N = int(input())        # 구역의 개수
people = list(map(int, input().split()))    # 각 구역별 인구수


adj_list = [[] for _ in range(N+1)]
for i in range(1, N+1):
    info = list(map(int, input().split()))
    print(info)
    for j in range(info[0]):
        adj_list[i].append(info[j+1])
        

print(adj_list)


