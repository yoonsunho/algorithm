import sys
sys.stdin = open("txt/1989.txt", "r")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    N = len(str1)

    ans = 1
    for i in range(N//2):
        if str1[i] != str1[N-1-i]:
            ans = 0
            break

    print(f'#{tc} {ans}')
