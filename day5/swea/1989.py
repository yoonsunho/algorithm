import sys
sys.stdin = open("txt/1989.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    txt = input()
    N = len(txt)

    for i in range(N):
        for j in range(N//2):
            if txt[i] != txt[N-1-i]:
                ans = 0
                break
        else:
            ans = 1


    print(f'#{test_case} {ans}')