import sys
sys.stdin = open("txt/5177.txt", "r")

# 최소 힙

def enq(n):     # 최소 힙 만들어 주는 함수
    global last
    last += 1
    heap[last] = n

    c = last
    p = c // 2
    while p and heap[p] > heap[c]:      # 부모가 있고, 부모의 값이 자식의 값보다 크다면
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
        

def sum_count(n):       # 조상의 합 구하는 함수
    cnt = 0
    while n > 1:
        cnt += heap[n//2]
        n = n//2

    return cnt


T = int(input())
for tc in range(1, T+1):

    N = int(input())

    arr = list(map(int, input().split()))

    heap = [0] * (N+1)

    last = 0

    for x in arr:
        enq(x)

    ans = sum_count(N)
    
    print(f'#{tc} {ans}')