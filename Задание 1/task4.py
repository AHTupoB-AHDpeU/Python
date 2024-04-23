ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
fire = 0
print(ship)
while fire != "exit":
    fire = input("Введите координату стрельбы: ")

    fire_up = fire.upper()
    i = ship.find(fire_up)

    if i >= 0:
        print("Попадание!")
    else:
        print("Промах!")
