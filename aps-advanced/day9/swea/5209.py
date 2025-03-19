import sys
sys.stdin = open("txt/5209.txt", "r")

def dfs(i, total):

    global min_price

    # 가지치기
    if total >= min_price:
        return

    if i == N:
        min_price = min(min_price, total)
        return

    for row in range(N):
        if visited[row] == 0:
            visited[row] = 1
            dfs(i+1, total + product[row][i])
            visited[row] = 0



T = int(input())
for tc in range(1, T+1):

    N = int(input())    # N종의 제품, N 곳의 공장(3<=N<=15)

    product = [list(map(int, input().split())) for _ in range(N)]   # 공장 별 생산 비용

    visited = [0] * N   # 공장별로만 할것임

    min_price = 1501
    dfs(0,0)
    


    print(f'#{tc} {min_price}')