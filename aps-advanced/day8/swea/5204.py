import sys
sys.stdin = open("txt/5204.txt", "r")

def merge(left,right):

    global cnt
    result = [0]* (len(left)+len(right))    # merge한 결과를 담을 리스트
    l, r = 0, 0

    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left) and r < len(right): # 두 리스트 다 병합한 애들이 남아있을 때 까지
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < len(left):
        result[l+r] = left[l]
        l += 1

    while r <len(right):
        result[l+r] = right[r]
        r += 1

    return result
    


def merge_sort(li):

    if len(li) == 1:
        return li

    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    merged_list = merge(left_list, right_list)
    return merged_list

T = int(input())
for tc in range(1, T+1):

    N = int(input())

    arr = list(map(int,input().split()))

    cnt = 0

    # print(merge_sort(arr))


    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')