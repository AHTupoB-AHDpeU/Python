pos = 0
neg = 0

number = int(input("Введите число: "))

for i in range(-number, number+2):
    print(i)
    if i > 0:
        pos = pos + i
    elif i < 0:
        neg = neg + i

print("Сумма положительных: " + str(pos))
print("Сумма положительных: " + str(neg))
