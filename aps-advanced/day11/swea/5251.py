import sys
sys.stdin = open("txt/5251.txt", "r")
import heapq

def dijkstra(st_node):

    pq = [(0, st_node)]
    dists = [INF] * (N+1)
    dists[st_node] = 0

    while pq:

        dist, node = heapq.heappop(pq)

        # dist 보다 크거나 같으면 pass
        if dists[node] < dist:
            continue
        # print(dists)
        # print(graph[node])
        for next_info in graph[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = dist + next_dist

            if new_dist >= dists[next_node]:
                continue

            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists

T = int(input())
for tc in range(1, T+1):

    N, E = map(int, input().split())     # 연결지점 0~N, 간선의 개수 E(1<=N,)

    graph = [[] for _ in range(N+1)]    ###### 여기 노드 수 넣어야함 주의!!!!!
    INF = int(21e8)

    for _ in range(E):
        st, e, wei = map(int, input().split())
        graph[st].append((wei, e))

    # print(graph)
    ans = dijkstra(0)
    # print(ans[N])


    print(f'#{tc} {ans[N]}')