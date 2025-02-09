import sys
sys.stdin = open("sorting.txt", "r")
# 버블 정렬
# 다시 해보기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())    # 5 <= N <=50

    arr = list(map(int, input().split()))

    for i in range(N-1,0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # 배열을 문자열로 변환하여 출력
    print(f'#{test_case} {" ".join(map(str,arr))} ')