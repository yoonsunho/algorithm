import sys
sys.stdin = open("txt/5189.txt", "r")

T = int(input())

def recur(loc, cnt, total):    # 중복이 없고, 본인인덱스에 자기자신이 아닌 순열 만들기

    global min_v

    if cnt == N-1:
        min_v = min(min_v, total+golf_zone[loc][0])
        return

    elif total > min_v:
        return

    for i in range(1, N):
        if visited[i] == 0:
            visited[i] = 1
            recur(i, cnt + 1, total + golf_zone[loc][i])
            visited[i] = 0


for tc in range(1, T+1):

    N = int(input())        # 3 <= N <= 10

    golf_zone = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N

    min_v = 1000

    recur(0, 0, 0)
    # print(min_v)

    print(f'#{tc} {min_v}')