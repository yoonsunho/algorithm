import sys
sys.stdin = open("txt/9367.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())        # 5<=N<=1000
    carrot_array = list(map(int, input().split()))  # 5<=N<=1000

    count = 1
    max_v = count
    for i in range(1, N):
        if carrot_array[i] > carrot_array[i-1]:
            count += 1
            max_v = max(max_v, count)
        else:
            count = 1

    print(f'#{test_case} {max_v}')