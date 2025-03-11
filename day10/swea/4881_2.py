import sys
sys.stdin = open("txt/4881.txt","r")

# dfs이용한 풀이(순열 x)
def dfs(i,N,s):

    global min_v

    if i == N:  # 배열의 끝까지 순회
        min_v = min(min_v, s)

    elif s > min_v:
        return

    for col in range(N):
        if visited[col] == 0:   # 아직 방문하지 않았다면
            visited[col] = 1
            dfs(i+1, N, s + arr[i][col])
            visited[col] = 0


T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0]* N
    min_v = 100
    s = 0   # 합을 담을 변수

    dfs(0, N, s)

    print(f'#{tc} {min_v}')
