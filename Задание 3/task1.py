action = str("")
while action != "exit":
    number1 = input("Введите первое число: ")
    number2 = input("Введите второе число: ")
    action = input("Выберите действие (+, -, *, /, ** или exit): ")

    try:
        if not (number1.isdigit() and number2.isdigit()):
            raise ValueError("Введите целые числа!")
        number1 = int(number1)
        number2 = int(number2)
    except ValueError as error:
        print(error)
        continue

    def plus(number1, number2):
        return number1 + number2

    def minus(number1, number2):
        return number1 - number2

    def ply(number1, number2):
        return number1 * number2

    def share(number1, number2):
        if number2 == 0:
            raise ZeroDivisionError("Нельзя делить на 0!")
        return number1 / number2

    def level(number1, number2):
        return number1 ** number2

    #  number1 = int(number1)
    #  number2 = int(number2)

    if action == "+":
        result = plus(number1, number2)
        print("Ответ: {}". format(result))
    elif action == "-":
        result = minus(number1, number2)
        print("Ответ: {}". format(result))
    elif action == "*":
        result = ply(number1, number2)
        print("Ответ: {}". format(result))
    elif action == "/":
        try:
            result = share(number1, number2)
            print("Ответ: {}". format(result))
        except ZeroDivisionError as error0:
            print(error0)
    elif action == "**":
        result = level(number1, number2)
        print("Ответ: {}". format(result))
    elif action == "exit":
        break
    else:
        print("Неверно введён знак действия!")
