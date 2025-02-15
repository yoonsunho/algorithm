num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

# 입력한 숫자 문자열들
arr = ['TWO', 'SIX', 'TWO', 'FIV', 'FOR', 'SIX']

# 1. 0-9 사이에 해당하는 문자열들을 리스트에
# lst =[]
# for val in arr:
#     lst.append()

# 2.딕셔너리
num_dict = {}
for i in range(10):
    num_dict[num_str[i]]= i
# print(num_dict)

lst =[]
for key in arr:
    lst.append(num_dict[key])
print(lst)  # [2, 6, 2, 5, 4, 6]