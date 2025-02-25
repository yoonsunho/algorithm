import sys
sys.stdin = open("txt/4834.txt", "r")

# 21m (꽤 오래 걸림..)

T = int(input())

for tc in range(1,T+1):

    N = int(input())        # 5 ≤ N ≤ 100

    num_ar = list(map(int, input()))       # 0 ≤ ai ≤ 9

    max_v = 1
    max_num = num_ar[0]
    for i in range(N-1):
        cnt = 1
        for j in range(i+1,N):
            if num_ar[i] == num_ar[j]:
                cnt += 1
        if cnt > max_v:
            max_v = cnt
            max_num = num_ar[i]
        elif cnt == max_v:
            max_num = max(max_num, num_ar[i])

        # max_v = max(max_v, cnt)



    print(f'#{tc} {max_num} {max_v}')