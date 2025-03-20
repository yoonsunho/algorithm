# prim
# - 특정 정점 기준으로 시작
# - 갈 수 잇는 노드들 중 가중치가 가장 작은 노드부터 고르자
# -> 그냥 큐가 아닌 우선순위 큐를 활용하면 좋다

# 우선순위큐:  투플의 첫번째 요소로 가중치 사용 (첫번째 요소 값이 작은게 우선)
import sys
sys.stdin = open("graph.txt", "r")

def prim(st_node):
    pq = [(0, st_node)]     # 시작점은 가중치가 0
    MST = [0]*V     # visited랑 동일
    min_wei = 0     # 최소 비용 저장

    while pq:

        wei, node = heapq.heappop(pq)

        # 이미 방문한 노드를 뽑았다면 continue
        if MST[node]:
            continue

        MST[node] = 1   # 방문 처리
        min_wei += wei  # 누적 합 추가

        for next_node in range(V):

            # 갈 수 없으면 pass
            if graph[node][next_node] == 0:
                continue
                
            # 이미 방문 완료
            if MST[next_node]:
                continue

            heapq.heappush(pq,(graph[node][next_node], next_node))

    return min_wei

import heapq

V, E = map(int,input().split())     # 정점수, 간선수
graph = [[0]* V for _ in range(V)]      # 인접 행렬
                                        # [선택과제] 인접 리스트로 구현

for _ in range(E):
    st, end, wei = map(int,input().split())
    graph[st][end] = wei
    graph[end][st] = wei

result = prim(4)     # 출발 정점을 바꾸어도 동일하다.

print(f'최소비용 = {result}')   # 최소비용 = 175