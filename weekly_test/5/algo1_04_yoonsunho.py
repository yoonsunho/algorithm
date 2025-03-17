T = int(input())

for tc in range(1, T+1):

    N, K = map(int, input().split())        # 이진수 문자열의 길이, 1의 개수(5<=N<=32, 2<=K<=N)
    bin_num = input()   # 문자로 받을 것임 #0으로 시작할 수 있음 주의

    count = 0
    for b in bin_num:
        if b == "1":
            count += 1  # 1의 총 개수 세기

    ans = 0

    if count < K:   # 찾고자 하는 1의 개수보다 1의 총 개수가 작으면 0 반환
        ans = 0

    else:
        st_i, st_j = -1, -1
        for i in range(N-1):
            # cnt = 0
            if bin_num[i] == "1":
                st_i = i    # 시작점 갱신
                cnt = 1     # 연속 1의 개수 담을 변수
                for j in range(i+1, N):
                    if bin_num[j] == "1":
                        cnt += 1
                    if cnt == K:
                        st_j = j
                        ans = max(st_j-st_i+1, ans)
                        break

    print(f'#{tc} {ans}')