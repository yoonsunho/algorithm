T = int(input())

for tx in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    min_num = ai[0]
    max_num = ai[0]

    for i in range(N):
        if max_num < ai[i]:
            max_num= ai[i]
        if min_num > ai[i]:
            min_num = ai[i]

    print(f'#{tx} {max_num-min_num}')
