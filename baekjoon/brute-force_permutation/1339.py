# 0326 단어 수학
# 0403
# 굳이 알팝벳으로 받지 않아도 될 듯

N = int(input())    # 알파벳으로 이루어진의 개수(1 ≤ N ≤ 10)

str_list = []
for _ in range(N):
    s = input()
    str_list.append([s, len(s)])

str_list.sort(key=lambda x: x[1], reverse=True)
print(str_list)

alpha_dict = {}
for x in str_list:
    for a in x[0]:
        if a in alpha_dict:
            alpha_dict[a] += 1
        else:
            alpha_dict[a] = 1
print(alpha_dict)

result = {}
num_list = [i for i in range(10)]
print(num_list)

#
for i in range(N-1):
    if str_list[i][1] > str_list[i+1][1]:
        k = str_list[i][1] - str_list[i+1][1]

        for x in range(k):
            result[str_list[i][0][x]] = num_list.pop(-1)
        str_list[i][1] -= k
        str_list[i][0] = str_list[i][0][k:]








print(str_list)
print(result)
