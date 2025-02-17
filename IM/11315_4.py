import sys
sys.stdin = open("txt/11315.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())    # 줄의 개수(5<=N <=20)

    omok_arr = [[0]*5 for _ in range(N)]

    for i in range(N):
        omok_arr[i] = list(map(str, input()))
    
    # 가로
    for i in range(N):
        count = 0
        for j in range(5):
            if omok_arr[i][j] == 'o':
                count += 1
        if count == 5:
            ans = 'YES'
            break
        else:
            ans = 'NO'
    
    # 세로
    if ans == 'NO':
        revers_omok = list(map(list, zip(*omok_arr)))
        for i in range(N):
            count = 0
            for j in range(5):
                if revers_omok[i][j] == 'o':
                    count += 1
            if count == 5:
                ans = 'YES'
                break
            else:
                ans = 'NO'
    
    # 왼대각
    if ans == 'NO':
        for i in range(N-4):
            count = 0
            for j in range(5):
                if omok_arr[i+j][j] == 'o':
                    count += 1
            if count == 5:
                ans = 'YES'
                break
            else:
                ans = 'NO'
    
    # 우대각
    if ans == 'NO':
        for i in range(N-4):
            count = 0
            for j in range(4, -1, -1):
                if omok_arr[i-j+4][j] == 'o':
                    count += 1
            if count == 5:
                ans = 'YES'
                break
            else:
                ans = 'NO'




    print(f'#{test_case} {ans}')