import sys
sys.stdin = open("txt/11315.txt", "r")

def check(x,y):
    if x < N - 4:
        for i in range(N-5+1):
            if omok_arr[i][0] == 'o':
                count = 1
                for j in range(1,5):
                    if omok_arr[i][j] =='o':
                        count += 1


# def check(i,j):
#     count = 1
#     count_l = 1
#     for j in range(1,5):
#         if omok_arr[i][j] == 'o':
#             count += 1
#         if omok_arr[i+j][j] == 'o':
#             count_l += 1
#     if count == 5 or count_l == 5:
#         return True
#     else:
#         return False
#
#
# def check_rev(i):
#     count = 1
#     for j in range(1,5):
#         if omok_arr[i+j][4-j] == 'o':
#             count += 1
#     if count == 5:
#         return True
#     else:
#         return False





T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())    # 줄의 개수(5<=N <=20)

    omok_arr = [[0]*5 for _ in range(N)]

    for i in range(N):
        omok_arr[i] = list(map(str, input()))

    for x in range(N):
        for y in range(5):
            check(x, y)

    # for i in range(N-5+1):
    #     if omok_arr[i][0] == 'o':
    #         t1 = check(i)
    #     elif omok_arr[i][4] == 'o':
    #         t2 = check_rev(i)
    #
    # for i in range(N-5+1, N):
    #     count = 0
    #     for j in range(5):
    #
    #         if omok_arr[i][j] == 1:
    #             count += 1
    #     if count == 5:
    #         t3 = True
    #         break
    #
    # ans = t1 or t2 or t3
    #
    # if ans == True:
    #     answer = 'YES'
    # else:
    #     answer = 'NO'
    print(f'#{test_case} {answer}')