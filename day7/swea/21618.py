import sys
sys.stdin = open("txt/21618.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    txt = list(input())

    def popo(i, N):
        if i == N-1:
            return N
        elif txt[i] == txt[i+1]:
            for _ in range(2):
                txt.pop(i)
            N = len(txt)
            i = 0
            return popo(i, N)
        else:
            return popo(i+1, N)


    N = len(txt)
    ans = popo(0, N)


    print(f'#{test_case} {ans}')