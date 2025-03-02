import sys
sys.stdin = open("txt/21649.txt", "r")


def bfs(v,n):
    visited = [0] * (n+1)
    stack = []      # 과거 방문기록을 조회하기 위함
    result = []     # 결과를 담을
    
    while True:
        if visited[v] == 0:     # 방문하지 않았다면
            visited[v] = 1
            result.append(v)
        for w in adj_list[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return result

for tc in range(1, 2):

    V, E = map(int, input().split())        # 정점의 개수, 간선의 개수

    arr = list(map(int, input().split()))

    adj_list = [[] for _ in range(V+1)]
    for i in range(E):
        m, n = arr[2*i], arr[2*i+1]
        adj_list[m].append(n)
        adj_list[n].append(m)

    ans = bfs(1,V)

    print(f'#{tc} {"-".join(map(str,ans))}')