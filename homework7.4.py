def common_elements():
    multiples_of_3 = set(range(0, 100, 3))
    multiples_of_5 = set(range(0, 100, 5))
    
    common = multiples_of_3.intersection(multiples_of_5)
    return common


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
