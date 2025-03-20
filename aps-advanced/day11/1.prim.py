# prim
# - 특정 정점 기준으로 시작
# - 갈 수 잇는 노드들 중 가중치가 가장 작은 노드부터 고르자
# -> 그냥 큐가 아닌 우선순위 큐를 활용하면 좋다
import sys
sys.stdin = open("graph.txt", "r")

def prim(st_node):
    pq = [(0, st_node)]     # 시작점은 가중치가 0
    MST = [0]*V     # visited랑 동일
    min_wei = 0

    while pq:

        wei, node = heapq.heappop(pq)

        # 이미 방문한 노드를 뽑았다면 continue
        if MST[node]:
            continue

        MST[node] = 1
        min_wei += wei

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

V, E = map(int,input().split())
graph = [[0]* V for _ in range(V)]

for _ in range(E):
    st, end, wei = map(int,input().split())
    graph[st][end] = wei
    graph[end][st] = wei

result = prim(0)

print(f'최소비용 = {result}')   # 최소비용 = 175