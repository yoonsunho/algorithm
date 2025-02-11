import sys
sys.stdin = open("txt/4865.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    str1 = set(list(input()))
    str2 = input()

    max_v = 0
    for s in str1:
        count = 0
        for s2 in str2:
            if s == s2:
                count += 1
        max_v = max(max_v,count)




    print(f'#{test_case} {max_v}')