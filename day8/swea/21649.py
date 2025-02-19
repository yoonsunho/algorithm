import sys
sys.stdin = open("txt/21649.txt", "r")

def dfs(v,n):       # v는 현 위치, n은 총 정점 개수
    visited = [0] * (n+1)
    result = []
    stack = []

    while True:
        if visited[v] == 0:
            visited[v] = 1
            result.append(v)
        for w in adj_list[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()     # v 에 pop한 6넣어주기 그러면 다시 돌아가서 6의 인접 요소가 있는지 탐색하게 됨
            else:
                return result

T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    V, E = map(int, input().split())    # 정점의 개수(V)와 간선의 개수(E)

    spots = list(map(int, input().split()))       # 연결 정점들

    # 인접한 리스트들
    adj_list = [[] for _ in range(V+1)]

    for i in range(E):
        v, w = spots[i*2], spots[2*i+1]
        adj_list[v].append(w)
        adj_list[w].append(v)

    ans = dfs(1, V)
    # print(ans)
    print(f'#{test_case} {"-".join(map(str,ans))}')