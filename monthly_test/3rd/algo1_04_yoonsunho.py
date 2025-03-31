T = int(input())        # 3<=T<=10

for tc in range(1, T+1):

    o, e = map(int, input().split())    # 체육관 여는 시간, 닫는 시간(6<=o<=12, 13<=e<=20)

    N = int(input())
    time_line = []

    for _ in range(N):
        st, end = map(int, input().split())
        time_line.append((st, end))

    time_line.sort(key=lambda x: x[1])  # 끝나는 시간 기준으로 오름차순 정렬

    # print(time_line)

    cnt = 0     # 신청가능 팀의 개수를 담을 변수
    i = 0
    next_st = o
    while i < N and time_line[i][1] <= e:

        if time_line[i][0] >= next_st:
            cnt += 1
            next_st = time_line[i][1]

        i += 1

    print(f'#{tc} {cnt}')