import sys
sys.stdin = open("txt/1225.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    tc = int(input())

    arr = list(map(int, input().split()))
    for i in range(5):
        if arr[0] - i >= 0:
            arr.append(arr[0]-(i+1))
        else:
            break







    print(f'#{tc}')