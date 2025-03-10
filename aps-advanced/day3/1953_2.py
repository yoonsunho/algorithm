import sys
from collections import deque
sys.stdin = open("txt/1953.txt", "r")

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 터널의 타입 별 뚫린 위치
types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

def bfs(r, c):
    # print(r,c)

    q = deque([[r, c]])
    visited[r][c] = 1   # 맨 홀 시작위치 방문한걸로 바꿔주기

    while q:

        now_i, now_j = q.popleft()  # 현 위치 갱신
        dirs = types[graph[now_i][now_j]]

        for i in range(4):      # 4 방향 탐색

            # 출구가 안열려 있는 경우 pass
            if dirs[i] == 0:
                continue

            nexti, nextj = now_i + di[i], now_j + dj[i]

            # 범위 밖이면 pass
            if nexti < 0 or nexti >= N or nextj < 0 or nextj >= M:
                continue

            # 이미 방문을 했었다면 pass
            if visited[nexti][nextj]:
                continue

            # 터널이 없으면 pass
            if graph[nexti][nextj] == 0:
                continue

            # 다음위치의 터널 방향
            next_dirs = types[graph[nexti][nextj]]

            # 터널의 뚫린위치 확인
            if i % 2 == 0 and next_dirs[i+1] == 0:
                continue

            if i % 2 == 1 and next_dirs[i-1] == 0:
                continue

            if visited[nexti][nextj] > L:
                break

            visited[nexti][nextj] = visited[now_i][now_j] + 1
            q.append([nexti, nextj])

T = int(input())

for tc in range(1, T+1):

    N, M, R, C, L = map(int, input().split())       # 세로, 가로, 맨홀 세로, 맨홀 가로, 소요시간

    graph = [list(map(int, input().split())) for _ in range(N)]     # 터널의 정보를 담을 matrix
    # print(graph)

    visited = [[0] * M for _ in range(N)]        # 방문의 여부를 담을 새로운 배열

    bfs(R, C)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')