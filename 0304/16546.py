import sys
sys.stdin = open("txt/16546.txt", "r")

# 베이비 진
# 못품
# 다시 풀어보기
T = int(input())
for tc in range(1, T+1):

    card = list(map(int, input()))
    num_card = [0] * 10

    run_n = 0
    triplet = 0

    for c in card:
        num_card[c] += 1

    # print(num_card)

    i = 0
    while i < 10:
        if num_card[i] >= 3:
            num_card[i] -= 3
            triplet += 1
            continue
        if i < 8 and num_card[i] >= 1 and num_card[i+1] >= 1 and num_card[i+2] >= 1:
            num_card[i] -= 1
            num_card[i+1] -= 1
            num_card[i+2] -= 1
            run_n += 1
            continue
        i += 1

    if run_n + triplet == 2:
        ans = "true"
    else:
        ans = "false"

    print(f'#{tc} {ans}')