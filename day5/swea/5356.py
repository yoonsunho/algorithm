import sys
sys.stdin = open("txt/5356.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    st_arr = [list(input()) for _ in range(5)]

    max_len = 0
    for i in range(5):
        leng = len(st_arr[i])
        max_len = max(max_len,leng)

    for i in range(5):
        if len(st_arr[i]) < max_len:
            for j in range(max_len-len(st_arr[i])):
                st_arr[i].append('')





    print(f'#{test_case}', end = " ")
    for j in range(max_len):
        for i in range(5):
            print(st_arr[i][j],end='')
    print()

