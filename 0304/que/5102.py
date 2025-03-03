import sys
sys.stdin = open("txt/5102.txt", "r")

def bfs(i,j,n):     # 시작점 정점개수

    visited = [0]*(n+1)
    q = []
    q.append(i)
    visited[i] = 1
    while q:
        t = q.pop(0)
        if t == j:
            return visited[j] - visited[i]
        for w in adj_list[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    return 0

T = int(input())
for tc in range(1,T+1):

    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]

    for _ in range(E):
        v, w = map(int,input().split())
        adj_list[v].append(w)
        adj_list[w].append(v)

    st, end = map(int, input().split())

    ans = bfs(st, end, V)

    print(f'#{tc} {ans}')
