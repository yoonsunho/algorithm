import sys
sys.stdin = open("txt/1861.txt", "r")

di = [0,1,0,-1]
dj = [1,0,-1,0]

def dfs(i, j, cnt):
    global max_cnt

    max_cnt = max(max_cnt, cnt)

    for x in range(4):
        ni, nj = i + di[x], j + dj[x]
        if 0 <= ni < N and 0 <= nj < N:
            if matrix[ni][nj]-matrix[i][j] == 1:
                visited[ni][nj] = 1
                dfs(ni, nj, cnt+1)
                visited[ni][nj] = 0





T = int(input())
for tc in range(1, T+1):

    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    # print(matrix)
    visited = [[0]*N for _ in range(N)]
    # print(visited)
    max_cnt = 0     # 최대 이동 경로
    dfs(0, 0, 1)

    print(f'#{tc}')