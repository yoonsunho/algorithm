import sys
sys.stdin = open("babygin.txt", "r")

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    num = int(input())
    # print(num)

    num_card = [0] * 12

    for i in range(6):
        num_card[num % 10] += 1
        num //= 10

    # print(num_card)

    i = 0
    run_num = 0
    triplet = 0

    while i < 10:
        if num_card[i] >= 3:
            num_card[i] -= 3
            triplet += 1
            continue
        if num_card[i] >= 1 and num_card[i + 1] >= 1 and num_card[i + 2] >= 1:
            num_card[i] -= 1
            num_card[i + 1] -= 1
            num_card[i + 2] -= 1
            run_num += 1
            continue
        i += 1

    if triplet + run_num == 2:
        ans = 'true'
    else:
        ans = 'false'

    print(f'#{test_case} {ans}')
