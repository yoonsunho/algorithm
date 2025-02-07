T = int(input())

for tc in range(1, T+1):

    N = int(input())
    per = list(map(int,input()))

    max_v = 0
    count = 0
    for i in range(N):
        if per[i] == 1:
            count += 1
            max_v = max(count,max_v)
        else:
            count = 0


    print(f'#{tc} {max_v}')