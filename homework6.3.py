number = int(input("Enter a number: "))
result = number

while result > 9:
    temp = 1
    for numeral in str(result):
        temp *= int(numeral)
        result = temp
    print(result)
print("Finish result:", result)
