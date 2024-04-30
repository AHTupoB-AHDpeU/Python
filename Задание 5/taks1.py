import random

s = random.randint(1, 100)
print(s)

if s % 2 == 0:
    print("Чётное число: {}!".format(s))
else:
    print("Нечётное число: {}!".format(s))
