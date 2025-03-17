import sys
sys.stdin = open("txt/5207.txt", "r")

def bim_search(n):
    left = 0
    right = len(arr)

    while left < right:

        mid = (left+right)//2

        if target == arr[mid]:
            cnt += 1
        left_list = arr


T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())

    arr = list(map(int, input().split()))
    find_list = list(map(int, input().split()))

    for x in find_list:
        bin_search(x)





    print(f'#{tc}')