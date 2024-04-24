string = input("Введите строку: ")
string2 = string.lower()

mydict = {}

for i in string2:
    if i == ' ':
        continue
    number = string2.count(i)
    #  print(i)
    #  print(count)
    mydict[i] = number
print(mydict)
