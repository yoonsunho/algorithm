import sys
sys.stdin = open("txt/1861.txt", "r")

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 내 풀이 but 시간 너무 오래걸림

def dfs(i ,j, cnt):
    global max_v

    for x in range(4):
        ni = i + di[x]
        nj = j + dj[x]
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] - matrix[i][j] == 1:
            dfs(ni, nj, cnt+1)

    max_v = max(max_v, cnt)


T = int(input())
for tc in range(1, T+1):

    N = int(input())    # N * N 배열 (1 ≤ N ≤ 10^3)

    matrix = [list(map(int, input().split())) for _ in range(N)]
    dp = [[1]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            max_v = 0
            dfs(i, j, 1)
            dp[i][j] = max_v

    max_result = max(max(row) for row in dp)
    path =[]    # 최댓값이 놓이는 후보를 답을 리스트
    # print(max_result)
    for i in range(N):
        for j in range(N):
            if dp[i][j] == max_result:
                path.append(matrix[i][j])
    # print(path)




    print(f'#{tc} {min(path)} {max_result}')