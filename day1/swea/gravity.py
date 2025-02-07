T = int(input())


for test_case in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))

    max_num = 0
    for i in range(N):
        count = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                count += 1
                # print(count)
        if max_num < count:
            max_num = count

    print(f'#{test_case} {max_num}')
