numbers = [1, 0, 3, 5, 0, 0, 6]

no_zero = []
zero = []

for num in numbers:
    if num == 0:
        zero.append(num)
    else:
        no_zero.append(num)
result = no_zero + zero
print(result)