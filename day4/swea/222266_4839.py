import sys
sys.stdin = open("txt/222266.txt", "r")

def binary_search(x):
    start = 1
    end = P
    cnt = 0
    while start <= end:
        middle = int((start + end) / 2)
        cnt += 1
        if middle == x:
            return cnt
        elif middle < x:
            start = middle
        else:
            end = middle
    return cnt


    return cnt


T = int(input())        # 1<=T<=50
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    P, Pa, Pb = map(int, input().split())
    A_num = binary_search(Pa)
    B_num = binary_search(Pb)
    if A_num > B_num:
        ans = 'B'
    elif A_num < B_num:
        ans = 'A'
    else:
        ans = 0

    print(f'#{test_case} {ans}')