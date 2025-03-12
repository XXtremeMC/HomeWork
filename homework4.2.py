numbers = [1, 2, 3, 4, 5, 6]
index_total = 0
for i in range(0, len(numbers), 2):
    index_total += numbers[i]
result = index_total * numbers[-1] if numbers else 0
print(result)