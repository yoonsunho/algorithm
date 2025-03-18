import sys
sys.stdin = open("txt/5208.txt", "r")

T = int(input())
for tc in range(1, T+1):

    arr = list(map(int,input().split()))
    N = arr[0]
    charging = arr[1:]
    # print(N, charging)


    cnt = 0

    i = 0
    while (i + charging[i]) < N-1:
        new_i = 0
        max_idx = 0
        for j in range(i+1, i+charging[i]+1):
            if max_idx < j + charging[j]:
                max_idx = j + charging[j]
                new_i = j

        i = new_i
        # print(i)
        cnt += 1
        # print(cnt)
            # max_long = max(max_long, j+ arr[j])

    # print(cnt)

    print(f'#{tc} {cnt}')