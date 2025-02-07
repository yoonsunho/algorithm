'''
3
5
1 1 2 3 3
10
3 10 5 5 8 3 9 1 3 3
20
4 1 6 7 9 4 1 4 8 4 1 6 5 3 1 4 3 1 10 10
'''

T = int(input())    # ( 1 ≤ T ≤ 10 )


for test_case in range(1, T+1):

    N = int(input())  # ( 5 ≤ N ≤ 100 )
    ai = list(map(int, input().split()))  # ( 1 ≤ ai≤ 10 )

    min_num_idx = 0
    max_num_idx = 0

    for i in range(1, N):
        if ai[min_num_idx] > ai[i]:
            min_num_idx = i
        if ai[max_num_idx] <= ai[i]:
            max_num_idx = i
    dif = max_num_idx - min_num_idx
    if dif < 0:
        dif = dif * (-1)

    print(f'#{test_case} {dif}')