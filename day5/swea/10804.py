import sys
sys.stdin = open("txt/10804.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    str_ori = list(input())
    str_ori.reverse()

    for i in range(len(str_ori)):
        if str_ori[i] == 'p':
            str_ori[i] = 'q'
        elif str_ori[i] == 'q':
            str_ori[i] = 'p'
        if str_ori[i] == 'b':
            str_ori[i] = 'd'
        elif str_ori[i] == 'd':
            str_ori[i] = 'b'

    result = ''.join(str_ori)

    print(f'#{test_case} {result}')