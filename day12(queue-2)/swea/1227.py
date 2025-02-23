import sys
sys.stdin = open("txt/1227.txt", "r")

def bfs(i,j):
    q = []
    visited = [[0]*100 for _ in range(100)]
    q.append([i, j])
    visited[i][j] = 1
    while q:
        ti, tj = q.pop(0)
        if maze[ti][tj] == 3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti + di, tj + dj
            if 0 <= wi < 100 and 0 <= wj < 100 and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = 1
    return 0


def find_start():
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                return i, j

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, T + 1):

    tc = input()

    maze = [list(map(int, input())) for _ in range(100)]  # 미로 배열

    sti, stj = find_start()

    ans = bfs(sti, stj)



    print(f'#{tc} {ans}')