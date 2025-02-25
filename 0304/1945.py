import sys
sys.stdin = open("txt/1945.txt", "r")

# 오래걸림 다시 풀어보자
# 재귀함수 return 조건 주의!!!

def divi(a, b, c, d, e,n):


    if n % 11 == 0:
        e += 1
        return divi(a, b, c, d, e, n//11)
    elif n % 7 == 0:
        d += 1
        return divi(a, b, c, d, e, n//7)
    elif n % 5 == 0:
        c += 1
        return divi(a, b, c, d, e, n // 5)
    elif n % 3 == 0:
        b += 1
        return divi(a, b, c, d, e, n // 3)
    elif n % 2 == 0:
        a += 1
        return divi(a, b, c, d, e, n//2)

    return a, b, c, d, e


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    a, b, c, d, e = 0, 0, 0, 0, 0

    ans = divi(a, b, c, d, e, N)

    print(f'#{tc} {" ".join(map(str,ans))}')