# 4*4 N Queen 문제
# - (i, j) 좌표에 queen 을 놓은 적이 있다
# visited 기록 방법
#       - 1. 이차원 배열
#       - 2. 일차원 배열로 효울적으로 하는 방법

def check(row,col):
    # 1. 같은 열에 놓은 적이 있는가
    for i in range(row):
        if visited[i][col]:
            return False

    # 2. 왼 대각(\)
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # [참고]
    # for i, j in zip(range((row-1,-1,-1)), range(col-1,-1,-1)):
    #     if visited[i][j]:
    #         return False

    # 3. 우 대각(/)
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        # 가지 치기
        if visited[i][j]:
            return False
        i -= 1
        j += 1



# level:  N개의 행에 모두 놓았다
# branch: N개의 열
def dfs(row):
    global answer
    if row == N:
        answer += 1
        return

    # 후보군 : N 개의 얄
    for col in range(N):
        if check(row,col) is False:      # if 기존에 같은 열이나 대각선에 놓았다면 ㅇ안된다!:
            continue
        visited[row][col] = 1
        dfs(row+1)
        visited[row][col] = 0

N = 4
visited = [[0]*N for _ in range(N)]
answer = 0
dfs(0)
print(answer)   # 256


