# import sys
# sys.stdin = open("txt/21618.txt", "r")
# 이거 테스트 케이스 오류 뜸 왜일까 못찾음..
# 재귀함수를 사용하면 스택 오버플렁 발생시킬 수 있다함 ..
# 스택 이용해서 풀어보자..

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    txt = list(input())
    N = len(txt)  # 1<=N<=1000


    def popo(i, N):
        if N == 0:
            return 0
        elif i == N-1:
            return N
        elif txt[i] == txt[i+1]:
            for _ in range(2):
                txt.pop(i)
            n = len(txt)
            i = 0
            return popo(i, n)
        else:
            return popo(i+1, N)



    ans = popo(0, N)


    print(f'#{test_case} {ans}')