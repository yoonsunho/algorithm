# 04/22(화)
# 파이프 옮기기 1(골드5)

# 시간초과.. -> dp를 이요하라는 것....
'''
최적화 핵심 포인트

'''
dir = [[[0, 1], [1, 1]],        # 가로일 떄 갈 수 있는 방향
       [[1, 0], [1, 1]],        # 세로일 때 갈 수 있는 방향
       [[0, 1], [1, 1], [1, 0]]]    # 대각선 일 떄 갈 수 있는 방향


def dfs(st_i, st_j, d):

    # global count

    if st_i == (N-1) and st_j == (N-1):
        return 1
        # count += 1
        # return

    if dp[st_i][st_j][d] != -1:
        return dp[st_i][st_j][d]

    count = 0
    for di, dj in dir[d]:
        ni = st_i + di
        nj = st_j + dj
        if 0 <= ni < N and 0 <= nj < N:

            if matrix[ni][nj] == 1:     # 벽 만났을 때 제외
                continue

            if di == 0 and dj == 1:     # 현 방향이 가로일 떄
                next_d = 0
            elif di == 1 and dj == 0:   # 현 방향이 세로일 때
                next_d = 1
            elif di == 1 and dj == 1:   # 현 방향이 대각선일 때
                if matrix[st_i+1][st_j] == 1 or matrix[st_i][st_j+1] == 1:  # 대각선일땐 3칸 안되니까 추가조건
                    continue
                next_d = 2
            count += dfs(ni, nj, next_d)

    dp[st_i][st_j][d] = count
    return count


N = int(input())        # 집의 크기
matrix = [list(map(int, input().split())) for _ in range(N)]

count = 0       # 갈 수 있는 방법의 수를 담을 변수
dp = [[[-1]*3 for _ in range(N)] for __ in range(N)]
ans = dfs(0, 1, 0)
print(ans)