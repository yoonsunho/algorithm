import sys
sys.stdin = open("txt/1219.txt", "r")

def check(i,j):

    arr1 = [0] * 100
    arr2 = [0] * 100

    while True:
        pass



for _ in range(10):

    T, N = map(int, input().split())

    spots = list(map(int, input().split()))

    adj_list = [[] for _ in range(99)]
    for i in range(N):
        v, w = spots[2*i], spots[2*i+1]
        adj_list[v].append(w)

    print(adj_list)
    check(0, 99)


    print(f'#{T}')
