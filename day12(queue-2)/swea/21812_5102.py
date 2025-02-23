import sys
sys.stdin = open("txt/5102.txt", "r")

def bfs(s,e,V):
    q = []
    visited = [0] * (V+1)
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        if t == e:
            return visited[e] - visited[s]
        for w in adj_l[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1

    return 0




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    V, E = map(int, input().split())    # 5<=V=50, 4<=E<=1000


    adj_l = [[] for _ in range(V+1)]
    for _ in range(E):
        v, w = map(int, input().split())
        adj_l[v].append(w)
        adj_l[w].append(v)

    st, end = map(int, input().split())

    ans = bfs(st, end, V)



    print(f'#{test_case} {ans}')