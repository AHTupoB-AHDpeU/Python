dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
print(dct[1])
print(dct)
print("")

keys = set()
values = set()

for key, value in dct.items():
    keys.add(key)
    values.add(value)

print(keys)
print(values)
print("")

result = keys | values
print("Результат: {}".format(result))
