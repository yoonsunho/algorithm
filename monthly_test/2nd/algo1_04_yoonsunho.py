'''
3
5 1
1 1 0 0 1
2 3 1
5 3
1 1 0 0 1
2 3 2
2 4 1
2 2 4
5 1
1 1 1 0 1
2 4 2

'''

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())        # N명, 명령 M번
    arr = list(map(int, input().split()))       # 초기상태

    for _ in range(M):      # 명령문 마다 작업 진행
        hard, st, r = map(int, input().split())

        for i in range(1, r+1):
            if st + i <= N and st - i > 0:
                if arr[st+i-1] == arr[st-i-1]:
                    arr[st+i-1], arr[st-i-1] = 1 - arr[st+i-1], 1 - arr[st-i-1]



        # print(hard,st,r)


    # print(arr)




    print(f'#{tc} {" ".join(map(str,arr))}')