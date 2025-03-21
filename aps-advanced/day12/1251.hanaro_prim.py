import sys
sys.stdin = open("txt/1251.txt", "r")

import heapq

def prim():

    pq = [(0, 0)]   # (비용, 노드)
    visited = [0] * N
    # visited[0] = 1
    min_cost = 0

    # 최적화 하기 위해 ( heappush 할 때 최소 비용 산정 됐음에도 불구하고 더 많은 비용 나오는애는 애초에 push 안하게 하주기
    dists = [float('inf')]* N  # 최소 비용 저장 리스트
    dists[0] = 1    # 시작점 비용은 0
    # print(dists)

    while pq:
            
        # cost가 저렴한 후보부터 나온다
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue
        
        visited[node] = 1   # 방문완료 처리
        min_cost += cost

        for next_node in range(N):
            if visited[next_node]:
                continue

            new_cost = ((x_li[next_node]-x_li[node])**2+(y_li[next_node]-y_li[node])**2)*E

            # 우선순위 큐에 삽입된 거리를 저장하면서 진행
            # - 더 작은 비용으로 갈 수 있을 때만 haepq에 삽입
            if new_cost < dists[next_node]:     # 최적화 해주기
                dists[next_node] = new_cost     # 비용 갱신
                heapq.heappush(pq, (new_cost, next_node))

    return round(min_cost)

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    x_li = list(map(int, input().split()))
    y_li = list(map(int, input().split()))
    E = float(input())

    edges = []
    for i in range(N):
        edges.append((x_li[i], y_li[i]))
    # print(edges)

    ans = prim()

    print(f'#{tc} {ans}')