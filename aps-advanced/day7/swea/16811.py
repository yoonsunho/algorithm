import sys
sys.stdin = open("txt/16811.txt", "r")
# import sys

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    size = list(map(int, input().split()))

    # 당근 크기별 개수 세기
    counting = [0] * 31
    for s in size:
        counting[s] += 1

    # 상자 초기화
    box = [0, 0, 0]  # 소, 중, 대 상자

    # 당근 크기별로 상자에 할당
    for i in range(30, 0, -1):
        if counting[i] > 0:
            # 같은 크기의 당근은 같은 상자에 할당
            if box[2] <= box[1] and box[2] <= box[0] and box[2] + counting[i] <= N // 2:
                box[2] += counting[i]
            elif box[1] <= box[2] and box[1] <= box[0] and box[1] + counting[i] <= N // 2:
                box[1] += counting[i]
            elif box[0] <= box[2] and box[0] <= box[1] and box[0] + counting[i] <= N // 2:
                box[0] += counting[i]
            else:
                # 다른 상자에 할당
                if box[2] + counting[i] <= N // 2:
                    box[2] += counting[i]
                elif box[1] + counting[i] <= N // 2:
                    box[1] += counting[i]
                elif box[0] + counting[i] <= N // 2:
                    box[0] += counting[i]
                else:
                    # 할당 불가
                    ans = -1
                    break
    else:
        # 조건 확인
        M = N // 2
        if max(box) > M or min(box) == 0:
            ans = -1
        else:
            ans = max(box) - min(box)

    print(f'#{tc} {ans}')
