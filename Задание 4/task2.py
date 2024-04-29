def fibonachy(num):
    number1 = 1  # Задание
    number2 = 1
    yield number1
    yield number2
    for i in range(num):
        number_next = number1 + number2
        number1 = number2
        number2 = number_next
        yield number_next


n = int(input("Введите n-число ряда Фибоначчи: "))
gen = fibonachy(n)
for j in range(n):
    print(next(gen))
