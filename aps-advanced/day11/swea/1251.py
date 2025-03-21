import sys
sys.stdin = open("txt/1251.txt", "r")

# 못품.. 모르겠음
# day12 수업시간 풀이 참고

import heapq

INF = int(21e8)

def prim(st_node):

    pq = [(0, st_node[0], st_node[1])]
    MST = [INF] * N

    while pq:

        cost, st_x, st_y = heapq.heappop(pq)

        for next_info in edges:
            pass

T = int(input())
for tc in range(1, T+1):

    N = int(input())

    x_li = list(map(int, input().split()))
    y_li = list(map(int, input().split()))
    E = float(input())

    edges = []
    for i in range(N):
        edges.append((x_li[i], y_li[i]))
    print(edges)

    prim(edges[0])

    print(f'#{tc}')