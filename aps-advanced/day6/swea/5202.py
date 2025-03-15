import sys

sys.stdin = open("txt/5202.txt", "r")


def recur(cnt, start):
    global N

    if start == N:
        # print(cnt)
        return cnt

    for i in range(start + 1, N):
        if time[start][1] <= time[i][0]:
            return recur(cnt + 1, i)

    return cnt


T = int(input())
for tc in range(1, T + 1):

    N = int(input())

    time = [[] * N for _ in range(N)]
    # print(time)

    for i in range(N):
        st, end = map(int, input().split())
        time[i] = [st, end]

    time.sort(key=lambda x: x[1])
    print(time)

    result = recur(1, 0)

    print(f'#{tc} {result}')


    def mini_sum(arr):
        sum(arr)
