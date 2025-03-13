import sys
sys.stdin = open("txt/1861.txt", "r")

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(i, j, cnt):
    global max_cnt

    max_cnt = max(max_cnt, cnt)
    # visited[(i, j)] = 1

    for x in range(4):
        ni, nj = i + di[x], j + dj[x]
        if 0 <= ni < N and 0 <= nj < N and visited[(ni, nj)] != 1:
            if matrix[ni][nj]-matrix[i][j] == 1:
                visited[(ni, nj)] = 1
                dfs(ni, nj, cnt+1)
                visited[(ni, nj)] = 0
            # if matrix[ni][nj]-matrix[i][j] != 1:
            #     max_cnt = max(max_cnt, cnt)


T = int(input())
for tc in range(1, T+1):

    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    # print(matrix)
    visited = {}
    for i in range(N):
        for j in range(N):
            visited[(i, j)] = 0
    # print(visited)
    max_cnt = 0     # 최대 이동 경로

    for i in range(N):
        for j in range(N):
            visited[(i, j)] = 1  # 시작 위치 방문 표시
            dfs(i, j, 1)
            visited[(i, j)] = 0  # 시작 위치 초기화
    # print(max_cnt)
    print(f'#{tc} {max_cnt}')