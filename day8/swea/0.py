import sys
sys.stdin = open("txt/21649.txt", "r")


def dfs(v, N):
    visited = [0] * (N + 1)
    stack = []
    lst = []

    while True:
        if visited[v] == 0:
            visited[v] = 1
            lst.append(v)
        for w in graph[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:       # 위에서 break가 걸리지 않을 때 실행 ( v가 5일때
            if stack:
                v = stack.pop()
            else:
                return lst


tc = 1
V, E = map(int, input().split())
lst = list(map(int, input().split()))

graph = [[] for _ in range(V + 1)]

for i in range(E):
    graph[lst[i * 2]].append(lst[i * 2 + 1])
    graph[lst[i * 2 + 1]].append(lst[i * 2])

print(f"#{tc}", '-'.join(map(str, (dfs(1, V)))))