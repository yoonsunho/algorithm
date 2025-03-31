import heapq

def prim(cnt,st_node):  # 이동 간선의 수, 시작 정점

    pq = [(cnt, st_node)]   # 최소 비용, 시작정점의 좌표
    visited[st_node] = 1
    # print(visited)

    while pq:

        dist, node = heapq.heappop(pq)
        visited[node] = 1
        cnt += 1

        if cnt == N:    # 간선 수가 N이 되면 종료
            # print(visited)
            # print(dist)
            return dist
            break

        for x in concent:

            if visited[x]:
                continue

            new_dist = abs(x[0]-node[0]) + abs(x[1]-node[1])
            new_node = x

            next_dist = dist + new_dist
            heapq.heappush(pq, (next_dist, new_node))



T = int(input())    # 3<=T<=10
for tc in range(1, T+1):

    N = int(input())    # 콘센트의 개수 1<=N<=10
    concent = []    # 컨센트들의 좌표
    visited = {}
    # concent.append((0, 0))

    for _ in range(N):
        x, y = map(int, input().split())
        concent.append((x, y))
        visited[(x, y)] = 0

    concent.sort(key=lambda x: x[0]+x[1])
    # print(concent)
    # print(visited)
    ans = prim(0, concent[0])


    print(f'#{tc} {ans}')