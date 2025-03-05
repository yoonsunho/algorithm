import sys
sys.stdin = open("txt/23879.txt", "r")

def pre_order(n):
    if n:
        print(n,end=" ")
        pre_order(left[n])
        pre_order(right[n])

V = int(input())        # 정점의 수
E = V-1                 # 간선의 수

arr = list(map(int, input().split()))
left = [0] * (V+1)
right = [0] * (V+1)
par = [0] * (V+1)

for i in range(E):
    p, c = arr[2*i], arr[2*i+1]
    par[c] = p
    if left[p] == 0:    # 왼쪽 비어 있으면
        left[p] = c
    else:
        right[p] = c

for i in range(1, V+1):
    if par[i] == 0:
        root= i
        break

pre_order(root)
