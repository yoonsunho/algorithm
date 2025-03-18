import sys
sys.stdin = open("txt/5207.txt", "r")

def bin_search(target):
    global cnt
    left = 0
    right = len(arr) - 1
    l_cnt, r_cnt = 0, 0

    while left <= right:

        mid = (left+right)//2

        if target == arr[mid]:  # 찾았으면
            cnt += 1
            break

        if target < arr[mid] and l_cnt == 0:
            right = mid - 1
            l_cnt, r_cnt = 1, 0

        elif target > arr[mid] and r_cnt == 0:
            left = mid + 1
            l_cnt, r_cnt = 0, 1

        else:
            break


T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())

    arr = sorted(list(map(int, input().split())))
    find_list = list(map(int, input().split()))

    cnt = 0
    for x in find_list:
        bin_search(x)
    # print(cnt)


    print(f'#{tc} {cnt}')