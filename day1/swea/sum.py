T = int(input())


for test_case in range(1,T+1):

    N, M = map(int, input().split()) # 정수의 개수:N, 구간의 개수 :M
    ai = list(map(int, input().split()))

    sum = 0
    for i in range(M):
        sum += ai[i]

    min_sum = sum
    max_sum = sum

    # s=0
    for i in range(N-M+1):
        s = 0
        for m in range(i, i+M):

            s += ai[m]
        if min_sum > s:
            min_sum = s
        if max_sum < s:
            max_sum = s

    print(f'#{test_case} {max_sum-min_sum}')