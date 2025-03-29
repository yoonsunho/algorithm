import sys
sys.stdin = open("txt/5189.txt", "r")

def recur(n,total,cnt):

    global min_v

    if cnt == N-1:
        min_v = min(min_v, total + matrix[n][0])
        return

    if min_v < total:
        return

    for i in range(N):
        if visited[i]:  # 이미 방문 했다면 넘어가기
            continue
        visited[i] = 1
        recur(i, total + matrix[n][i], cnt+1)
        visited[i] = 0



T = int(input())

for tc in range(1, T+1):

    N = int(input())    # 관리 구역(N * N)

    matrix = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    visited[0] = 1
    # result = 0
    min_v = float('inf')
    recur(0, 0, 0)

    print(f'#{tc} {min_v}')