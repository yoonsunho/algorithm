import sys
sys.stdin = open("txt/20397.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    stone_arr = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        for k in range(1, j+1):
            if i - k >= 0 and i+k <= N-1:
                if stone_arr[i-k-1] == stone_arr[i+k-1]:
                    stone_arr[i-k-1] = 1 - stone_arr[i-k-1]
                    stone_arr[i + k - 1] = 1 - stone_arr[i+k-1]
    print(stone_arr)


    print(f'{test_case}')