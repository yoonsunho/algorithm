import sys
sys.stdin = open("txt/in.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())  # 방의 가로 길이

    arr = list(map(int,input().split()))
    # 8 - 같은 높이 아이들

    max_v = 0
    for i in range(N-1):
        count = 0
        for j in range(i+1,N):
            if arr[i]> arr[j]:
                count += 1

        max_v = max(max_v,count)


    print(f'#{test_case} {max_v}')