# 0326 단어 수학
# 0403
# 굳이 알팝벳으로 받지 않아도 될 듯

N = int(input())    # 알파벳으로 이루어진의 개수(1 ≤ N ≤ 10)

str_list = []
for _ in range(N):
    s = input()
    str_list.append(s)

# print(str_list)

alpha_dict = {}
for x in str_list:
    for i in range(len(x)):
        if x[i] in alpha_dict:
            alpha_dict[x[i]] += 10 ** (len(x)-i-1)
        else:
            alpha_dict[x[i]] = 10**(len(x)-i-1)
# print(alpha_dict)
value_list = list(alpha_dict.values())
value_list.sort(reverse=True)
# print(value_list)

result = 0
num_list = [i for i in range(10)]

for x in value_list:
    result += num_list.pop(-1)*x

print(result)
