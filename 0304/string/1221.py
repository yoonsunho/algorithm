import sys
sys.stdin = open("txt/1221.txt", "r")

T = int(input())
for _ in range(1, T+1):

    tc, N = input().split()
    N = int(N)
    # print(N)
    gns = list(input().split())

    arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    count_arr = [0] * 10
    for i in range(10):
        for x in gns:
            if arr[i] == x:
                count_arr[i] += 1

    # print(count_arr)



    print(f'{tc} ')
    for i in range(10):
        print((arr[i]+' ')*count_arr[i], end=" ")
    print()