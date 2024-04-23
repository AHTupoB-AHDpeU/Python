number = 0
while number != "exit":
    number = input("Введите трёхзначное число, где все цифры различные: ")
    if len(number) != 3:
        print("Введите трёхзначное число! ")
    else:
        if len(set(number)) != 3:
            print("Число должно состоять из разных цифр! ")
        else:
            numbers = [number[0] + number[1] + number[2],
                       number[0] + number[2] + number[1],
                       number[1] + number[0] + number[2],
                       number[1] + number[2] + number[0],
                       number[2] + number[1] + number[0],
                       number[2] + number[0] + number[1]]
            for i in numbers:
                print(i)
