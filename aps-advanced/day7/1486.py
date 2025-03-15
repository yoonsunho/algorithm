import sys
sys.stdin = open("txt/1486.txt", "r")

# 내 풀이
# 부분집합을 구하고
# 탑의 높이와 동일한 합이 나오면 break
# 없으면 차가 가장 작을 때 를 찾고 break
# ㅎ,ㅁ... 못품

T = int(input())
for tc in range(1, T+1):

    N, B = map(int, input().split())    # 점원의 수, 탑의 높이(1 ≤ N ≤ 20, 1 ≤ B ≤ S)
    hei = list(map(int, input().split()))

    arr = []
    # print(1<<N)
    for tar in range(1 << N):
        for i in range(N):
            if tar >> i & 0x1:
                arr.append(sum(hei[i]))
                # print(hei[i], end=' ')
        # print()

    print(arr)
    print(f'#{tc}')