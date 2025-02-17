import sys
sys.stdin = open("txt/3499.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())

    arr = list(map(str, input().split()))
    new_arr = [0]*N

    if N % 2 == 0:
        first = arr[0:N//2]
        last = arr[N//2:N]
        for i in range(N // 2):
            new_arr[2 * i] = first[i]
            new_arr[2 * i + 1] = last[i]
    else:
        first = arr[0:N//2+1]
        last = arr[N//2+1:N]
        # print(first)
        # print(last)
        for i in range(N//2):
            new_arr[2*i] = first[i]
            new_arr[2*i+1] = last[i]
        new_arr[N-1] = first[N//2]



    print(f'#{test_case} {" ".join(map(str,new_arr))}')