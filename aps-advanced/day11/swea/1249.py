import sys

sys.stdin = open("txt/1249.txt", "r")
import heapq

# 품

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
INF = int(21e8)


def dijkstra(st_i, st_j):
    pq = [(0, st_i, st_j)]  # 누적 비용, 시작 인덱스
    dists = [[INF] * N for _ in range(N)]  # 이차원배열로 각 지점별 누적 최소 비용 담을 리스트
    dists[st_i][st_j] = 0  # 시작지점 비용 = 0

    while pq:

        dist, s_i, s_j = heapq.heappop(pq)

        # 이미 더 작은 비용으로 온적이 있다면 pass
        if dists[s_i][s_j] < dist:
            continue

        for i in range(4):

            # 범위 밖이면 pass
            if s_i + di[i] < 0 or s_i + di[i] >= N:
                continue
            if s_j + dj[i] < 0 or s_j + dj[i] >= N:
                continue

            # 복구가 필요하면
            if int(hei[s_i+di[i]][s_j+dj[i]]) > 0:
                next_dist = int(hei[s_i+di[i]][s_j+dj[i]])
            else:
                next_dist = 0

            # 다음 위치 갱신
            next_i, next_j = s_i + di[i], s_j + dj[i]

            # 거리 누적 합으로 갱신
            new_dist = dist + next_dist

            # 원래 dists 에 저장된 이동거리 보다 길거나 같으면 pass
            if new_dist >= dists[next_i][next_j]:
                continue

            # 다음 지점까지 가는데 드는 비용 = new_dist
            dists[next_i][next_j] = new_dist
            heapq.heappush(pq, (new_dist, next_i, next_j))

    return dists


T = int(input())
for tc in range(1, T + 1):

    N = int(input())  # 가로 세로 칸 수 3<=N<=100
    hei = [list(input()) for _ in range(N)]
    # print(hei)

    ans_list = dijkstra(0, 0)
    # print(ans_list)

    print(f'#{tc} {ans_list[N - 1][N - 1]}')