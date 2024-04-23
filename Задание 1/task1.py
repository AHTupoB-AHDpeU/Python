number = 0
while number != "exit":
   number = input("Введите число: ")
   if number.isdigit():
       n = len(number)
       print("Длина введённого числа:", n)
   else:
       print("Несоответствие типа данных!")
