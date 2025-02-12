import sys
sys.stdin = open("txt/4839.txt", "r")


def binary_search(n, k):
    start = 1
    end = n
    while start <= end:
        middle = (start - end) // 2
        cnt = 1
        if k == middle:
            return cnt
        elif k <= middle:
            cnt += 1
            end = middle - 1
        else:
            cnt += 1
            start = middle + 1
    return cnt

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    P, A, B = map(int, input().split())



    print(binary_search(P, A))
    print(binary_search(P, B))



    print(f'#{test_case}')