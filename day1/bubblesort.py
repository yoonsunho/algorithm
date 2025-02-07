'''
5
55 7 78 12 42
'''

N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1,0,-1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr) # [7, 12, 42, 55, 78]