def func_file(name, text):
    file = open(name, "a+",
                encoding="utf-8")
    file.read()
    file.write(text)
    file.close()

    file = open(name, "r",
                encoding="utf-8")
    element = file.readlines()
    info = [element for i, element in enumerate(element) if i%2 == 1]
    print("")
    print("Информация из чётных строк: {}".format(info))  # Выводит строку вместе с /n ???
    file.close()


name = input("Введите имя файла (новый или существующий): ")
text = ""
while text != " ":
    line = input("Введите новую строчку текста(пустая строка - завершение): ")
    if line == "":
        break
    line = line + "\n"
    text = text + line

func_file(name, text)

file1 = open(name, "r", encoding="utf-8")
s = file1.read()
n = name
print("Файл: {}".format(name))
print(s)
file1.close()
