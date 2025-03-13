# 도둑
gold = [[5, 50], [10, 60], [20, 140]]
target = 30
n = 3

# kg 당 가격으로 어떻게 정렬?
# 정렬: (price/kg)
gold.sort(key=lambda x: (x[1] /x[0]),reverse=True)
print(gold)