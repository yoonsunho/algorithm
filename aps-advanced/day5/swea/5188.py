import sys
sys.stdin = open("txt/5188.txt", "r")

di = [0, 1]
dj = [1, 0]

def recur(i,j,N,total):
    global min_v
    # 현재 (갱신된 위치 방문 표시 해주기)
    visited[i][j] = 1

    #종료 조건
    if (i == N-2 and j == N-1) or (i == N-1 and j == N-2):
        # print(path)
        min_v = min(min_v, total)
        return

    elif total > min_v:
        return

    for x in range(2):
        wi, wj = i + di[x], j + dj[x]
        if 0 <= wi < N and 0 <= wj < N and visited[wi][wj] == 0:    # 범위 안에 있고 아직 방문하지 않았다면
            visited[wi][wj] = 1
            path.append([wi, wj])
            recur(wi, wj, N, total + maze[wi][wj])
            visited[wi][wj] = 0
            path.pop()


T = int(input())
for tc in range(1, T+1):

    N = int(input())    # N x N 배열

    maze = [list(map(int, input().split())) for _ in range(N)]

    min_v = 10000
    path = []
    visited = [[0] * N for _ in range(N)]
    # print(visited)
    visited[0][0] = 1
    recur(0, 0, N, maze[0][0])

    # print(min_v+maze[N-1][N-1])

    print(f'#{tc} {min_v+maze[N-1][N-1]}')