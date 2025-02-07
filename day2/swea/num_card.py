import sys
sys.stdin = open("num_card.txt", "r")

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    ai = list(map(int, input()))

    count = 0

    for i in range(N):
        cnt = 1
        for j in range(i+1,N):
            if ai[i] == ai[j]:
                cnt += 1
            if cnt > count:
                count = cnt
                max_v = ai[j]

    print(f'#{test_case} {max_v} {count}')