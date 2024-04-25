numbers = [1, 2, 3, 4, 5]
number = 5

def func(numbers, number=2):
    result = [element * number for element in numbers]
    return result

funclambda = lambda lst, number=2: [element * number for element in lst]

result = func(numbers, number)
lambda_result = funclambda(numbers, number)

result2 = func(numbers)
lambda_result2 = funclambda(numbers)

print(result)
print("")
print(lambda_result)
print("")
print("Нет множителя: {}".format(result2))
print("Нет множителя (лямбда): {}".format(lambda_result2))
