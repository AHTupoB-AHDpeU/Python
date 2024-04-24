quantity = int(input("Количество чисел?: "))
level = int(input("Степень: "))
numbers = []
n = 1

for i in range(quantity):
    number = input("Введите {} число: ".format(n))
    n += 1
    numbers.append(number)

for j in numbers:
    if j.isdigit() | (j[0] == '-' and j[1:].isdigit()):  # 1 - цифры, 2 - первый символ -, последующие цифры
        j = int(j)
        result = j ** level  # числа
    else:
        result = j * level  # строка
    print(result)
