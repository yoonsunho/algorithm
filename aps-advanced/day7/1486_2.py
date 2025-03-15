import sys
sys.stdin = open("txt/1486.txt", "r")

# 강사님 풀이
# 합이   B이상인 부분집합을 구하라
# level : 점원의 수
# branch : 포함 or 포함 x
# 가지치기가 핵심~!

def recur(cnt,total):

    global min_hei
    global B

    if total >= B:
        min_hei = min(min_hei,total)
        return

    if cnt == N:
        return

    recur(cnt + 1, total + hei[cnt])   # 현재 점원 포함
    recur(cnt + 1, total)             # 현재 점원 포함 x

T = int(input())
for tc in range(1, T+1):

    N, B = map(int, input().split())    # 점원의 수, 탑의 높이(1 ≤ N ≤ 20, 1 ≤ B ≤ S)
    hei = list(map(int, input().split()))

    min_hei = 200001
    recur(0,0)

    # print(arr)
    print(f'#{tc} {min_hei-B}')