import sys
sys.stdin = open("txt/16546.txt", "r")

T = int(input())

for tc in range(1, T+1):
    
    # 0~9까지의 카드
    number = int(input())
    n = len(number)

    num_card = [0] * 10

    for i in range(n):
        num_card[number % 10] += 1
        number //= 10

    triplet = 0
    run_num = 0
    while i < 10:
        if num_card[i] >= 3:
            num_card[i] -= 3
            triplet += 1
            continue
        elif num_card[i]>= 1 and num_card[i+1]>=1 and num_card[i+1] >= 1:
            num_card[i],

    print(f'#{tc}')