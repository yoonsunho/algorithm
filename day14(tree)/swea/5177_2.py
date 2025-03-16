import sys
sys.stdin = open("txt/5177.txt", "r")

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last    # 자식
    p = c//2
    while p != 0 and heap[c] < heap[p]:    # 부모가 있고 자식이 부모보다 작다면
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq(n):     # 조상들의 합 구하기
    global sum_v
    while n:
        n //= 2
        sum_v += heap[n]

# 최소 힙
# 0316 다시 풀어보기
T = int(input())
for tc in range(1, T+1):

    N = int(input())        # 정점의 개수
    arr = list(map(int, input().split()))   # 각 정점에 들어갈 값들

    last = 0
    heap = [0] * (N+1)
    for a in arr:
        enq(a)

    # print(heap)
    # print(last)
    sum_v = 0
    deq(last)
    # print(sum_v)
    print(f'#{tc} {sum_v}')