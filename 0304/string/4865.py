import sys
sys.stdin = open("txt/4865.txt", "r")

# 10m

T = int(input())
for tc in range(1, T+1):

    str1 = input()
    str2 = input()

    N, M = len(str1), len(str2)
    arr = [0] * N
    for i in range(N):
        for x in str2:
            if str1[i] == x:
                arr[i] += 1

    # print(max(arr))


    print(f'#{tc} {max(arr)}')