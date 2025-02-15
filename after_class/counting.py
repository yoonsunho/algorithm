arr = [2, 0, 2, 3, 1, 4, 0, 2]

max_val = 4
cnt = [0] * (max_val +1 )
for val in arr:
    cnt[val] += 1

print(cnt)

sorted_list =[]
for i in range(max_val +1):
    if cnt[i] != 0:
        sorted_list += [i]* cnt[i]
print(sorted_list)