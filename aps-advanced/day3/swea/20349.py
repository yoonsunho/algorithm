import sys
sys.stdin = open("txt/20349.txt", "r")

def shuffle(n, arr,c):

    global T

    if c == T:
        return arr

    # 1회 셔플
    m = int(n*0.37)
    new_card = arr[:]

    arr = new_card[n-m:n]
    arr.extend(new_card[0:n-m])
    # print(arr)
    
    # 2회 셔플
    new_card = arr[:]
    k = n // 2
    if n % 2 == 0:
        for i in range(k):
            arr[2*i] = new_card[i]
            arr[2*i+1] = new_card[k+i]

    else:   # 홀수
        for i in range(k):
            arr[2*i] = new_card[i]
            arr[2*i+1] = new_card[k+i+1]
        arr[n-1] = new_card[k]
    # print(arr)
    shuffle(n, arr, c+1)


T = int(input())

for tc in range(1, T+1):

    N, T = map(int, input().split())

    num_card = [0] * N
    for i in range(N):
        num_card[i] = i+1

    cnt = 0

    ans = shuffle(N, num_card, cnt)
    print(ans)

    print(f'#{tc}')