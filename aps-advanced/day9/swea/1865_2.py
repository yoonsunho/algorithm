import sys
sys.stdin = open("txt/1865.txt", "r")

# 시간 오래 검림

def dfs(i, total):
    global max_percent

    # 가지 치기
    if total == 0:
        return

    if total < max_percent:
        return


    if i == N:
        # print(total)
        max_percent = max(max_percent, total)
        return

    for col in range(N):
        if visited[col] == 0:
            visited[col] = 1
            dfs(i +1, total*percent[i][col]*0.01)
            visited[col] = 0

T = int(input())
for tc in range(1, T+1):

    N = int(input())

    percent= [list(map(int,input().split())) for _ in range(N)]

    visited = [0] * N

    max_percent = 0
    dfs(0,1)

    # print(max_percent)
    # print(round(max_percent*100,6))
    # print(max_percent.6f)
    # print("{:.6f}".format(max_percent*100))

    print(f'#{tc}' " {:.6f}".format(max_percent*100))