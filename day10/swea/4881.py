import sys
sys.stdin = open("txt/4881.txt","r")

def f(i,N,s):
    global min_v

    if i == N:
        min_v = min(s, min_v)
    elif s > min_v:
        return
    for j in range(i, N):
        p[i], p[j] = p[j], p[i]
        f(i+1, N, s + arr[i][p[i]])
        p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]
    # print(p)
    min_v = 100
    s = 0
    f(0, N, s)
    # print(min_v)

    print(f'#{tc} {min_v}')
