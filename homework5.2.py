while True:

    num1 = int(input("Enter number: "))
    operator = (input("Operator: "))
    num3 = int(input("Enter number: "))

    match operator:
        case "+":
            result = num1 + num3
            print(result)
        case "-":
            result = num1 - num3
            print(result)
        case "*":
            result = num1 * num3
            print(result)
        case "/":
            if num3 == 0:
                print("Not divisible by zero")
            else:
                result = num1 / num3
                print(result)
        case _:
            print("Error")

    while True:
        continue_calc = input("Do you want to continue?(y/n): ").lower()
        if continue_calc == 'yes' or continue_calc == 'y':
            break
        elif continue_calc == 'no' or continue_calc == 'n':
            print("Finish")
            exit()
