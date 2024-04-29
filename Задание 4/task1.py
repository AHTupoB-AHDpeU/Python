natural = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadro = [x**2 for x in natural]
print(quadro)

print("")

libraries = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
set_libraries = {x.lower() for x in libraries}
print(set_libraries)


print("")

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
#  number = {n: n+1 for n in week} ???
number = {n: week.index(n)+1 for n in week}
print(number)
