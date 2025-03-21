import sys
sys.stdin = open("txt/4012.txt", "r")

def get_cenergy(li):
    total = 0

    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            total += (food_mix[li[i]][li[j]] + food_mix[li[j]][li[i]])

    return total

def make_list():

    A, B = [], []

    for i in range(N):
        if visited[i]:
            A.append(i)
        else:
            B.append(i)

    return get_cenergy(A), get_cenergy(B)

def dfs(start, cnt):
    global ans

    if cnt == N//2:
        a_tot, b_tot = make_list()
        ans = min(ans, abs(a_tot - b_tot))
        return

    # visited[cnt] = 1

    for i in range(start, N):
        if visited[i]:
            continue

        visited[i] = 1
        dfs(i+1, cnt+1)
        visited[i] = 0

T = int(input())
for tc in range(1, T+1):

    N = int(input())

    food_mix = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N

    ans = float('inf')

    dfs(0, 0)

    print(f'#{tc} {ans}')