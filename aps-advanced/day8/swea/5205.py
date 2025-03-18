import sys
sys.stdin = open("txt/5205.txt", "r")

def partitioning(left,right):

    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j:

        while i <= j and arr[i] <= pivot:       # 왼쪽에  pivot보다 작거나 같은값 너흘 것임
            i += 1

        while i <= j and arr[j] >= pivot:       # 오른쪽에  pivot보다 크거나 같은값 너흘 것임
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]     # 자리 교환

    arr[left], arr[j] = arr[j], arr[left]     # 피봇 위치 바꿔주고
    return j    # 피봇 인덱스 반환
            
def quick_sort(left,right):

    if left < right:

        pivot = partitioning(left,right)
        quick_sort(left,pivot - 1)
        quick_sort(pivot + 1, right)

T = int(input())
for tc in range(1, T+1):

    N = int(input())

    arr = list(map(int, input().split()))

    quick_sort(0,len(arr)-1)



    print(f'#{tc} {arr[N//2]}')