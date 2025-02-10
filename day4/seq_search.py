def seq_search(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
    return -1

arr= [4, 9, 11, 23, 2, 19, 7]
print(seq_search(arr, len(arr), 23))    # 3
print(seq_search(arr, len(arr), 100))   # -1

key = 11
ans = -1
for i in range(len(arr)):
    if arr[i] == key:
         ans = i