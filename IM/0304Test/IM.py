'''
3
4 2
6 4 2 3
4 3
1 2 3 4
4 1
1 3 7 5
'''

T = int(input())

for tc in range(1, T+1):

    N, K = map(int, input().split())

    arr = sorted(list(map(int, input().split())))[::-1]
    # print(arr)

    ans = 1
    x = N

    while x > 1:
        for i in range(N-x+1):
            if arr[i] - arr[i+x-1] <= K:
                ans = x
                break
        if ans != 1:
            break

        x -= 1
    # while x > 1:
    #     for i in range(N-x+1):
    #         for j in range(x-1):
    #             if arr[i+j] - arr[i+j+1] > K-1:
    #                 break
    #         else:
    #             ans = x
    #             break
    #
    #     if ans != 1:
    #         break


    print(f'#{tc} {ans}')