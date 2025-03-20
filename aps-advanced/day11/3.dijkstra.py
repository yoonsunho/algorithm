import sys
sys.stdin = open("graph2.txt", "r")
import heapq

def dijkstra(st_node):
    pq =[(0, st_node)]  # (누적거리, 노드 번호)

    dists = [INF] * V   # 각 정점까지의 (누적)최단 거리를 저장할 리스트
    dists[st_node] = 0  # 시작노드 최단 거리는 0

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 pass
        # 에제 그림: 로 가는 경로가 3 or 4
        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]    # 다음 노드로 가기위한 가중치
            next_node = next_info[1]    # 다음 노드 번호
            
            # 다음 노드로 가기 위한 누적 거리
            new_dist = dist + next_dist

            # 이미 같은 가중치 이거나, 더 작은 가중치로 온 적이 있다면 continue(같아도 볼 필요 없음)
            if new_dist >= dists[next_node]:
                continue

            # next_node 까지 도착하는데 비용은 new_dist
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists

INF = int(21e8)     # 21억(무한대를 의미한다 가정)

V, E = map(int, input().split())    # 노드 수, 간선 수
start_node = 0  # 문제에 따라 다름

graph = [[] for _ in range(V)]  # 인접 리스트로 구현

for _ in range(E):
    u,v,w = map(int, input().split())

    graph[u].append((w,v))  # 단방향 그래프!!
    
# 0 에서 출발하여 다른 노드들 까지의 최단 거리를 모두 구한다
result_dists = dijkstra(0)
print(result_dists)     # [0, 2, 3, 9, 6, 10]