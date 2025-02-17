import sys
sys.stdin = open("txt/11315.txt", "r")

def check(i):
    count = 1
    for j in range(1, 5):
        if omok_arr[i][j] == 'o':
            count += 1
    if count == 5:
        return 'YES'
    else:
        return 'NO'

def check_l(i):
    count = 1
    for j in range(1, 5):
        if omok_arr[i+j][j] == 'o':
            count += 1
    if count == 5:
        return 'YES'
    else:
        return 'NO'

def check_r(i):
    count = 1
    for j in range(1, 5):
        if omok_arr[i + j][4 - j] == 'o':
            count += 1
    if count == 5:
        return 'YES'
    else:
        return 'NO'



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())    # 줄의 개수(5<=N <=20)

    omok_arr = [[0]*5 for _ in range(N)]

    for i in range(N):
        omok_arr[i] = list(map(str, input()))

    for x in range(N-5+1):
        if omok_arr[x][0] == 'o':
            ans = check(x)
            print(ans)
            an = check_l(x)
            print(an)
        elif omok_arr[x][4] == 'o':
            ans = check_r(x)
            print(ans)

    for x in range(N-5+1, N):
        count = 0
        for j in range(5):

            if omok_arr[x][j] == 1:
                count += 1
        if count == 5:
            a = 'YES'
        else:
            a = 'NO'
        print(a)

    if ans == 'YES' or a == 'YES':
        answer = 'YES'
    else:
        answer = 'NO'

    print(f'#{test_case} {answer}')