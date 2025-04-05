def difference(*args):
    if not args:  # якщо аргументів немає
        return 0

    return round(max(args) - min(args), 2)  # знаходимо різницю між max та min значеннями, та округляємо результат


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
print(difference(1, 2, 3))