import sys
sys.stdin = open("txt/1486.txt", "r")

# 합이 B이상인 부분집합 개수 구하기
def recur(i, total):
    global N, B
    global min_hei
    # print(hei)
    # print(total)

    # if total > min_hei:
    #     return

    if i == N:
        if total >= B:
        # print(total)
            min_hei = min(min_hei, total)
            return
        else:
            return

    recur(i+1,total)
    recur(i+1,total+hei[i])


T = int(input())
for tc in range(1,T+1):

    N, B = map(int,input().split())     # 점원의 수, 탑의 높이
    hei = list(map(int, input().split()))       # 점원들 키의 배열(1 ≤ Hi ≤ 10,000)
    # print(hei)

    min_hei = 200001
    recur(0, 0)

    print(f'#{tc} {min_hei-B}')