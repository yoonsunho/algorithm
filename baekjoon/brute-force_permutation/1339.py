# 0326 단어 수학
# 0403
# 굳이 알팝벳으로 받지 않아도 될 듯

N = int(input())    # 알파벳으로 이루어진의 개수(1 ≤ N ≤ 10)

str_list = []
for _ in range(N):
    s = input()
    str_list.append((s, len(s)))

str_list.sort(key=lambda x: x[1], reverse=True)
print(str_list)

