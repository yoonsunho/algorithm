import sys
sys.stdin = open("txt/4864.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    str1 = input()  # 문자열 길이 N, (5≤N≤100,)
    str2 = input()  # 문자열 길이 M, (10≤M≤1000, N≤M)
    result = 0

    if str1 in str2:
        result = 1

    print(f'#{test_case} {result}')