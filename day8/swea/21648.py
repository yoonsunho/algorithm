import sys
sys.stdin = open("txt/21648.txt", "r")

def check(i,j,N):
    visited = [0] * (N+1)
    stack = []

    while True:
        if visited[i] == 0:
            visited[i] = 1
        for w in adj_list[i]:
            if visited[w] == 0:
                stack.append(i)
                i = w
                break
        else:
            if stack:
                i = stack.pop()
            else:
                 break

    if visited[j] == 1:
        return 1
    else:
        return 0



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    V, E = map(int,input().split())     #  5≤V≤50, 4≤E≤1000

    spots = [list(map(int, input().split())) for _ in range(E)]
    st, end = map(int, input().split())

    adj_list = [[] for _ in range(V+1)]

    for i in range(E):
        v, w = spots[i][0], spots[i][1]
        adj_list[v].append(w)
        # adj_list[w].append(v) # 경로에 방향성 있으므로 쓰면 안됨

    ans = check(st,end,V)

    print(f'#{test_case} {ans}')