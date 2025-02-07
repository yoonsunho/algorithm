import sys
sys.stdin = open("factorization.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())

    a = b = c = d = e = 0

    while N >= 2:
        if N % 11 == 0:
            e += 1
            N //= 11
            # print(N)
            continue
        if N % 7 == 0:
            N //= 7
            d += 1
            continue
        if N % 5 == 0:
            N //= 5
            c += 1
            continue
        if N % 3 == 0:
            N //= 3
            b += 1
            continue
        if N % 2 == 0:
            N //= 2
            a += 1
            continue

    print(f'#{test_case} {a} {b} {c} {d} {e}')
